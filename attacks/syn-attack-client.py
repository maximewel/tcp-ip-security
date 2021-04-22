from scapy.all import *
from scapy.layers.inet import *

# [print(f"{p.summary()} with ttl {p.ttl}") for p in IP(ttl=(1,5))/ICMP()]


ans, unans = srloop(IP(dst="192.168.1.103")/TCP(dport=9999,flags="S"))

temp = 0
for s, r in ans:
   temp = r[TCP].seq - temp
   print("%d\t+%d" % (r[TCP].seq, temp))