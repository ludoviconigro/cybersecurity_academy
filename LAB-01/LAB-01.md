## 🧩 Script: Cambia Indirizzo MAC (`mac_change.py`)

### 📖 Descrizione
Questo script consente di **modificare l’indirizzo MAC** di una specifica interfaccia di rete su sistemi **Linux**, utilizzando il comando `ip` del pacchetto **iproute2**.  
È utile per test di rete, esercitazioni di cybersecurity o per motivi di privacy.  
> ⚠️ **Richiede privilegi di root** per poter effettuare le modifiche.

---

### ⚙️ Funzionamento
1. Imposta i parametri `INTERFACCIA` e `NUOVO_MAC` all’inizio del file Python.  
2. Lo script verifica che il formato del MAC sia valido e che l’interfaccia esista.  
3. Disattiva l’interfaccia con `ip link set <iface> down`.  
4. Imposta il nuovo MAC con `ip link set <iface> address <mac>`.  
5. Riattiva l’interfaccia con `ip link set <iface> up`.  
6. Verifica che il MAC impostato corrisponda a quello effettivo riportato dal sistema.

---

### ▶️ Esecuzione
```bash
sudo python3 mac_change.py
```

### 💻 Esempio di Output
```bash
[i] MAC attuale di eth0: 00:11:22:33:44:55
[+] Spengo la scheda di rete eth0…
[+] Imposto il nuovo MAC 00:11:22:33:44:58 su eth0…
[+] Riattivo la scheda di rete eth0…
[i] MAC riportato dal sistema: 00:11:22:33:44:58
[✓] Indirizzo MAC cambiato con successo.
```
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🛰️ Script: icmp_request & icmp2_request con Scapy
Questi due script inviano un **ICMP Echo Request (ping)** costruito manualmente con **Scapy**, specificando indirizzo IP sorgente, destinazione e interfaccia di uscita. Entrambi richiedono privilegi di root perché inviano pacchetti raw e possono usare IP "spoofed".  

- **File principali**
  - `icmp_request.py` — versione semplice: invia l'Echo Request e mostra la risposta (o timeout).
  - `icmp2_request.py` — versione estesa: invia l'Echo Request e stampa un report dettagliato che spiega i campi IP/ICMP, preview del payload e un hexdump.

> ⚠️ Uso responsabile: questi script possono essere usati per test di rete in ambienti controllati. Non inviare pacchetti spoofed su reti pubbliche o su reti di terzi senza autorizzazione.

---

### 🔧 Requisiti
- Python 3  
- Scapy (`pip install scapy`)  
- Permessi di root (es. `sudo`)  
- Interfaccia di rete correttamente configurata (es. `eth0`) e routing adeguato per la destinazione

---

### ⚙️ Parametri comuni (da impostare nei file)
```py
SRC_IP  = "0.0.0.0"              # IP sorgente da usare (può essere spoofed)
DST_IP  = "255.255.255.255"     # IP di destinazione
IFACE   = "eth0"                # interfaccia di uscita
TIMEOUT = 2                     # timeout in secondi per la risposta
TTL     = 64                    # Time To Live
PAYLOAD = b"ping-test-scapy"    # dati trasportati nell'ICMP Echo
```
### ▶️ Esecuzione
```bash
sudo python3 icmp_request.py
# oppure per la versione estesa
sudo python3 icmp2_request.py
```

### 💻 Esempio di Output - 1
```bash
[*] Invio ICMP Echo Request da 0.0.0.0 a 255.255.255.255 su eth0…
[✓] Risposta ricevuta:
<dettagli pacchetto>
[i] Riepilogo: IP / ICMP / ...
```
### 💻 Esempio di Output - 2
```bash
[*] Invio ICMP Echo Request da 0.0.0.0 a 255.255.255.255 su eth0…
[✓] Risposta ricevuta. Dettagli ed interpretazione:

— Livello IP (Internet Protocol v4) —
  version = 4  → Versione del protocollo IP (4 per IPv4).
  ihl     = 5  → Lunghezza header IP...
  ...
— Livello ICMP (Internet Control Message Protocol) —
  type = 0 → Echo Reply
  code = 0
  id   = 4660
  seq  = 1

— Payload (dati) —
  length = 14 byte → ...
  text preview = 'ping-test-scapy'
  hex sample = 70 69 6e 67 ...

— Riepilogo sintetico —
IP / ICMP / ...
— Hexdump (pacchetto completo) —
0000  45 00 00 54 ... (etc)

```

---
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🔎 Script: ARP Sweep con Scapy (`network_arp_scan.py`)

### 📖 Descrizione
Questo script esegue un **ARP sweep** su una rete (CIDR) usando **Scapy**: invia richieste ARP in broadcast e raccoglie le risposte per scoprire host attivi. Per ogni host che risponde stampa l'indirizzo IP e l'indirizzo MAC corrispondente.  
⚠️ Richiede privilegi di root perché invia e riceve frame a livello 2 (Ethernet).

---

### 🔧 Requisiti
- Python 3  
- Scapy installato (`sudo pip3 install scapy`)  
- Esegui con privilegi elevati (es. `sudo`)  
- Interfaccia di rete correttamente configurata (es. `eth0`)

---

### ⚙️ Funzionamento (breve)
1. Analizza gli argomenti da linea di comando (network CIDR, interfaccia, timeout, verbose).  
2. Verifica che lo script sia eseguito con privilegi di root e che l'interfaccia esista.  
3. Costruisce un frame Ethernet di broadcast (`ff:ff:ff:ff:ff:ff`) contenente una richiesta ARP (`who-has`) verso la rete/CIDR specificata.  
4. Invia il pacchetto in L2 con `srp()` e attende risposte per il tempo specificato.  
5. Per ogni risposta ricevuta stampa `IP -> MAC`. Se non ci sono risposte segnala che la scansione non ha restituito host attivi.

---

### ▶️ Argomenti / Parametri
```text
-n, --network   Rete di destinazione in notazione CIDR (default: 255.255.255.255/24)
-i, --interface Interfaccia di rete da usare (default: eth0)
-t, --timeout   Timeout in secondi per attendere le risposte (default: 2)
-v, --verbose   Modalità verbosa (stampa output Scapy)
```
### ▶️ Esecuzione
```bash
sudo python3 network_arp_scan.py -n 255.255.255.255/24 -i eth0 -t 2
```
> Nota: il valore di default 255.255.255.255/24 è insolito per una rete — sostituiscilo con la rete corretta del tuo laboratorio.

### 💻 Esempio di Output
```bash
Host attivi trovati (IP -> MAC):
----------------------------------------
255.255.255.255    -> 00:11:22:33:44:55
255.255.255.254    -> 66:77:88:99:aa:bb
(altre righe...)
```
---
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
