# MCE
Jinja based project templating migration configuration

Login on Lab bastion

python3 -m venv ./mce/env
source bin/activate
pip3.6 install --upgrade Jinja2

download the base_config.py file and the file that's attached on the config quide in bastion under ~/mce/venv
chmod 775 base_config.py
./base_config.py
