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
    parser.add_option('-s', '--stack', action='store_true', dest='stack',
                      help='Indicate Virtual Chassis (stack)')
    parser.add_option('-p', '--port', dest='port',
                      help='Read port allocations from FILENAME')

    (options, args) = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    if options.base_config and options.vlan:
        with open(options.base_config, 'r') as f:
            data = "{" + f.read() + "}"

        device = json.loads(data)

        file_loader = FileSystemLoader('.')
        env = Environment(loader=file_loader)
        env.trim_blocks = True
        env.lstrip_blocks = True
        env.rstrip_blocks = True

        template = env.get_template('base_config.txt')

        if options.stack:
            template = env.get_template('base_config_stack.txt')

        output = template.render(device=device)
        print(output)

        vlan_list = []
        with open(options.vlan, 'r') as f:
            for line in f:
                vlan_list.append(json.loads(line.strip('\n')))

            if '03' in device['MCE'] or '04' in device['MCE']:
                template = env.get_template('subtend.txt')
            elif '02' in device['MCE']:
                template = env.get_template('vlan_config_even.txt')
            else:
                template = env.get_template('vlan_config_odd.txt')

            output = template.render(vlan_list=vlan_list, stack=options.stack)
            print(output)

    elif options.port and not options.vlan and not options.base_config and not options.stack:
        port_list = []
        with open(options.port, 'r') as f:
            for line in f:
                port_list.append(json.loads(line.strip('\n')))

            file_loader = FileSystemLoader('.')
            env = Environment(loader=file_loader)
            env.trim_blocks = True
            env.lstrip_blocks = True
            env.rstrip_blocks = True

            template = env.get_template('port_config.txt')
            output = template.render(port_list=port_list)
            print(output)
    else:
        print('\nERROR: Base config (-b) must be combined with vlan (-v)')
        parser.print_help()
        exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  #catch ctrl-c and call handler to terminate the script
    main()
