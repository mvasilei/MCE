# Jinja based project templating migration configuration

Login on Lab bastion

python3.6 -m venv ./mce/env

source bin/activate

pip install --upgrade pip

pip install Jinja2

download the base_config.py file and the file that's attached on the config quide in bastion under ~/mce/venv

chmod 775 base_config.py
===
run the script e.g.

./base_config.py -b device_details.txt -v vlan.txt -s
===
create a file on your local directory with the following format
```
"MCE": "UKX...",
"NMCE": "UKX...",
"LOCATION": "MTX RACK details",
"SNMP_SHA": "SHA KEY",
"SNMP_AES": "AES KEY",
"TACACS_PASSWORD": "PASSWORD",
"LOCAL_PASSWORD": "PASSWORD",
"LOOPBACK": "IP OF DEVICE LO I/F",
"MPE_HSRP_IP": "VLAN 600 VIP",
"VLAN600_IP": "VLAN 600 LOCAL IP",
"SUBNETMASK_LENGTH": "BITS NUMBER"
"MPE": "PE hostname",
"MPE_IF": "PE I/F number"
```
