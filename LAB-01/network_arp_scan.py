#!/usr/bin/env python3
"""
ARP Sweep con Scapy
- Invia un ARP Request in broadcast su una rete (CIDR) e raccoglie le risposte.
- Stampa IP e MAC degli host che rispondono.

Esecuzione:
    sudo python3 network_arp_scan.py -n 255.255.255.255/24 -i eth0 -t 2
"""

import sys
import os
import argparse

try:
    # Scapy fornisce i layer di rete (Ether, ARP) e le funzioni di invio/ricezione (srp)
    from scapy.all import Ether, ARP, srp, get_if_list
except ImportError:
    print("[ERRORE] Scapy non è installato. Installa con: sudo pip3 install scapy")
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="ARP sweep semplice con Scapy")
    parser.add_argument(
        "-n", "--network", default="255.255.255.255/24",
        help="Rete di destinazione in notazione CIDR (default: 255.255.255.255/24)"
    )
    parser.add_argument(
        "-i", "--interface", default="eth0",
        help="Interfaccia di rete da usare (default: eth0)"
    )
    parser.add_argument(
        "-t", "--timeout", type=int, default=2,
        help="Timeout in secondi per attendere le risposte (default: 2)"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Modalità verbosa di Scapy"
    )
    return parser.parse_args()


def main():
    # Verifica permessi: per inviare frame L2 serve normalmente l'utente root
    if hasattr(os, "geteuid") and os.geteuid() != 0:
        print("[ERRORE] Esegui lo script con privilegi elevati (es. sudo).")
        sys.exit(1)

    args = parse_args()

    # Controllo rapido che l'interfaccia esista sul sistema
    if args.interface not in get_if_list():
        print(f"[ERRORE] Interfaccia '{args.interface}' non trovata. Interfacce disponibili:")
        for iface in get_if_list():
            print(f" - {iface}")
        sys.exit(1)

    # Indirizzo MAC di broadcast: tutti i bit a 1 -> ff:ff:ff:ff:ff:ff
    broadcast_mac = "ff:ff:ff:ff:ff:ff"

    # Layer 2 (Ethernet):
    # - dst=broadcast_mac: invia il frame a tutti i nodi del dominio di broadcast L2
    ether_layer = Ether(dst=broadcast_mac)

    # Layer ARP (Address Resolution Protocol):
    # - op=1 (who-has): richiesta ARP per sapere "chi ha" un dato IP
    # - pdst = rete/host di destinazione (accetta anche range in CIDR, es. 192.168.1.0/24)
    arp_layer = ARP(op=1, pdst=args.network)

    # Costruzione del pacchetto completo:
    # - In Scapy l'operatore '/' concatena i layer in ordine (Ethernet / ARP)
    packet = ether_layer / arp_layer

    # Invio e ricezione in L2 con srp (send/receive packets at layer 2):
    # - iface: interfaccia da usare
    # - timeout: quanto attendere le risposte
    # - verbose: stampa dettagli interni di Scapy
    # Ritorna una tupla (risposte, non_risposte). 'risposte' è una lista di coppie (snd, rcv)
    ans, unans = srp(
        packet,
        iface=args.interface,
        timeout=args.timeout,
        verbose=1 if args.verbose else 0
    )

    # Intestazione output
    print("\nHost attivi trovati (IP -> MAC):")
    print("-" * 40)

    # Scansione delle risposte
    # Ogni elemento 'rcv' è un pacchetto di risposta: un ARP reply incapsulato in un frame Ethernet
    found = 0
    for _snd, rcv in ans:
        # rcv[ARP].psrc = IP sorgente nel pacchetto ARP di risposta (l'host che risponde)
        ip = rcv[ARP].psrc

        # rcv[Ether].src = MAC address sorgente del frame Ethernet (MAC dell'host che risponde)
        mac = rcv[Ether].src

        # Stampa formattata
        print(f"{ip:15} -> {mac}")
        found += 1

    if found == 0:
        print("(nessuna risposta)")

    # Nota su alcuni campi utili (approfondimento):
    # - ARP.op: 1 = who-has (request), 2 = is-at (reply)
    # - ARP.psrc / ARP.pdst: IP sorgente/destinazione a livello ARP
    # - ARP.hwsrc / ARP.hwdst: MAC sorgente/destinazione a livello ARP
    # - Ether.src / Ether.dst: MAC sorgente/destinazione del frame Ethernet
    # Per un singolo pacchetto 'rcv', puoi ispezionare tutti i campi con: rcv.show()


if __name__ == "__main__":
    main()
