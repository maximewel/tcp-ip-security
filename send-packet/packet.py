"""
Authors : Fridez Lucas, Maxime Welcklen
Send a packet with interval
"""

# Imports
from scapy.all import *
from scapy.layers.inet import *
from time import sleep
import argparse


def main(dst, port):
    """Send packets with regular interval

    Args:
        dst (str): Destination address
        port (int): Destination port
    """
    DST = dst
    D_PORT = port
    SLEEP_S = 1
    NBR_MSG = 100

    # Send packets
    for i in range(1, NBR_MSG + 1):
        packet = IP(dst=DST)/TCP(dport=D_PORT)/f"Hi, it is message number {i}"
        sleep(SLEEP_S)
        send(packet)
        print(f"--> Message number {i} sent !")


def __configure_argparse__():
    """Configure argparser

    Returns:
        parser: Arguments parser
    """
    parser = argparse.ArgumentParser(description='Foo')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument(
        '-d', '--dst', help='Destination address', required=True)
    requiredNamed.add_argument(
        '-p', '--port', help='Destination port', required=True, type=int)

    return parser


# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()

    main(args.dst, args.port)
