# 🛡️ **BLUE TEAM – COMANDI METERPRETER PER INVESTIGAZIONE & DFIR (LAB)**

---

# 🔵 1. **Raccolta Informazioni sulla Macchina**

### Info sistema (per capire OS, versione, patch)

```bash
sysinfo
```

### Utente attivo / token

```bash
getuid
getprivs
```

### Variabili d’ambiente (PATH sospetti)

```bash
env
```

---

# 🔍 2. **Processi (DFIR fondamentale)**

### Lista processi

```bash
ps
```

### Trovare processi sospetti

```bash
ps | grep -i powershell
ps | grep -i rundll32
ps | grep -i wscript
```

### Info su un processo specifico

```bash
ps -S <PID>
```

---

# 📌 3. **Servizi e Persistenza**

### Elenco dei servizi Windows

```bash
run post/windows/gather/enum_services
```

### Enumerazione RUN Keys

```bash
run post/windows/gather/enum_autorun
```

### Altri punti di persistenza

```bash
run post/windows/manage/registry_persistence
```

*(solo per analisi, non applica modifiche)*

---

# 🗂️ 4. **File System & Forensics**

### Lista file nella directory

```bash
ls
```

### Vedere file nascosti

```bash
ls -la
```

### Ricerca file sospetti

```bash
search -f *.exe
search -f *.dll
search -f "*password*"
search -f "*.ps1"
```

### Hash dei file (per IOC)

```bash
hashdump   # (LAB ONLY – per verificare integrità)
```

### Scaricare file per analisi DFIR

```bash
download <file>
```

### Caricare strumenti di analisi

```bash
upload <file.exe>
```

---

# 🔎 5. **Log Investigation (via Meterpreter)**

### Dump Event Logs (da analizzare offline)

```bash
run post/windows/gather/enum_eventlogs
```

### Dump Security Log

```bash
run post/windows/gather/enum_malware
```

---

# 📡 6. **Network Forensics**

### Info rete

```bash
ipconfig
```

### Tabella ARP

```bash
arp
```

### Porte aperte

```bash
netstat
```

### Enumerazione shares

```bash
run post/windows/gather/enum_shares
```

---

# 🧪 7. **Volatile Memory (LIVE RESPONSE)**

### Enumerare handle e librerie

```bash
ps -v <PID>
```

### Dumpare un processo sospetto

```bash
migrate <PID>   # per poter analizzare dal vivo
```

### Estrarre credenziali (LAB ONLY)

```bash
load kiwi
kiwi_cmd "creds_all"
```

---

# 🧹 8. **Blue Team OpSec – Pulizia & Contenimento**

### Terminare un processo malevolo

```bash
kill <PID>
```

### Rimuovere file

```bash
rm <file>
```

### Rimuovere backdoor/persistenza creata nel lab

```bash
run post/windows/manage/persistence -d
```

---

# 🔄 9. **Network Isolation (LAB)**

### Disabilitare un’interfaccia

```bash
shell
netsh interface set interface "Ethernet" admin=disabled
```

### Chiudere porte aperte

```bash
shell
netsh advfirewall firewall add rule name="block" dir=in action=block remoteport=4444
```

---

# 🕵️ 10. **Threat Hunting via Meterpreter**

### Elenco software installato (indicatori sospetti)

```bash
run post/windows/gather/enum_applications
```

### Enumerare utenti loggati

```bash
run post/windows/gather/enum_logged_on_users
```

### Enumerare credenziali wifi (per verificare compromissione)

```bash
run post/windows/gather/credentials/wifi
```

### Enumerare Scheduled Tasks

```bash
run post/windows/gather/enum_scheduled_tasks
```

---

# 📌 Vuoi la versione PDF?

Se vuoi posso crearti:

* 📘 **Blue Team Playbook COMPLETO (PDF)**
* 📄 **Cheat Sheet compatto per SOC**
* 🎓 **Versione Markdown pronta per GitHub**

Dimmi solo quale preferisci.
