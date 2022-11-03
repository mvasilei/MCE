#! /usr/bin/env python3.6
from jinja2 import Environment, FileSystemLoader
from optparse import OptionParser
import signal, sys, json


def signal_handler(sig, frame):
     print('Exiting gracefully Ctrl-C detected...')
     sys.exit()

def main():
    usage = 'usage: %prog options [arg]'
    parser = OptionParser(usage)
    parser.add_option('-b', '--base', dest='base_config',
                      help='Read base config data from FILENAME')
    parser.add_option('-v', '--vlan', dest='vlan',
                      help='Read vlan data from FILENAME')
    parser.add_option('-o', '--odd', action='store_true', dest='odd',
                      help='Odd numbered MCE')

    (options, args) = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    with open(options.base_config, 'r') as f:
        data = "{" + f.read() + "}"

    device = json.loads(data)

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True

    template = env.get_template('base_config.txt')
    output = template.render(
         MCE = device["MCE"],
         NMCE=device["NMCE"], #neighbour MCE
         LOCATION = device["LOCATION"],
         SNMP_SHA = device["SNMP_SHA"],
         SNMP_AES = device["SNMP_AES"],
         TACACS_PASSWORD = device["TACACS_PASSWORD"],
         LOCAL_PASSWORD = device["LOCAL_PASSWORD"],
         LOOPBACK = device["LOOPBACK"],
         MPE_HSRP_IP = device["MPE_HSRP_IP"],
         VLAN600_IP = device["VLAN600_IP"],
         SUBNETMASK_LENGTH = device["SUBNETMASK_LENGTH"],
         MPE = device["MPE"],
         MPE_IF = device["MPE_IF"])

    print(output)

    vlan_list = []
    with open(options.vlan, 'r') as f:
        for line in f:
            vlan_list.append(json.loads(line.strip('\n')))

    if (options.odd):
        template = env.get_template('vlan_config_odd.txt')
    else:
        template = env.get_template('vlan_config_even.txt')
    output = template.render(vlan_list = vlan_list)

    print(output)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  #catch ctrl-c and call handler to terminate the script
    main()
