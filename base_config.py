#! /usr/bin/env python3.6
from jinja2 import Environment, FileSystemLoader
from optparse import OptionParser
import signal, sys, json


def signal_handler(sig, frame):
     print('Exiting gracefully Ctrl-C detected...')
     sys.exit()

def main():
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('base_config.txt')

    usage = 'usage: %prog options [arg]'
    parser = OptionParser(usage)
    parser.add_option('-f', '--file', dest='filename',
                      help='Read data from FILENAME')

    (options, args) = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    with open(options.filename, 'r') as f:
        data = f.read()

    device = json.loads(data)

    output = template.render(
         MCE = device["MCE"],
         LOCATION = device["LOCATION"],
         SNMP_SHA = device["SNMP_SHA"],
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
