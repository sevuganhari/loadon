## Update all Ubuntu Packages
sudo apt update
## Install Python3.8, PIP
## Install uwsgi
sudo apt install python3.8 python3.8-dev python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev python3-pip python3.8-venv
sudo apt-get install uwsgi-plugin-python3
sudo ufw allow 5000
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install uwsgi
export PYTHON=python3.8
uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python38"
sudo mv python38_plugin.so /usr/lib/uwsgi/plugins/python38_plugin.so
sudo chmod 666 /usr/lib/uwsgi/plugins/python38_plugin.so

