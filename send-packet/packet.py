# TCP IP Security
# Send packet with interval
# HE-Arc - Security
# 2021, Welcklen & Fridez

from scapy.all import *
from scapy.layers.inet import *
from time import sleep
import argparse


def main(dst, port):
    DST = dst
    D_PORT = port
    SLEEP_S = 1
    NBR_MSG = 100

    for i in range(1, NBR_MSG + 1):
        packet = IP(dst=DST)/TCP(dport=D_PORT)/f"Hi, it is message number {i}"
        sleep(SLEEP_S)
        send(packet)
        print(f"--> Message number {i} sent !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Foo')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-d', '--dst', help='Destination address', required=True)
    requiredNamed.add_argument('-p', '--port', help='Destination port', required=True, type=int)
    args = parser.parse_args()

    main(args.dst, args.port)
