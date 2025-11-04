## Che cos'è (a livello concettuale)

Questo file descrive a livello generale il concetto di *reverse shell*.
Una reverse shell è una tecnica in cui una macchina (il *client* o *implant*) apre una connessione verso una macchina di controllo (tipicamente un *listener* su una workstation dell'analista/attaccante) e fornisce un canale che permette l'esecuzione remota di comandi sulla macchina che ha stabilito la connessione. Lo scopo tecnico può essere legittimo (ad es. test di sicurezza in ambiente autorizzato, gestione remota controllata) o illecito se usato senza permesso.

## Cosa fa lo script (descrizione non operativa)

Lo script che hai mostrato crea un canale di comunicazione persistente tra la macchina che esegue lo script e una macchina remota indicata da IP e porta. Attraverso quel canale, chi controlla il listener può inviare comandi che saranno eseguiti sulla macchina che ha lanciato lo script. Il meccanismo usa una *named pipe* (FIFO) come meccanismo interno per passare i dati verso e dalla shell.

## Macchine Coinvolte
- Macchina Vittima : Ubuntu
- Macchina Attaccante : Kali Linux

## Cosa fa lo script (descrizione non operativa)
Come avviarlo 
1 - dai i permessi con il comando nella macchina Vittima
```bash
chmod +x implant.sh
```
2 - dalla macchina attacante apri la porta attraverso il comando 
```bash
nc -lvp 443
```
3 - dalla macchina Vittima fai partire il file attraverso il comando 
```bash
./implant.sh
```
4 - Dalla macchina Attaccante si aprirà una shell collagata al computer della vittima

## Perché è pericoloso

* Offre accesso remoto diretto alla shell del sistema: chi ottiene accesso può eseguire qualunque comando con i privilegi dell'utente che avvia lo script.
* Può essere usato per compromissione, movimento laterale, raccolta di credenziali o esfiltrazione di dati.
* Spesso è usato da attori malevoli; la sua presenza sui sistemi è un forte indicatore di compromissione.

## Uso consentito e raccomandazioni di sicurezza (solo in ambiente autorizzato)

* Usalo **solo** in laboratori isolati (VM non connesse a risorse di produzione), con immagini snapshot e con autorizzazione esplicita.
* Non eseguire su macchine di produzione, reti aziendali reali o su sistemi di terzi senza permesso scritto.
* Quando sperimenti, monitora la rete e i processi, tieni snapshot/backup e isola l'ambiente (rete NAT interna, VLAN di laboratorio, ecc.).
* Logga ogni esperimento e conserva evidenze per scopi di apprendimento e di audit.

## Come rilevare e mitigare (linee guida generiche)

* Monitorare connessioni in uscita anomale verso porte non usuali o IP pubblici.
* Regole IDS/IPS per rilevare pattern tipici di shell reverse.
* Eseguire scansioni di integrità dei file e controllare processi/pipes sospette.
* Applicare least privilege, patching e restrizioni di egress network per ridurre la probabilità di connessioni non autorizzate.

## Nota legale ed etica

L'uso di strumenti e script che consentono l'accesso remoto a sistemi altrui senza consenso è illegale nella maggior parte delle giurisdizioni e contrario all'etica professionale. Lavorare in un "academy di cybersecurity" richiede di attenersi a regole di autorizzazione e responsabilità: esercitati solo su risorse di tua proprietà o in laboratori espressamente autorizzati.

---

