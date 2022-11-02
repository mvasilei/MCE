#! /usr/bin/env python3.6
from jinja2 import Environment, FileSystemLoader
import signal, sys

def signal_handler(sig, frame):
     print('Exiting gracefully Ctrl-C detected...')
     sys.exit()

def main():
    #This line uses the current directory
    file_loader = FileSystemLoader('.')
    # Load the enviroment
    env = Environment(loader=file_loader)
    template = env.get_template('base_config.txt')

    device = {"MCE": "Sandrine",
         "LOCATION": "Gergeley",
         "SNMP_SHA": "Frieda",
         "SNMP_AES": "Fritz",
         "TACACS_PASSWORD": "tacacs99",
         "LOCAL_PASSWORD": "Sirius",
         "LOOPBACK": "10.10.10.10",
         "MPE_HSRP_IP": "60.60.60.1",
         "VLAN600_IP": "60.60.60.15",
         "SUBNETMASK_LENGTH": "24"}

    output = template.render(
         MCE = device["MCE"],
         LOCATION =  device["LOCATION"],
         SNMP_SHA =  device["SNMP_SHA"],
         SNMP_AES = device["SNMP_AES"],
         TACACS_PASSWORD = device["TACACS_PASSWORD"],
         LOCAL_PASSWORD = device["LOCAL_PASSWORD"],
         LOOPBACK = device["LOOPBACK"],
         MPE_HSRP_IP = device["MPE_HSRP_IP"],
         VLAN600_IP = device["VLAN600_IP"],
         SUBNETMASK_LENGTH = device["SUBNETMASK_LENGTH"])

    print(output)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  #catch ctrl-c and call handler to terminate the script
    main()
