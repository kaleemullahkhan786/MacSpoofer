import subprocess
import logging
import sys
import time
import os
import platform
from colorama import Fore, Style

logs = logging.basicConfig(level=logging.DEBUG, filemode='a', filename='mac_spoof.log', format='[%(asctime)s] - %(levelname)s %(message)s')

version = 1.1

def checkroot():
    if not 'SUDO_UID' in os.environ.keys():
        sys.exit(f'{Fore.RED}Run the script with root{Style.RESET_ALL}')

def interface_check(interface):
    try:
        if interface in os.listdir('/sys/class/net'):
            return interface
        else:
            logging.error(f'This interface:{interface} is Invalid')
            sys.exit(f'\nInvalid Interface: {interface}')

    except Exception as e:
        exit(logging.error(e))

def os_check(support=['Linux', 'Unix']):
    if platform.system() not in support:
        logging.error('Unsupported OS detected')
        exit('This program runs on Linux only')

def check_existing_connection(ssid):
    result = subprocess.run(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], stdout=subprocess.PIPE)
    connections = result.stdout.decode().splitlines()
    return ssid in connections

def configure_wifi(interface, ssid, password):
    if not check_existing_connection(ssid):
        logging.info(f'Configuring WiFi network {ssid}')
        print(f'[Console] ===> Configuring WiFi network {ssid}')
        
        subprocess.run(['nmcli', 'connection', 'add', 'type', 'wifi', 'ifname', interface, 'con-name', ssid, 'ssid', ssid])
        subprocess.run(['nmcli', 'connection', 'modify', ssid, 'wifi-sec.key-mgmt', 'wpa-psk'])
        subprocess.run(['nmcli', 'connection', 'modify', ssid, 'wifi-sec.psk', password])

        logging.info(f'WiFi network {ssid} configured successfully.')
        print(f'[Console] ===> WiFi network {ssid} configured successfully.')
    else:
        logging.info(f'WiFi network {ssid} already exists. Skipping configuration.')
        print(f'[Console] ===> WiFi network {ssid} already exists. Skipping configuration.')

    result = subprocess.run(['nmcli', 'connection', 'up', ssid], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    if result.returncode == 0:
        logging.info(f'Connected to {ssid}')
        print(f'[Console] ===> Successfully connected to {ssid}')
    else:
        logging.error(f'Failed to connect to {ssid}: {result.stderr.decode()}')
        print(f'[Console] ===> Failed to connect to {ssid}')

def mac(interface, bssid):
    try:
        logging.info(f'Disabling the WPA service on {interface}')
        print('[Console] ===> Disabling WPA service')
        subprocess.run(['systemctl', 'stop', 'wpa_supplicant.service'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)

        logging.info(f'Killing the Network and Libs for WPA service')
        print('[Console] ===> Killing the Network and Libs for WPA service')
        subprocess.run(['airmon-ng', 'check', 'kill'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)

        logging.info(f'Starting the Network and Libs for WPA service')
        print('[Console] ===> Starting the Network and Libs for WPA service')
        subprocess.run(['systemctl', 'start', 'wpa_supplicant.service'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)

        logging.warning(f'Bringing the Interface Down')
        print('[Console] ===> Bringing the Interface Down')
        os.system(f'ip link set {interface} down')
        time.sleep(2)

        logging.info(f'Changing the MAC Address on Interface {interface} to {bssid}')
        print(f'[Console] ===> Changing the MAC Address on Interface {interface} to {bssid}')
        subprocess.run(['macchanger', interface, '-b', '-m', bssid], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)

        print(f'[Console] ===> Enabling the interface: {interface} up')
        logging.info(f'Enabling the interface: {interface} up')
        os.system(f'ip link set {interface} up')

        print('[Console] ===> Starting a Network Manager Service')
        logging.info('Starting a Network Manager Service')
        subprocess.run(['systemctl', 'start', 'NetworkManager.service'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(3)

        print('[Console] ===> Done')
    except OSError as e:
        logging.error(e)

def print_banner():
    banner = r"""
{0}888b     d888                   .d8888b.                              .d888                 
8888b   d8888                  d88P  Y88b                            d88P                  
88888b.d88888                  Y88b.                                 888                    
888Y88888P888  8888b.   .d8888b "Y888b.   88888b.   .d88b.   .d88b.  888888 .d88b.  888d888 
888 Y888P 888     "88b d88P"       "Y88b. 888 "88b d88""88b d88""88b 888   d8P  Y8b 888P"   
888  Y8P  888 .d888888 888           "888 888  888 888  888 888  888 888   88888888 888     
888   "   888 888  888 Y88b.   Y88b  d88P 888 d88P Y88..88P Y88..88P 888   Y8b.     888     
888       888 "Y888888  "Y8888P "Y8888P"  88888P"   "Y88P"   "Y88P"  888    "Y8888  888     
                                          888                                               
                                          888                                               
                                          888                                              
                                                                 {1}

Coder: Kaleemullah Khan
MacSpoofer Version: 1.1
""".format(Fore.CYAN, Style.RESET_ALL)
    print(banner)

if __name__ == "__main__":
    print_banner()
    print('Program Started .....')
    time.sleep(3)
    checkroot()
    os_check()
    
    interface = input(f'{Fore.GREEN}Enter the network interface: {Style.RESET_ALL}')
    interface_check(interface)
    
    target_mac = input(f'{Fore.GREEN}Enter the target MAC address: {Style.RESET_ALL}')
    wifi_ssid = input(f'{Fore.GREEN}Enter the WiFi SSID (network name): {Style.RESET_ALL}')
    wifi_password = input(f'{Fore.GREEN}Enter the WiFi password: {Style.RESET_ALL}')
    
    mac(interface=interface, bssid=target_mac)
    
    configure_wifi(interface=interface, ssid=wifi_ssid, password=wifi_password)
    
    print('[Console] ===> All operations completed successfully.')

