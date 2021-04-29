"""
Authors : Fridez Lucas, Maxime Welcklen
Sniffer
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
import argparse

# Constants for colors
BLUE = '\033[94M'
GREEN = '\033[32m'
RED = '\033[91m'
WHITE = '\033[0m'


def sniff_packet(packet):
    """Sniff packet

    Args:
        packet (packet): Packet that is sniffed
    """
    if packet.haslayer(IP):
        pckt_src = packet[IP].src
        pckt_dst = packet[IP].dst
        pckt_ttl = packet[IP].ttl
        print(RED + "IP packet: " + GREEN + str(pckt_src) + RED + " is going to " +
              GREEN + str(pckt_dst) + RED + " and has ttl value " + GREEN + str(pckt_ttl))


def main(args):
    """Main method to sniff

    Args:
        args (array): Arguments
    """

    filter_prepared = filter_from_args(args)
    print(f"Custom Packets sniffer with filter : {filter_prepared}")
    sniff(filter=filter_prepared, prn=sniff_packet, iface=args.iface)


def filter_from_args(args):
    """Apply filter from args

    Args:
        args (array): arguments

    Returns:
        str: filter
    """
    filterArray = []
    if args.mode is not None:
        filterArray += [str(args.mode)]

    if args.ip is not None:
        filterArray += [f"dst {args.ip} or host {args.ip}"]

    if args.port is not None:
        filterArray += [f"dst port {args.port}"]

    return " and ".join(filterArray)


def __configure_argparse__():
    """Configure argparser

    Returns:
       parser: Arguments parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", help="IP to sniff")
    parser.add_argument("-port", help="port to sniff")
    parser.add_argument("-mode", help="protocol to sniff (ex ip, tcp, etc)")
    parser.add_argument("-iface", help="Interface from which to capture")

    return parser


# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args)
