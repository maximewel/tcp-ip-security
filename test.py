from scapy.all import *
from scapy.layers.inet import *

[print(f"{p.summary()} with ttl {p.ttl}") for p in IP(ttl=(1,5))/ICMP()]