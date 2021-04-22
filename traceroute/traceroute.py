# TCP IP Security
# Try traceroute in Python
# HE-Arc - Security
# 2021, Welcklen & Fridez

from scapy.all import *
from scapy.layers.inet import *
import matplotlib.pyplot as plt

ans, unans = traceroute('fridez.dev')