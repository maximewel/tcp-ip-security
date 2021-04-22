# TCP IP Security
# Show a TCP Paquet
# HE-Arc - Security
# 2021, Welcklen & Fridez

from scapy.all import *
from scapy.layers.inet import *

BLUE = '\033[94M'
GREEN = '\033[32m'
RED = '\033[91m'
WHITE = '\033[0m'

def sniff_packet(packet):
    if packet.haslayer(IP):
        pckt_src=packet[IP].src
        pckt_dst = packet[IP].dst
        pckt_ttl = packet[IP].ttl
        print(RED +"IP packet: " + GREEN + str(pckt_src) + RED + " is going to " + GREEN + str(pckt_dst)+ RED + " and has ttl value " + GREEN + str(pckt_ttl))

def main():
    print("Custom Packets sniffer")
    sniff(filter="ip", prn=sniff_packet, iface="wlp59s0")

if __name__ == "__main__":
    main()