Crea una cartella ed esegui il Comando 
```bash
git clone https://github.com/redcanaryco/atomic-red-team.git
```
Entra dentro la cartella generata e dovresti trovare la cartella atomics
```bash
cd atomic-red-team
cd atomics
```
Questo attacco corrisponde all'attacco Golden Ticket (MITRE ATT&CK T1558.001).
>Questo attacco un attacco che consiste nel creare un ticket Kerberos falso usando l’hash dell’account KRBTGT di Active Directory. Permette a un attaccante di impersonare qualsiasi utente del dominio e ottenere accesso completo e persistente alla rete.
Esegui il comando 
```bash
cd T1518    
cat T1518.md
```
Da un altro terminale, avvia Caldera e apri il browser e vai al sito  `http://localhost:8888` ed effettua il login
> il file per l'installazione e l'avvio di Caldera è presente nella cartella sotto il nome di Installazione_caldera.md
