from scapy.all import *

A = "1.2.3.4" # spoofed source IP address
B = "127.0.0.1" # destination IP address
C = RandShort() # source port
D = 9999 # destination port
payload = "Hello from client" # packet payload

conf.L3socket=L3RawSocket

#while True:
spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet)
