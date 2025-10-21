#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
import threading

class BotRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_ip = self.client_address[0]
        thread_name = threading.current_thread().name
        print(f"[{thread_name}] Connessione ricevuta da: {client_ip}")
        
        try:
            while True:
                data_bytes = self.request.recv(1024)
                if not data_bytes:
                    break

                received_message = data_bytes.decode('utf-8').strip()
                print(f"[{thread_name}] Bot {client_ip} ha inviato: '{received_message}'")

                # Trasforma tutta la stringa in maiuscolo, compresi eventuali spazi
                response_message = received_message.upper()

                # Invia risposta codificata
                self.request.sendall(response_message.encode('utf-8'))

        except ConnectionResetError:
            print(f"[{thread_name}] La connessione con {client_ip} è stata interrotta bruscamente.")
        except Exception as e:
            print(f"[{thread_name}] Errore durante la gestione della connessione con {client_ip}: {e}")
        finally:
            print(f"[{thread_name}] Connessione chiusa con: {client_ip}")


def main():
    HOST, PORT = "0.0.0.0", 8000
    socketserver.ThreadingTCPServer.allow_reuse_address = True

    try:
        with socketserver.ThreadingTCPServer((HOST, PORT), BotRequestHandler) as server:
            print(f"Server multithread in ascolto su {HOST}:{PORT}")
            print("Premi CTRL+C per arrestare il server.")
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nArresto del server richiesto dall'utente...")
    finally:
        print("Server arrestato.")

if __name__ == "__main__":
    main()
