#!/usr/bin/env python3
"""
Implementazione completa di un server e client SSL con autenticazione mutua.
Include generazione automatica di certificati e gestione robusta degli errori.

1. copiare il codice sia su server, sia su client

2. generare certificati su server col comando: python3 server_client_cert_gen.py gen_certs

3. copiare sul client i files: ca_cert.pem, client_cert.pem e client key.pem

4. avviare il server col comando: python3 server_client_cert_gen.py server <ip del server>

5 avviare il client col comando: python3 server_client_cert_gen.py client <ip del server>

"""

import socket
import ssl
import os
import sys
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime

# =============== CONFIGURAZIONE ===============
PORT = 4433                      # Porta di ascolto del server
BUFFER_SIZE = 1024               # Dimensione del buffer di comunicazione
BACKLOG = 5                      # Numero massimo di connessioni in coda

# Nomi file certificati
CA_CERT_FILE = 'ca_cert.pem'     # Certificato della CA
CA_KEY_FILE = 'ca_key.pem'       # Chiave privata della CA
SERVER_CERT_FILE = 'server_cert.pem'  # Certificato del server
SERVER_KEY_FILE = 'server_key.pem'    # Chiave privata del server
CLIENT_CERT_FILE = 'client_cert.pem'  # Certificato del client
CLIENT_KEY_FILE = 'client_key.pem'    # Chiave privata del client

# Informazioni per la Certificate Authority
CA_INFO = {
    "country": "IT",
    "state": "Italy",
    "locality": "Rome",
    "organization": "My CA",
    "common_name": "myca.example.com",
    "valid_days": 3650  # 10 anni
}

# Informazioni per il certificato del server
SERVER_INFO = {
    "country": "IT",
    "state": "Italy",
    "locality": "Milan",
    "organization": "Server Org",
    "common_name": "server.example.com",  # Deve matchare l'hostname
    "valid_days": 365  # 1 anno
}

# Informazioni per il certificato del client
CLIENT_INFO = {
    "country": "IT",
    "state": "Italy",
    "locality": "Turin",
    "organization": "Client Device",
    "common_name": "client.example.com",
    "valid_days": 365  # 1 anno
}

# =============== FUNZIONI PER LA GENERAZIONE DEI CERTIFICATI ===============

def genera_chiave_privata(key_file: str, key_size: int = 2048) -> rsa.RSAPrivateKey:
    """
    Genera una chiave privata RSA e la salva su file in formato PEM.
    
    Args:
        key_file: Percorso del file dove salvare la chiave
        key_size: Dimensione della chiave in bit (default 2048)
    
    Returns:
        Oggetto chiave privata generato
    """
    # Generazione chiave RSA con esponente pubblico 65537
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    
    # Scrittura su file in formato PEM senza password
    with open(key_file, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    return private_key

def genera_certificato_ca() -> tuple:
    """
    Genera un certificato self-signed per la Certificate Authority (CA).
    
    Returns:
        Tupla contenente (chiave_privata_CA, certificato_CA)
    """
    print("Generando certificato CA...")
    
    # 1. Genera la chiave privata della CA
    ca_key = genera_chiave_privata(CA_KEY_FILE)
    
    # 2. Crea subject e issuer (uguali per certificato self-signed)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, CA_INFO["country"]),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, CA_INFO["state"]),
        x509.NameAttribute(NameOID.LOCALITY_NAME, CA_INFO["locality"]),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, CA_INFO["organization"]),
        x509.NameAttribute(NameOID.COMMON_NAME, CA_INFO["common_name"]),
    ])
    
    # 3. Costruzione del certificato con tutte le estensioni necessarie
    cert = (x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=CA_INFO["valid_days"]))
        # Estensioni critiche per una CA
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        # Identificatori chiave
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False)
        .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False)
        # Key Usage appropriata per una CA
        .add_extension(x509.KeyUsage(
            digital_signature=True,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=True,    # Può firmare certificati
            crl_sign=True,         # Può firmare CRL
            encipher_only=False,
            decipher_only=False),
            critical=True)
        .sign(ca_key, hashes.SHA256(), default_backend()))
    
    # 4. Salvataggio su file
    with open(CA_CERT_FILE, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    return ca_key, cert

def genera_certificato_firmato(ca_key, ca_cert, info: dict, cert_file: str, key_file: str, is_server: bool = False) -> tuple:
    """
    Genera un certificato firmato dalla CA.
    
    Args:
        ca_key: Chiave privata della CA per la firma
        ca_cert: Certificato della CA
        info: Dizionario con le informazioni del soggetto
        cert_file: Percorso per salvare il certificato
        key_file: Percorso per salvare la chiave privata
        is_server: Se True, aggiunge estensioni specifiche per server
    
    Returns:
        Tupla contenente (chiave_privata, certificato)
    """
    # 1. Genera la chiave privata
    private_key = genera_chiave_privata(key_file)
    
    # 2. Crea il subject
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, info["country"]),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, info["state"]),
        x509.NameAttribute(NameOID.LOCALITY_NAME, info["locality"]),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, info["organization"]),
        x509.NameAttribute(NameOID.COMMON_NAME, info["common_name"]),
    ])
    
    # 3. Costruzione del certificato
    builder = (x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(ca_cert.subject)  # Il firmatario è la CA
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=info["valid_days"]))
        # Identificatori chiave
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(private_key.public_key()), critical=False)
        .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False)
        # Key Usage appropriata per client/server
        .add_extension(x509.KeyUsage(
            digital_signature=True,
            content_commitment=False,
            key_encipherment=True,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False),
            critical=True))
    
    # 4. Aggiunta estensioni specifiche
    if is_server:
        # Subject Alternative Name per il server
        builder = builder.add_extension(
            x509.SubjectAlternativeName([x509.DNSName(info["common_name"])]),
            critical=False)
        # Extended Key Usage per autenticazione server
        builder = builder.add_extension(
            x509.ExtendedKeyUsage([x509.OID_SERVER_AUTH]),
            critical=False)
    else:
        # Extended Key Usage per autenticazione client
        builder = builder.add_extension(
            x509.ExtendedKeyUsage([x509.OID_CLIENT_AUTH]),
            critical=False)
    
    # 5. Firma il certificato con la chiave della CA
    cert = builder.sign(ca_key, hashes.SHA256(), default_backend())
    
    # 6. Salvataggio su file
    with open(cert_file, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    return private_key, cert

def genera_tutti_certificati():
    """Genera tutti i certificati necessari (CA, server e client)"""
    if os.path.exists(CA_CERT_FILE):
        print("Certificati già esistenti. Eliminarli manualmente per rigenerarli.")
        return
    
    print("Generazione di tutti i certificati...")
    
    # 1. Genera CA
    ca_key, ca_cert = genera_certificato_ca()
    
    # 2. Genera certificato server
    print("Generando certificato server...")
    genera_certificato_firmato(ca_key, ca_cert, SERVER_INFO, SERVER_CERT_FILE, SERVER_KEY_FILE, is_server=True)
    
    # 3. Genera certificato client
    print("Generando certificato client...")
    genera_certificato_firmato(ca_key, ca_cert, CLIENT_INFO, CLIENT_CERT_FILE, CLIENT_KEY_FILE)
    
    print("Tutti i certificati sono stati generati con successo!")

# =============== FUNZIONI SERVER ===============

def avvia_server(host: str):
    """
    Avvia il server SSL in ascolto sull'host specificato.
    
    Args:
        host: Indirizzo IP su cui mettersi in ascolto
    """
    # Configurazione del contesto SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.verify_mode = ssl.CERT_REQUIRED  # Richiede autenticazione client
    context.load_cert_chain(certfile=SERVER_CERT_FILE, keyfile=SERVER_KEY_FILE)
    context.load_verify_locations(cafile=CA_CERT_FILE)
    
    # Per testing, disabilita la verifica dell'hostname
    context.check_hostname = False
    
    # Crea il socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Configura il socket per riutilizzare l'indirizzo
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Binding alla porta
        sock.bind((host, PORT))
        sock.listen(BACKLOG)
        print(f"Server in ascolto su {host}:{PORT}")
        
        try:
            while True:
                # Accetta connessioni in entrata
                conn, addr = sock.accept()
                print(f"Connessione accettata da {addr}")
                
                try:
                    # Applica il layer SSL
                    with context.wrap_socket(conn, server_side=True) as ssl_conn:
                        try:
                            # Estrai informazioni dal certificato client
                            cert = ssl_conn.getpeercert()
                            if not cert:
                                print("Attenzione: Nessun certificato client ricevuto!")
                                continue
                            
                            # Estrai Common Name dal certificato
                            subject = dict(x[0] for x in cert['subject'])
                            common_name = subject.get('commonName', 'Sconosciuto')
                            print(f"Client autenticato: {common_name}")
                            
                            # Ricevi dati dal client
                            data = ssl_conn.recv(BUFFER_SIZE)
                            if not data:
                                print("Connessione chiusa dal client")
                                continue
                                
                            print(f"Ricevuto: {data.decode()}")
                            
                            # Invia risposta
                            try:
                                ssl_conn.sendall(b"Messaggio ricevuto dal server!")
                            except BrokenPipeError:
                                print("Client ha chiuso la connessione improvvisamente")
                            
                        except ssl.SSLError as e:
                            print(f"Errore SSL durante la comunicazione: {e}")
                        except Exception as e:
                            print(f"Errore durante la comunicazione: {e}")
                            
                except ssl.SSLError as e:
                    print(f"Errore SSL durante l'handshake: {e}")
                except Exception as e:
                    print(f"Errore durante l'accettazione della connessione: {e}")
                finally:
                    # Chiudi la connessione
                    try:
                        conn.close()
                    except:
                        pass
                        
        except KeyboardInterrupt:
            print("\nServer arrestato manualmente.")
        finally:
            sock.close()

# =============== FUNZIONI CLIENT ===============

def avvia_client(server_host: str):
    """
    Avvia il client SSL che si connette al server specificato.
    
    Args:
        server_host: Indirizzo IP o hostname del server
    """
    # Configurazione del contesto SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.verify_mode = ssl.CERT_REQUIRED  # Verifica il certificato server
    context.load_verify_locations(cafile=CA_CERT_FILE)
    context.load_cert_chain(certfile=CLIENT_CERT_FILE, keyfile=CLIENT_KEY_FILE)
    
    # Per testing, disabilita la verifica dell'hostname
    context.check_hostname = False
    
    try:
        # Crea una connessione TCP al server
        with socket.create_connection((server_host, PORT)) as sock:
            print(f"Connesso a {server_host}:{PORT}")
            
            try:
                # Applica il layer SSL
                with context.wrap_socket(sock, server_hostname=SERVER_INFO["common_name"]) as ssl_conn:
                    try:
                        # Estrai informazioni dal certificato server
                        cert = ssl_conn.getpeercert()
                        if not cert:
                            print("Attenzione: Nessun certificato server ricevuto!")
                            return
                        
                        # Estrai Common Name dal certificato
                        subject = dict(x[0] for x in cert['subject'])
                        common_name = subject.get('commonName', 'Sconosciuto')
                        print(f"Connesso al server: {common_name}")
                        
                        # Invia un messaggio al server
                        message = b"Ciao dal client!"
                        ssl_conn.sendall(message)
                        print(f"Inviato: {message.decode()}")
                        
                        # Ricevi la risposta
                        data = ssl_conn.recv(BUFFER_SIZE)
                        if not data:
                            print("Server ha chiuso la connessione")
                            return
                            
                        print(f"Risposta: {data.decode()}")
                        
                    except ssl.SSLError as e:
                        print(f"Errore SSL durante la comunicazione: {e}")
                    except BrokenPipeError:
                        print("Server ha chiuso la connessione improvvisamente")
                    except Exception as e:
                        print(f"Errore durante la comunicazione: {e}")
                        
            except ssl.SSLError as e:
                print(f"Errore SSL durante l'handshake: {e}")
            except Exception as e:
                print(f"Errore durante la connessione SSL: {e}")
                
    except ConnectionRefusedError:
        print(f"Connessione rifiutata. Verifica che il server sia attivo su {server_host}:{PORT}")
    except Exception as e:
        print(f"Errore durante la connessione: {e}")

# =============== MAIN ===============

def main():
    """Funzione principale che gestisce i comandi da riga di comando."""
    if len(sys.argv) < 2:
        print("Utilizzo:")
        print("  Genera certificati: python3 script.py gen_certs")
        print("  Avvia server: python3 script.py server <indirizzo>")
        print("  Avvia client: python3 script.py client <indirizzo_server>")
        sys.exit(1)
    
    comando = sys.argv[1]
    
    if comando == "gen_certs":
        genera_tutti_certificati()
    elif comando == "server":
        host = sys.argv[2] if len(sys.argv) > 2 else '0.0.0.0'
        avvia_server(host)
    elif comando == "client":
        if len(sys.argv) < 3:
            print("Specificare l'indirizzo del server")
            sys.exit(1)
        avvia_client(sys.argv[2])
    else:
        print("Comando non valido")

if __name__ == "__main__":
    main()
