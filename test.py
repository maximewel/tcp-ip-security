from scapy.all import *
from scapy.layers.inet import *

# [print(f"{p.summary()} with ttl {p.ttl}") for p in IP(ttl=(1,5))/ICMP()]


ans, unans = srloop(IP(dst="betweenfriends.forumactif.com")/TCP(dport=80,flags="S"))

temp = 0
for s, r in ans:
   temp = r[TCP].seq - temp
   print("%d\t+%d" % (r[TCP].seq, temp))