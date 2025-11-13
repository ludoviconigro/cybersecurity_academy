# Installazione di Wine per Shellter su Kali Linux

Di seguito i passaggi necessari per installare Wine e preparare l’ambiente per utilizzare Shellter. I comandi riportati sono esattamente quelli richiesti.

---

## 🔧 1. Installazione preliminare di Wine

```bash
sudo apt install wine -y
```

---

## 📦 2. Scaricare Shellter dal sito ufficiale

Scaricare il file ZIP da:

[https://www.shellterproject.com/download/](https://www.shellterproject.com/download/)

---

## 📁 3. Preparazione della cartella in /opt

```bash
cd /opt
sudo mkdir shellter
cd shellter
sudo cp /home/kali/Downloads/shellter.zip ./
```

---

## 🔄 4. Aggiornamento dei pacchetti

```bash
sudo apt update
ls
```

---

## 📦 5. Estrazione di Shellter

```bash
sudo unzip shellter.zip
```

---

## 🏗️ 6. Abilitazione dell’architettura i386

```bash
sudo dpkg --add-architecture i386
```

---

## 🍷 7. Installazione di Wine (seconda installazione richiesta)

```bash
sudo apt install wine -y
```

---

## 🍷 8. Tentativo di installazione di wine32

```bash
sudo apt install wine32
```

---

## 🔍 9. Verifica della versione di Wine

```bash
wine --version
```

---

# Installazione di Wine per Shellter su Kali Linux

## 🔟 10. Lista dei file estratti

```
ls               
shellter  shellter.zip
```

---

## 1️⃣1️⃣ 11. Entrare nella cartella di Shellter

```
cd shellter
```

---

## 1️⃣2️⃣ 12. Verificare i file interni

```
ls
docs  Executable_SHA-256.txt  licenses  shellcode_samples  shellter.exe
```

---

## 1️⃣3️⃣ 13. Avvio di Shellter

```
wine shellter.exe




        1010101 01   10 0100110 10     01  11001001 0011101 001001
        11      10   01 00      01     01     01    10      11   10                                                                                                                                
        0010011 1110001 11011   11     10     00    10011   011001                                                                                                                                 
             11 00   10 01      11     01     11    01      01   11                                                                                                                                
        0010010 11   00 0011010 100111 000111 00    1100011 01   10 v7.2                                                                                                                           
        www.ShellterProject.com                     Wine Mode                                                                                                                                      
                                                                                                                                                                                                   
                                                                                                                                                                                                   
                                                                                                                                                                                                   
Choose Operation Mode - Auto/Manual (A/M/H):
```


