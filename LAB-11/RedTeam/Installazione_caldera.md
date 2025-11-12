
# Installazione Caldera (versione manuale da sorgente)

## ⚠️ Avvertenze importanti
Disinstallare eventuali versioni precedenti di Caldera** prima di seguire questi passaggi per evitare conflitti:  
   ```bash
   sudo apt purge caldera -y
   sudo apt autoremove --purge -y
   sudo rm -rf /usr/share/caldera /var/lib/caldera /etc/caldera
```

1. **Clonare Caldera dal repository ufficiale MITRE**:

   ```bash
   git clone https://github.com/mitre/caldera.git
   ```

2. **Modifica file `requirements.txt`** prima di installare le dipendenze:
   cerca la riga

   ```
   lxml~=4.9.1
   ```

   e sostituiscila con:

   ```bash
   lxml>=5.2,<6
   # oppure, se serve una versione specifica:
   # lxml==5.2.1 (o > 5.2 se disponibile)
   ```

---

## 🧩 Procedura di installazione

### 1. Installa python3-venv

```bash
sudo apt install python3-venv python3-full
```

### 2. Vai nella directory di Caldera

```bash
cd caldera
```

### 3. Crea un virtual environment

```bash
python3 -m venv venv
```

### 4. Attiva il virtual environment

```bash
source venv/bin/activate
```

### 5. Ora installa i requisiti (il prompt cambierà in "(venv)")

```bash
pip3 install -r requirements.txt
```

### 6. Avvia Caldera

```bash
python3 server.py --insecure --build
```

---

## 🔧 In caso l'ultimo comando dia errore

### 1. Assicurati di essere nella directory caldera (già ci sei)

```bash
cd ~/Desktop/HACK12/Caldera/caldera
```

### 2. Scarica tutti i submodule (plugin) mancanti

```bash
git submodule update --init --recursive
```

### 3. Installa Node.js se manca (per Vue UI)

```bash
sudo apt install -y nodejs npm
```

### 4. Con il virtual environment attivo, riavvia Caldera

```bash
source venv/bin/activate
python3 server.py --insecure --build
```
* L’interfaccia web è accessibile da browser su `http://localhost:8888`
> Credenziali default (modalità insecure):
>> Username: red  
>> Password: admin
