# DA CAMBIARE INDIRIZZI IP (ADATTATO ALLA TUA CONFIGURAZIONE)
"""
Invia un ping (ICMP Echo Request) con Scapy e, sulla risposta, stampa
un report dettagliato che spiega i campi IP e ICMP (significato e scopo).

- Sorgente:     0.0.0.0   (Kali, eth0)
- Destinazione: 255.255.255.255   (LabVM)
- Interfaccia:  eth0

Esecuzione:
    sudo python3 icmp2_request.py
"""

import os
import sys
from scapy.all import IP, ICMP, sr1, conf, hexdump, raw


# === Parametri ===========
SRC_IP  = "0.0.0.0"   # IP sorgente (Kali, eth0)
DST_IP  = "255.255.255.255"   # IP destinazione (labvm)
IFACE   = "eth0"              # Interfaccia di uscita sulla Kali
TIMEOUT = 2                   # timeout in secondi per la risposta
TTL     = 64                  # Time To Live dei pacchetti in uscita
PAYLOAD = b"ping-test-scapy"  # dati applicativi trasportati dall'ICMP Echo
# =========================


def explain_ip(ip):
    """
    Restituisce una stringa che spiega dettagliatamente i campi dell'header IP.
    """
    lines = []
    lines.append("— Livello IP (Internet Protocol v{}) —".format(ip.version))
    lines.append(f"  version = {ip.version}  → Versione del protocollo IP (4 per IPv4).")
    lines.append(f"  ihl     = {ip.ihl} (parole da 32 bit) → Lunghezza header IP (senza dati).")
    dscp = (ip.tos >> 2) & 0x3F
    ecn  = ip.tos & 0x03
    lines.append(f"  tos     = 0x{ip.tos:02x} → DSCP={dscp} (classe di servizio), ECN={ecn} (Explicit Congestion Notification).")
    lines.append(f"  len     = {ip.len} byte → Lunghezza totale (header + dati).")
    lines.append(f"  id      = {ip.id} → Identificatore: usato per riassemblare i frammenti dello stesso datagramma.")
    # Flags/frag
    try:
        df = bool(ip.flags.DF)
        mf = bool(ip.flags.MF)
    except Exception:
        df = bool(ip.flags & 0x2)
        mf = bool(ip.flags & 0x1)
    lines.append(f"  flags   = {ip.flags} → DF={'1' if df else '0'} (Don’t Fragment), MF={'1' if mf else '0'} (More Fragments).")
    lines.append(f"  frag    = {ip.frag} → Offset di frammentazione (in blocchi da 8 byte). 0 se non frammentato.")
    lines.append(f"  ttl     = {ip.ttl} → Time To Live: salta che il pacchetto può effettuare prima di essere scartato.")
    lines.append(f"  proto   = {ip.proto} → Protocollo di livello superiore: 1=ICMP, 6=TCP, 17=UDP, ecc.")
    lines.append(f"  chksum  = 0x{ip.chksum:04x} → Checksum header IP per rilevare errori nell’header.")
    lines.append(f"  src     = {ip.src} → Indirizzo IP sorgente.")
    lines.append(f"  dst     = {ip.dst} → Indirizzo IP destinazione.")
    if ip.options:
        lines.append(f"  options = {ip.options} → Opzioni IP (rare): timestamp, record route, security, ecc.")
    else:
        lines.append("  options = (nessuna) → Normalmente assenti per semplicità e performance.")
    return "\n".join(lines)


def explain_icmp(icmp):
    """
    Restituisce una stringa che spiega dettagliatamente i campi dell'header ICMP.
    """
    lines = []
    lines.append("— Livello ICMP (Internet Control Message Protocol) —")
    lines.append(f"  type   = {icmp.type} → Tipo messaggio ICMP (0=Echo Reply, 8=Echo Request, 3=Dest Unreachable, 11=Time Exceeded, ecc.).")
    lines.append(f"  code   = {icmp.code} → Sottocodice che affina il significato del tipo (per Echo è 0).")
    lines.append(f"  chksum = 0x{icmp.chksum:04x} → Checksum ICMP su header+dati per rilevare errori.")
    if hasattr(icmp, "id"):
        lines.append(f"  id     = {icmp.id} → Identificatore Echo: accoppia richiesta e risposta (utile con più ping concorrenti).")
    if hasattr(icmp, "seq"):
        lines.append(f"  seq    = {icmp.seq} → Numero di sequenza Echo: indica l’ordine dei pacchetti.")
    return "\n".join(lines)


def explain_payload(pkt):
    """
    Restituisce una stringa con info sul payload (dati applicativi) trasportato dall’ICMP.
    """
    data = bytes(pkt[ICMP].payload) if pkt.haslayer(ICMP) else b""
    lines = []
    lines.append("— Payload (dati) —")
    lines.append(f"  length = {len(data)} byte → Dati trasportati dal messaggio ICMP (eco del mittente).")
    if len(data):
        preview = data.decode('utf-8', errors='replace')
        lines.append(f"  text preview = {preview!r} → Anteprima interpretabile come testo (UTF-8, con sostituzioni).")
        hex_sample = " ".join(f"{b:02x}" for b in data[:32])
        lines.append(f"  hex sample (primi 32 B) = {hex_sample}")
    else:
        lines.append("  (vuoto)")
    return "\n".join(lines)


def main():
    # Verifica privilegi: servono per impostare sorgente e inviare raw socket
    if hasattr(os, "geteuid") and os.geteuid() != 0:
        print("[!] Questo script richiede privilegi di root (sudo).")
        return 1

    conf.verb = 0  # riduce il rumore di Scapy in console

    # Costruzione pacchetto in uscita: IP / ICMP / payload
    ip_layer   = IP(src=SRC_IP, dst=DST_IP, ttl=TTL)
    icmp_req   = ICMP(type=8, id=0x1234, seq=1)  # Echo Request
    packet_out = ip_layer / icmp_req / PAYLOAD

    print(f"[*] Invio ICMP Echo Request da {SRC_IP} a {DST_IP} su {IFACE}…")

    try:
        # sr1 invia e attende UNA risposta (Echo Reply atteso: type=0)
        response = sr1(packet_out, iface=IFACE, timeout=TIMEOUT)

        if response is None:
            print("[!] Nessuna risposta ricevuta (timeout).")
            print("    Possibili cause: host down, filtro ICMP, anti-spoofing, route errata.")
            return 2

        print("[✓] Risposta ricevuta. Dettagli ed interpretazione:\n")

        # 1) Spiegazione IP
        if response.haslayer(IP):
            print(explain_ip(response[IP]))
        else:
            print("(!) Nessun header IP rilevato nella risposta (non comune).")

        print()  # riga vuota

        # 2) Spiegazione ICMP
        if response.haslayer(ICMP):
            print(explain_icmp(response[ICMP]))
        else:
            print("(!) Nessun header ICMP: la risposta non è ICMP (inatteso per un echo).")

        print()  # riga vuota

        # 3) Payload (eco dei dati inviati)
        print(explain_payload(response))

        print()  # riga vuota

        # 4) Riepilogo breve e hexdump opzionale (diagnostica binaria)
        print("— Riepilogo sintetico —")
        print(response.summary())
        print("\n— Hexdump (pacchetto completo) —")
        hexdump(response)

        return 0

    except PermissionError:
        print("[!] Permesso negato: esegui con sudo.")
        return 3
    except OSError as e:
        print(f"[!] Errore di sistema: {e}")
        return 4
    except Exception as e:
        print(f"[!] Errore imprevisto: {e}")
        return 5


if __name__ == "__main__":
    sys.exit(main())
