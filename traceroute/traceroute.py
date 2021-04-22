from scapy.all import *
from scapy.layers.inet import *
import matplotlib.pyplot as plt

ans, unans = traceroute('fridez.dev')