"""
Script per cambiare l'indirizzo MAC di un'interfaccia di rete su Linux
usando il comando 'ip' (pacchetto iproute2). Richiede privilegi di root.

Istruzioni:
1) Imposta INTERFACCIA e NUOVO_MAC nelle costanti qui sotto.
2) Esegui con: sudo python3 mac_change.py 
"""

import re
import subprocess
import sys

# === PARAMETRI DA PERSONALIZZARE ============================================
INTERFACCIA = "eth0"                 # es. "eth0", "wlan0", "enp3s0", ecc.
NUOVO_MAC   = "00:11:22:33:44:58"    # formato XX:XX:XX:XX:XX:XX
# ============================================================================


def run(cmd):
    """
    Esegue un comando di sistema e solleva un'eccezione se fallisce.
    - cmd: lista di stringhe (es. ["ip", "link", "set", "eth0", "down"])
    Usiamo check=True per far alzare CalledProcessError in caso di errore.
    """
    subprocess.run(cmd, check=True)


def get_current_mac(iface):
    """
    Ritorna l'indirizzo MAC corrente dell'interfaccia 'iface'
    leggendo l'output di 'ip link show <iface>'.
    Se non viene trovato, ritorna None.
    """
    out = subprocess.check_output(["ip", "link", "show", iface], text=True)
    m = re.search(r"link/ether\s+([0-9a-f:]{17})", out, re.IGNORECASE)
    if m:
        return m.group(1)
    return None


def is_valid_mac(addr):
    """
    Verifica che la stringa 'addr' sia un MAC valido nel formato XX:XX:XX:XX:XX:XX
    composto da cifre esadecimali.
    """
    return re.fullmatch(r"[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}", addr) is not None


def main():
    iface = INTERFACCIA
    new_mac = NUOVO_MAC

    # 1) Validazione input
    if not iface:
        print("[!] Interfaccia non specificata.")
        return 1
    if not is_valid_mac(new_mac):
        print("[!] MAC non valido: {} (usa formato XX:XX:XX:XX:XX:XX).".format(new_mac))
        return 1

    try:
        # 2) MAC attuale (prima della modifica)
        current_before = get_current_mac(iface)
        print("[i] MAC attuale di {}: {}".format(iface, current_before))

        # 3) Porta giù l'interfaccia per consentire il cambio MAC
        print("[+] Spengo la scheda di rete {}…".format(iface))
        run(["ip", "link", "set", iface, "down"])

        # 4) Imposta il nuovo MAC
        print("[+] Imposto il nuovo MAC {} su {}…".format(new_mac, iface))
        run(["ip", "link", "set", iface, "address", new_mac])

        # 5) Riporta su l'interfaccia
        print("[+] Riattivo la scheda di rete {}…".format(iface))
        run(["ip", "link", "set", iface, "up"])

        # 6) Verifica finale
        current_after = get_current_mac(iface)
        print("[i] MAC riportato dal sistema: {}".format(current_after))

        if current_after and current_after.lower() == new_mac.lower():
            print("[✓] Indirizzo MAC cambiato con successo.")
            return 0
        else:
            print("[!] Attenzione: il MAC non coincide con quello richiesto.")
            print("    Possibili cause: NetworkManager, driver, o policy del sistema.")
            return 2

    except subprocess.CalledProcessError as e:
        print("[!] Errore di sistema durante l'esecuzione: {}".format(e))
        return 3
    except FileNotFoundError:
        print("[!] Comando 'ip' non trovato. Installa il pacchetto 'iproute2'.")
        return 4
    except Exception as e:
        print("[!] Errore imprevisto: {}".format(e))
        return 5


if __name__ == "__main__":
    sys.exit(main())





