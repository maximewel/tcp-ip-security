# TCP IP Security
# Show a TCP Paquet
# HE-Arc - Security
# 2021, Welcklen & Fridez

from scapy.all import *
from scapy.layers.inet import *


def ask_dst():
    dst_address = input("Please enter your destination address : ")
    print("\n")
    return dst_address


def main():
    dst = "fridez.dev" #ask_dst()
    p = Ether()/IP(dst=dst)/TCP(flags="F")
    print("------------ Paquet information ------------\n")
    print(p[IP].show())

    print("\n------------ Hex Representation ------------\n")
    hexdump(p)

    print("\n---------------- Paquet Data ----------------\n")
    print(p.payload)

if __name__ == "__main__":
    main()
