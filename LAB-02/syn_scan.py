from scapy.all import IP, ICMP, TCP, sr1, sr, conf
import sys
from datetime import datetime

# Disabilita l'output verboso di Scapy
conf.verb = 0

def print_banner():
    """
    Stampa il banner iniziale del programma
    """
    print("\n" + "="*60)
    print("     SYN SCANNER - AUTO DISCOVERY (1-65535)")
    print("="*60)

def icmp_probe(ip):
    """
    Verifica se un host è raggiungibile tramite un ping ICMP.
    
    Args:
        ip (str): L'indirizzo IP dell'host da verificare
    
    Returns:
        bool: True se l'host risponde, False altrimenti
    """
    print(f"\n[*] ICMP probe su {ip}...")
    
    # Crea e invia un pacchetto ICMP Echo Request
    icmp_packet = IP(dst=ip)/ICMP()
    resp_packet = sr1(icmp_packet, timeout=2, verbose=0)
    
    if resp_packet is not None:
        print(f"[+] Host {ip} raggiungibile\n")
        return True
    else:
        print(f"[-] Host {ip} non risponde al ping ICMP")
        print(f"[*] Continuo comunque la scansione...\n")
        return False

def syn_scan(ip, port):
    """
    Esegue una scansione SYN su una singola porta.
    
    Args:
        ip (str): L'indirizzo IP target
        port (int): La porta da scansionare
    
    Returns:
        str: "open", "closed" o "filtered"
    """
    # Crea un pacchetto TCP SYN
    syn_packet = IP(dst=ip)/TCP(dport=port, flags='S')
    
    # Invia il pacchetto e attendi risposta (timeout 1 secondo)
    resp_packet = sr1(syn_packet, timeout=1, verbose=0)
    
    # Analizza la risposta
    if resp_packet is None:
        # Nessuna risposta = porta filtrata
        return "filtered"
    
    elif resp_packet.haslayer(TCP):
        # Estrai i flag TCP dalla risposta
        tcp_flags = resp_packet[TCP].flags
        
        # Flag 0x12 = SYN-ACK (porta aperta)
        if tcp_flags == 0x12:
            # Invia RST per chiudere la connessione
            rst_packet = IP(dst=ip)/TCP(dport=port, flags='R')
            sr1(rst_packet, timeout=1, verbose=0)
            return "open"
        
        # Flag 0x14 = RST-ACK (porta chiusa)
        elif tcp_flags & 0x04:  # Controlla se RST è impostato
            return "closed"
    
    # Altri casi = porta filtrata
    return "filtered"

def quick_scan(ip, start_port=1, end_port=1024, batch_size=100):
    """
    Scansiona rapidamente un range di porte per trovare quelle aperte.
    Usa batch per velocizzare (invia più pacchetti insieme).
    
    Args:
        ip (str): IP target
        start_port (int): Prima porta del range
        end_port (int): Ultima porta del range
        batch_size (int): Numero di porte da scansionare per batch
    
    Returns:
        list: Lista delle porte aperte
    """
    open_ports = []
    total_ports = end_port - start_port + 1
    scanned = 0
    
    print(f"[*] Scansione veloce porte {start_port}-{end_port}...")
    print(f"[*] Totale porte: {total_ports}")
    print(f"[*] Questo potrebbe richiedere alcuni minuti...\n")
    
    # Scansiona a batch per velocizzare
    for batch_start in range(start_port, end_port + 1, batch_size):
        batch_end = min(batch_start + batch_size - 1, end_port)
        
        # Crea pacchetti SYN per tutte le porte del batch
        packets = [
            IP(dst=ip)/TCP(dport=port, flags='S') 
            for port in range(batch_start, batch_end + 1)
        ]
        
        # Invia tutti i pacchetti e ricevi risposte
        # inter=0.001 = 1ms tra un pacchetto e l'altro (evita sovraccarico)
        answered, unanswered = sr(packets, timeout=2, verbose=0, inter=0.001)
        
        # Analizza le risposte
        for sent, received in answered:
            if received.haslayer(TCP):
                # Se riceve SYN-ACK, la porta è aperta
                if received[TCP].flags == 0x12:  # SYN-ACK
                    port = received[TCP].sport
                    open_ports.append(port)
                    print(f"[+] Porta {port:5d} APERTA")
                    
                    # Invia RST per chiudere la connessione
                    rst = IP(dst=ip)/TCP(dport=port, flags='R')
                    sr1(rst, timeout=1, verbose=0)
        
        # Aggiorna progresso
        scanned += (batch_end - batch_start + 1)
        percentage = (scanned / total_ports) * 100
        print(f"[*] Progresso: {scanned}/{total_ports} ({percentage:.1f}%)", end='\r')
    
    print("\n")  # Nuova riga dopo il progresso
    return sorted(open_ports)

def full_scan(ip, ports):
    """
    Esegue una scansione dettagliata sulle porte specificate.
    
    Args:
        ip (str): IP target
        ports (list): Lista di porte da scansionare in dettaglio
    """
    print("\n" + "="*60)
    print("     SCANSIONE DETTAGLIATA PORTE APERTE")
    print("="*60 + "\n")
    
    results = {"open": [], "closed": [], "filtered": []}
    
    for port in ports:
        print(f"[*] Analisi dettagliata porta {port}...", end='')
        status = syn_scan(ip, port)
        results[status].append(port)
        
        # Codifica colori ANSI
        if status == "open":
            print(f" [\033[92mAPERTA\033[0m]")
        elif status == "closed":
            print(f" [\033[91mCHIUSA\033[0m]")
        else:
            print(f" [\033[93mFILTRATA\033[0m]")
    
    return results

def print_summary(results, start_time):
    """
    Stampa il riepilogo finale della scansione.
    
    Args:
        results (dict): Dizionario con i risultati della scansione
        start_time (datetime): Timestamp di inizio scansione
    """
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "="*60)
    print("     RIEPILOGO SCANSIONE")
    print("="*60 + "\n")
    
    # Porte aperte
    if results["open"]:
        print(f"[+] Porte APERTE ({len(results['open'])}):")
        for port in results["open"]:
            print(f"    - Porta {port}")
    else:
        print("[-] Nessuna porta aperta trovata")
    
    print()
    
    # Porte chiuse
    if results["closed"]:
        print(f"[-] Porte CHIUSE ({len(results['closed'])}):")
        for port in results["closed"]:
            print(f"    - Porta {port}")
    
    print()
    
    # Porte filtrate
    if results["filtered"]:
        print(f"[?] Porte FILTRATE ({len(results['filtered'])}):")
        for port in results["filtered"]:
            print(f"    - Porta {port}")
    
    print("\n" + "="*60)
    print(f"[*] Tempo totale: {duration:.2f} secondi")
    print("="*60 + "\n")

def main():
    """
    Funzione principale del programma
    """
    # Controlla argomenti
    if len(sys.argv) < 2:
        print("\n[!] Uso corretto:")
        print("    sudo python3 syn_scanner_auto.py <IP> [opzioni]\n")
        print("Opzioni:")
        print("    --quick       Scansiona solo porte 1-1024 (veloce)")
        print("    --common      Scansiona solo le 100 porte più comuni")
        print("    --full        Scansiona tutte le 65535 porte (lento)\n")
        print("Esempi:")
        print("    sudo python3 syn_scanner_auto.py 192.168.1.1 --quick")
        print("    sudo python3 syn_scanner_auto.py 192.168.1.1 --full")
        print("    sudo python3 syn_scanner_auto.py 192.168.1.1  (default: --quick)\n")
        sys.exit(1)
    
    # Estrai IP e opzioni
    ip = sys.argv[1]
    
    # Determina range di porte
    if "--full" in sys.argv:
        start_port = 1
        end_port = 65535
        scan_type = "COMPLETA (1-65535)"
    elif "--common" in sys.argv:
        # Lista delle 100 porte più comuni
        common_ports = [
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 
            995, 1723, 3306, 3389, 5900, 8080, 20, 69, 161, 162, 389, 636, 
            1433, 1521, 2049, 3268, 5432, 5800, 8443, 1080, 1194, 8888, 27017,
            137, 138, 500, 1701, 4500, 465, 587, 514, 515, 631, 873, 2181,
            2375, 2376, 3000, 5000, 5001, 5432, 5984, 6379, 7001, 8000, 8008,
            8081, 8443, 8888, 9000, 9090, 9200, 9300, 10000, 27017, 28017,
            50000, 50070, 123, 161, 162, 179, 389, 443, 636, 989, 990, 1433,
            1434, 1521, 1830, 2082, 2083, 2086, 2087, 2095, 2096, 3128, 8009,
            9999, 19132, 19133, 25565, 25575
        ][:100]  # Prendi solo le prime 100
        print(f"[*] Modalità: scansione porte comuni")
        start_time = datetime.now()
        print_banner()
        print(f"Target: {ip}")
        print(f"Tipo scansione: PORTE COMUNI (top 100)\n")
        
        # Ping check
        icmp_probe(ip)
        
        # Scansiona solo le porte comuni
        open_ports = []
        for port in common_ports:
            status = syn_scan(ip, port)
            if status == "open":
                open_ports.append(port)
                print(f"[+] Porta {port:5d} APERTA")
        
        if open_ports:
            results = full_scan(ip, open_ports)
            print_summary(results, start_time)
        else:
            print("[-] Nessuna porta comune aperta trovata")
        
        return
    else:  # Default: --quick
        start_port = 1
        end_port = 1024
        scan_type = "VELOCE (1-1024)"
    
    # Stampa informazioni iniziali
    start_time = datetime.now()
    print_banner()
    print(f"Target: {ip}")
    print(f"Tipo scansione: {scan_type}")
    print(f"Ora inizio: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Step 1: Verifica che l'host sia raggiungibile
    icmp_probe(ip)
    
    # Step 2: Quick scan per trovare porte aperte
    open_ports = quick_scan(ip, start_port, end_port)
    
    # Step 3: Se trova porte aperte, fai scan dettagliato
    if open_ports:
        print(f"\n[+] Trovate {len(open_ports)} porte aperte")
        print(f"[*] Avvio scansione dettagliata...\n")
        
        results = full_scan(ip, open_ports)
        print_summary(results, start_time)
    else:
        print(f"[-] Nessuna porta aperta trovata nel range {start_port}-{end_port}")
        print(f"[*] Tempo totale: {(datetime.now() - start_time).total_seconds():.2f} secondi\n")

# Entry point del programma
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Scansione interrotta dall'utente")
        sys.exit(0)
    except PermissionError:
        print("\n[!] Errore: privilegi insufficienti")
        print("[!] Esegui il programma con privilegi di root/amministratore")
        print("[!] Linux/Mac: sudo python3 syn_scanner_auto.py <IP>")
        print("[!] Windows: esegui come Amministratore\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Errore imprevisto: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
