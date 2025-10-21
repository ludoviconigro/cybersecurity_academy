# -*- coding: utf-8 -*
#Eseguire in Python2


import socket  # Importa il modulo socket per la comunicazione di rete
import sys     # Importa il modulo sys per accedere agli argomenti da riga di comando

def connect_to_server(server_ip, server_port):
    try:
        # Crea un socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Specifica l'indirizzo IP e la porta del server a cui connettersi
        server_address = (server_ip, server_port)

        # Stampa un messaggio che indica l'indirizzo e la porta a cui ci si sta connettendo
        print("Connessione a {} porta {}".format(server_ip, server_port))

        # Connette il socket al server
        sock.connect(server_address)

        try:
            while True:
                # Richiede all'utente di inserire un messaggio da inviare al server
                message = raw_input("Inserisci un messaggio da inviare (o 'exit' per uscire): ")

                # Se il messaggio è "exit", chiude la connessione e termina
                if message.lower() == 'exit':
                    print("Chiusura connessione...")
                    break  # Esce dal ciclo principale mantenendo una chiusura ordinata
					    # Stampa il messaggio che sta per essere inviato
                print("Invio: {}".format(message))

                # Invia il messaggio al server (in Python 2 non è necessario codificare la stringa)
                sock.sendall(message)

                # Ricezione della risposta dal server
                while True:
                    # Riceve un pacchetto di massimo 1024 byte
                    data = sock.recv(1024)

                    # Se non ci sono più dati, il server ha chiuso la connessione
                    if not data:
                        print("Connessione chiusa dal server.")
                        return

                    # Stampa la risposta ricevuta dal server
                    print("Risposta dal server: {}".format(data))

                    # Se il messaggio ricevuto è inferiore a 1024 byte, non ci sono altri dati in attesa
                    if len(data) < 1024:
                        break
        finally:
            # Chiude il socket e stampa un messaggio di chiusura
            sock.close()
            print("Connessione chiusa.")

    except Exception as e:
        # Gestisce eventuali errori e li stampa
        print("Errore: {}".format(e))
        sys.exit(1)  # Termina il programma con un codice di errore
		if __name__ == "__main__":
    # Verifica che siano stati forniti l'indirizzo IP del server e la porta
    if len(sys.argv) != 3:
        print("Uso: python client.py [indirizzo_ip_server] [porta_server]")
        sys.exit(1)  # Termina il programma se i parametri non sono corretti

    # Legge l'indirizzo IP e la porta dai parametri della riga di comando
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Avvia la connessione al server
    connect_to_server(server_ip, server_port)
