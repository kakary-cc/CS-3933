iptables -A FORWARD -p tcp -d 192.168.60.5 --dport 23 -j ACCEPT
iptables -A FORWARD -p tcp -s 192.168.60.5 --sport 23 -j ACCEPT
iptables -P FORWARD DROP