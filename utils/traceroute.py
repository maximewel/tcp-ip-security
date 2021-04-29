"""
Authors : Fridez Lucas, Maxime Welcklen
Traceroute with Scapy
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
import matplotlib.pyplot as plt


# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    ans, unans = traceroute('fridez.dev')
