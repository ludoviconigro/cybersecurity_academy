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
## Conclusione

L’attacco **Golden Ticket** rappresenta una delle tecniche più potenti e persistenti nel contesto della compromissione di Active Directory. Una volta ottenuto l’hash dell’account **KRBTGT**, un attaccante può generare ticket Kerberos falsi che gli consentono di autenticarsi come qualsiasi utente del dominio, inclusi gli amministratori di dominio, senza necessità di ulteriori credenziali.

Questo tipo di attacco dimostra l’importanza della **protezione dell’autorità di autenticazione (Domain Controller)** e della corretta gestione delle chiavi Kerberos. In un ambiente di sicurezza controllato, viene utilizzato per comprendere le modalità di abuso del protocollo Kerberos e per addestrare i team di difesa a **rilevare e mitigare** tali comportamenti.

### Possibili contromisure

* **Monitorare l’attività di autenticazione Kerberos**, in particolare ticket con durate anomale o provenienti da host insoliti.
* **Ruotare periodicamente la password dell’account KRBTGT** (almeno due volte per annullare i ticket falsi esistenti).
* **Limitare i privilegi amministrativi** e segmentare la rete per ridurre l’impatto di una compromissione.
* **Implementare controlli di rilevamento avanzati (SIEM, EDR)** per individuare anomalie legate alla generazione o all’uso di ticket sospetti.

In sintesi, la comprensione del Golden Ticket è fondamentale per chi studia la sicurezza informatica: consente di approfondire i meccanismi di autenticazione di Windows e sviluppare strategie difensive più efficaci contro attacchi avanzati.

---

Vuoi che te lo formatto subito in un file `T1518.md` pronto da salvare nella cartella `atomics/T1518`?
