# Cyber-Sentry: Network Packet Sniffer
# Created by: Shweta (B.Tech CSE)

from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    # 1. Check karein ki packet mein IP Layer hai ya nahi
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src = ip_layer.src  # Kahan se aa raha hai
        dst = ip_layer.dst  # Kahan ja raha hai
        proto = ip_layer.proto # Kaunsa protocol hai (TCP=6, UDP=17)

        print(f"\n[+] New Packet Captured:")
        print(f"    Source IP: {src} ---> Destination IP: {dst}")

        # 2. Check karein ki TCP hai ya UDP (Deep Inspection)
        if packet.haslayer(TCP):
            print(f"    Protocol: TCP | Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    Protocol: UDP | Port: {packet[UDP].dport}")

def start_sniffing():
    print("="*50)
    print("      CYBER-SENTRY: NETWORK ANALYZER STARTING...      ")
    print("    (Monitoring live network traffic for analysis)    ")
    print("="*50)
    
    # 3. Network traffic ko pakadna shuru karein (count=20 matlab 20 packets)
    # count hatane par ye chalta hi rahega jab tak aap Stop na karein
    sniff(prn=process_packet, count=100)

if __name__ == "__main__":
    start_sniffing()