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

## ▶️ 10. Avvio di Shellter

```bash
wine shellter.exe
```

