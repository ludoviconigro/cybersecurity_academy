"""
Invia un ping (ICMP Echo Request) con Scapy specificando IP sorgente e destinazione.
- Sorgente:     0.0.0.0   (Kali, eth0)
- Destinazione: 255.255.255.255   (LabVM)
- Interfaccia:  eth0

Esecuzione:
    sudo python3 icmp_request.py
"""

import os
import sys
from scapy.all import IP, ICMP, sr1, conf

# === Parametri ===========
SRC_IP  = "0.0.0.0"   # IP della tua macchina Kali (eth0)
DST_IP  = "255.255.255.255"   # IP della macchina labvm (ens32)
IFACE   = "eth0"              # interfaccia sulla Kali
TIMEOUT = 2                   # secondi di attesa per la risposta
TTL     = 64                  # TTL del pacchetto IP
PAYLOAD = b"ping-test-scapy"
# ========================

def main():
    # Verifica privilegi: servono per impostare sorgente e inviare raw socket
    if hasattr(os, "geteuid") and os.geteuid() != 0:
        print("[!] Questo script richiede privilegi di root (sudo).")
        return 1

    # Riduci verbosità Scapy (evita log rumorosi)
    conf.verb = 0

    # Costruzione del livello IP:
    # - src: IP sorgente (spoofed/clonato)
    # - dst: IP destinazione
    # - ttl: Time To Live
    ip_layer = IP(src=SRC_IP, dst=DST_IP, ttl=TTL)

    # Costruzione del livello ICMP:
    # - type=8 -> Echo Request
    # - id/seq impostati per tracciabilità
    icmp_req = ICMP(type=8, id=0x1234, seq=1)

    # Pacchetto finale: IP / ICMP / payload
    packet = ip_layer / icmp_req / PAYLOAD

    print(f"[*] Invio ICMP Echo Request da {SRC_IP} a {DST_IP} su {IFACE}…")

    try:
        # sr1 invia e attende UNA risposta (Echo Reply) entro TIMEOUT secondi
        response = sr1(packet, iface=IFACE, timeout=TIMEOUT)

        if response is None:
            print("[!] Nessuna risposta ricevuta (timeout).")
            print("    Possibili cause: host down, filtro ICMP, anti-spoofing, route errata.")
            return 2

        # Mostra un riepilogo leggibile del pacchetto di risposta
        print("[✓] Risposta ricevuta:")
        response.show()  # dettagli completi
        print(f"[i] Riepilogo: {response.summary()}")
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
