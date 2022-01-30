# YT
Python 3.8 + Flask 2.0.2 
http://yout.grafr.ru

Deployment (w/o Docker):
* git clone https://github.com/Lixeiden/YT.git
* python3.8 -m venv venv
* source ./venv/bin/activate
* pip install pip --upgrade
* pip install -r requirements.txt
* nginx config to /etc/nginx/sites-available + softlink + nginx -t + restart
* /etc/systemd/system/YT.service + systemctl start YT + systemctl status YT // source gunicorn_start.sh
* remove .gitkeeps
* apt install ffmpeg
* firewall: open ssh ???? & http 80 port