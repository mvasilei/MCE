# MCE
Jinja based project templating migration configuration

Login on Lab bastion

python3 -m venv ./mce/env

source bin/activate

pip3.6 install --upgrade Jinja2

download the base_config.py file and the file that's attached on the config quide in bastion under ~/mce/venv

chmod 775 base_config.py
===
run the scrpt e.g.

./base_config.py -b device_details.txt -v vlan.txt -o
===
create a file on your local directory with the following format

"MCE": "UKX...",
"LOCATION": "MTX RACK details",
"SNMP_SHA": "SHA KEY",
"SNMP_AES": "AES KEY",
"TACACS_PASSWORD": "PASSWORD",
"LOCAL_PASSWORD": "PASSWORD",
"LOOPBACK": "IP OF DEVICE LO I/F",
"MPE_HSRP_IP": "VLAN 600 VIP",
"VLAN600_IP": "VLAN 600 LOCAL IP",
"SUBNETMASK_LENGTH": "BIT NUMBERS"


e.g

"MCE": "Sandrine",
"LOCATION": "Gergeley",
"SNMP_SHA": "Frieda",
"SNMP_AES": "Fritz",
"TACACS_PASSWORD": "tacacs99",
"LOCAL_PASSWORD": "Sirius",
"LOOPBACK": "10.10.10.10",
"MPE_HSRP_IP": "60.60.60.1",
"VLAN600_IP": "60.60.60.15",
"SUBNETMASK_LENGTH": "24"
