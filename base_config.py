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
    parser.add_option('-s', '--stack', action='store_true', dest='stack',
                      help='Indicate Virtual Chassis (stack)')

    (options, args) = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    with open(options.base_config, 'r') as f:
        data = "{" + f.read() + "}"

    device = json.loads(data)
    print(device)

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True

    template = env.get_template('base_config.txt')
    if (options.stack):
        template = env.get_template('base_config_stack.txt')

    output = template.render(device=device)

    print(output)

    vlan_list = []
    with open(options.vlan, 'r') as f:
        for line in f:
            vlan_list.append(json.loads(line.strip('\n')))

    template = env.get_template('vlan_config_even.txt')
    if (options.odd):
        template = env.get_template('vlan_config_odd.txt')

    output = template.render(vlan_list=vlan_list)

    print(output)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  #catch ctrl-c and call handler to terminate the script
    main()
