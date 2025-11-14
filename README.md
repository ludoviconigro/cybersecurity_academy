# 🧠 Cybersecurity Academy — Repository di Studio Personale

Questa repository raccoglie **materiale di studio personale** e codice prodotto durante il percorso formativo della **Cybersecurity Academy**.  
Contiene esercitazioni, script e laboratori svolti durante le lezioni e i moduli pratici, con l’obiettivo di **comprendere e sperimentare in modo sicuro** i principali concetti di **sicurezza informatica**, **analisi di rete** e **cyber defense**.

---
### 💻 Macchine virtuali utilizzate in VMware

Durante le attività di laboratorio in ambiente controllato, ho utilizzato le seguenti macchine virtuali tramite **VMware Workstation**:

* **Metasploitable2-Linux**
* **FreeBSD version 10 and earlier 64-bit**
* **Cybersecurity_Lab_VM_Workstation_20250409**
* **Ubuntu_24.04_VM_LinuxVMImages.COM**
* **Tenable-Core-OL8-Nessus-20250923**
* **kali-linux-2025.3-vmware-amd64**
* **Windows 7 x64**

In aggiunta, ho impiegato un **emulatore Android** con:

* **Dispositivo virtuale:** Pixel 2
* **API Level:** 33 (“Tiramisu”)
* **Versione Android:** 13.0

---


## 📂 Cartelle dei Laboratori

Ogni cartella rappresenta un laboratorio pratico (es. `LAB-01`, `LAB-02`, ...).  
In ciascun lab sono inclusi script, spiegazioni e test didattici relativi a uno specifico argomento di rete o sicurezza.

---
### `LAB-01`
Introduzione alle analisi di rete di base:
- **ICMP e ARP** con Scapy  
- **Cambio indirizzo MAC** e manipolazione interfacce di rete  
- **Rilevamento host attivi** (ARP Sweep)  
- **ARP Spoofing**
---
## `LAB-02`
Implementazione di tecniche fondamentali di comunicazione e attacco in rete tramite Python:
### **Botnet**
Architetture e comunicazioni tra nodi:
* **Modello Client-Server** di una botnet (server di comando e client che si collegano)
* **Architettura P2P** con comunicazione multicast per la distribuzione dei comandi
* Studio del funzionamento delle botnet e gestione del C2 (Command & Control)
### **encryiption**
Esempi introduttivi di cifratura e gestione chiavi:
* **AES-256** (file esplicativo)
* **Cifrario di Cesare** implementato in Python
* **Generazione chiave pubblica/privata** e concetti base di crittografia asimmetrica
### **reverse_shell**
Implementazione di connessioni remote:
* **Reverse shell client** che esegue comandi ricevuti dal server
* **Reverse shell server** per il controllo remoto della macchina bersaglio (sempre in ambiente controllato)
### **syn_scan.py**
Strumento per il port scanning:
* **SYN Scan TCP** per identificare porte aperte utilizzando packet crafting
* Analisi del comportamento della vittima tramite risposte SYN/ACK o RST
---
## `LAB-03`
Sicurezza delle comunicazioni, generazione certificati e simulazione di attacchi tramite rete:
### **SSL**
Implementazione di comunicazioni sicure:
* **Server SSL** che accetta connessioni cifrate
* **Gestione dei socket sicuri** tramite certificati
* File di comandi utili per generare e utilizzare certificati X.509
### **net_ransomware**
Simulazione (in ambiente controllato) del comportamento di un ransomware:
* **Server** che genera e distribuisce le chiavi di cifratura
* **Client** che cifra i file utilizzando la chiave ricevuta
* File di output per verificare il risultato dell’operazione
### **server_client_cert_gen**
Generazione automatizzata dei certificati:
* Script Python per creare **chiavi private**, **CSR** e **certificati server/client**
* Introduzione pratica ai concetti di **PKI**, certificazione e fiducia nelle comunicazioni crittografate
---
## `LAB-07`
Analisi e sfruttamento (in ambiente controllato) di vulnerabilità note nelle comunicazioni sicure:
### **Hearbleed**
Studio della vulnerabilità CVE-2014-0160 (Heartbleed):
* Analisi di come l’**estensione Heartbeat** di OpenSSL possa essere sfruttata
* Esempi pratici di **estrazione di memoria** dal server vulnerabile
* Comprensione dell’impatto su chiavi private, sessioni e dati sensibili
---
## `LAB-08`
Studio e implementazione di shell remote e trojan multi-piattaforma in ambiente controllato:
### **SHELL_SECOND_COMPUTER**
Implementazione di una reverse shell realistica:
* Script **implant.sh** per creare un agente che stabilisce una connessione remota verso un listener
* Documentazione concettuale nel **ReadMe.md**, che spiega il funzionamento della reverse shell e il flusso di comunicazione tra macchina vittima e macchina di controllo
### **TROJAN**
Realizzazione di trojan basilari per diverse piattaforme:
* **Android**: due esempi di payload e spiegazioni operative
* **Linux**: versione semplice del trojan per sistemi Unix-like
* **Windows**: variante dedicata agli ambienti Microsoft
* **TROJAN_con_Deb**: versione con configurazione specifica per sistemi Debian-based
---
## `LAB-09`
Analisi e sviluppo di componenti malevoli a basso livello e tecniche di intercettazione in ambiente controllato:
### **Kernel**
Introduzione allo sviluppo di moduli kernel Linux:
* **hello.c**: esempio base di modulo caricabile (LKM) per comprendere hook, log e interazione col kernel
* **Makefile** per la compilazione del modulo tramite `make`
* **command.md** con i comandi fondamentali per compilare, caricare ed effettuare il debug del modulo (es. `insmod`, `dmesg`, `rmmod`)
### **Keylogger**
Implementazione di un keylogger semplice in Python:
* **Keylogger.py** mostra come intercettare input da tastiera e registrarli su file
* Utilizzato per comprendere le tecniche di raccolta input lato utente e la loro gestione sicura in un laboratorio controllato
---
## `LAB-10`
Tecniche di attacco e analisi su reti wireless e applicazioni web, in ambiente controllato:
### **CRACK_WIFI**
Esempio pratico di attacco WPA2:
* Procedura completa per **catturare il 4-way handshake** tramite airmon-ng, airodump-ng e aireplay-ng
* Sniffing del traffico con **Wireshark**
* Tentativo di **crack della chiave WPA2** tramite Aircrack-ng o servizi di cracking online
* Note operative su interfacce Wi-Fi, modalità monitor e perdita di connettività
### **SQL**
Dimostrazione di SQL Injection:
* File di comandi e teoria essenziale per comprendere come un input non validato possa manipolare query SQL
* Test in ambiente sicuro su applicazioni vulnerabili
### **XSS_attack**
Esecuzione di attacchi XSS tramite BeEF:
* Installazione e avvio di **BeEF (Browser Exploitation Framework)**
* Attivazione dell’hook JavaScript sulla vittima tramite link dedicato
* Uso della dashboard BeEF: comandi, controllo browser e raccolta informazioni
* Dimostrazione dei moduli: redirect, alert, phishing, sniffing credenziali, identificazione host nella LAN
---
## `LAB-11`
Esecuzione di attività Red Team in ambiente controllato tramite piattaforme dedicate all’automazione degli attacchi:
### **Caldera**
Utilizzo del framework MITRE Caldera:
* File di **Installazione** per la configurazione completa dell’ambiente
* File **Attacco** con esempi di esecuzione di operazioni automatiche tramite agenti
* Comprensione dei plugin, dei profili MITRE ATT&CK e delle campagne simulate
### **Covenant**
Piattaforma C2 moderna basata su .NET:
* **Installazione** della piattaforma e configurazione dei listener
* File **Attacco** con esempi di utilizzo degli agenti (Grunts)
* Gestione dei comandi, sessioni e moduli integrati per movimento laterale e raccolta informazioni
### **Wine**
Ambiente Windows simulato tramite Wine:
* File di **Installazione** per configurare un ambiente Wine adatto all’esecuzione di payload Windows
* File **Attacco** con esempi di creazione ed esecuzione di payload compatibili Win32
* **comandi_meterpreter.md** con i comandi principali usati in sessione Meterpreter (post-exploitation, raccolta info, persistenza, ecc.)
### **General_command.md**
Raccolta di comandi generali Red Team:
* Insieme di istruzioni utili per operazioni comuni di attacco e post-exploitation
* Riferimenti rapidi a comandi cross-tool (Caldera, Covenant, Wine, Meterpreter)
---
<div align="center" style="border:4px solid #c0392b; padding:18px; border-radius:10px; background:#fff5f5;">

  <h2 style="margin:0; color:#c0392b;">⚠️ DISCLAIMER — USO RESPONSABILE E LIMITAZIONE DI RESPONSABILITÀ</h2>

  <p style="margin:12px 0 0; font-weight:600; max-width:800px; text-align:justify;">
  Il materiale presente in questa repository è fornito esclusivamente a <strong>fini didattici e di apprendimento</strong> nell’ambito del percorso formativo della <strong>Cybersecurity Academy</strong>.
  Tutti gli esempi e gli script devono essere eseguiti <strong>solo</strong> in ambienti controllati, isolati e virtualizzati
  (ad es. VM in una rete privata o VLAN di laboratorio), utilizzando le macchine virtuali <strong>Ethical Hacker Kali Linux</strong> e <strong>LabVM Workstation</strong>.
  </p>

  <p style="margin:12px 0 0; text-align:justify;">
  L’autore di questa repository <strong>non si assume alcuna responsabilità</strong> per danni, perdite di dati o conseguenze legali derivanti dall’uso improprio dei materiali.
  Non è consentito l’utilizzo degli script o delle tecniche descritte su sistemi o reti di terzi senza <strong>autorizzazione esplicita</strong>.
  </p>

  <p style="margin:12px 0 0; text-align:justify;">
  Questa repository ha esclusivamente finalità <strong>educative</strong> e serve a documentare il percorso di apprendimento tecnico
  in ambito <strong>cybersecurity</strong>, con focus sulla <strong>difesa, l’analisi e la prevenzione</strong>.
  </p>

</div>

---

## 🧾 Note finali
Tutti i laboratori e gli script sono parte del mio percorso di formazione e sperimentazione personale.  
Gli argomenti affrontati vanno dalla rete e protocolli base, fino a concetti avanzati di sicurezza e ethical hacking, sempre in contesti **legali, virtuali e controllati**.
