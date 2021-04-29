"""
Authors : Fridez Lucas, Maxime Welcklen
Show a TCP Packet
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *


def ask_dst():
    """Ask destination address

    Returns:
        string: destination address to contact
    """
    dst_address = input("Please enter your destination address : ")
    print("\n")
    return dst_address


def main():
    """Main method
    """
    dst = "fridez.dev" #ask_dst()
    p = Ether()/IP(dst=dst)/TCP(flags="F")
    print("------------ Paquet information ------------\n")
    print(p[IP].show())

    print("\n------------ Hex Representation ------------\n")
    hexdump(p)

    print("\n---------------- Paquet Data ----------------\n")
    print(p.payload)

# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    main()
