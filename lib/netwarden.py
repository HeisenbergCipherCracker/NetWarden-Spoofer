import thirdparty.scapy as scapy
import subprocess
import sys
import time
import os
from ipaddress import IPv4Network
import threading

cwd = os.getcwd()

def arp_scan(ip_range):
    arp_responses = []
    answered_lst = scapy.arping(ip_range, verbose=0)[0]
    for _result in answered_lst:
        arp_responses.append(_result)

    return arp_responses

def is_gateway()
