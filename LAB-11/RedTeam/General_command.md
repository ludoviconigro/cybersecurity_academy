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
---
---
---
## 📘 Conclusione

All’interno della cartella `atomics` è possibile trovare una vasta raccolta di test di simulazione basati sul framework **MITRE ATT&CK**.
Ogni test (chiamato *atomic test*) rappresenta una singola tecnica di attacco, descritta in modo dettagliato e accompagnata dai comandi necessari per riprodurla **in ambiente sicuro e controllato**.

Questa repository, sviluppata da **Red Canary**, è uno strumento fondamentale per **valutare la capacità di rilevamento e risposta di un sistema di sicurezza**.
Permette infatti di:

* comprendere meglio le tattiche e tecniche usate dagli attaccanti reali;
* testare e migliorare i sistemi di **monitoraggio, logging e difesa**;
* addestrare il personale di sicurezza in scenari realistici ma sicuri.

> ⚠️ Tutti i test devono essere eseguiti **esclusivamente in un ambiente di laboratorio isolato**, poiché simulano comportamenti malevoli che, in un contesto produttivo, potrebbero compromettere la sicurezza del sistema.

