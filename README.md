# YT
Python 3.8 + Flask 2.0.2 
http://yout.grafr.ru

Deployment (w/o Docker):
1. git clone https://github.com/Lixeiden/YT.git
2. python3.8 -m venv venv
3. source ./venv/bin/activate
4. pip install pip --upgrade
5. pip install -r requirements.txt
6. nginx config to /etc/nginx/sites-available + softlink + nginx -t + restart
7. /etc/systemd/system/YT.service + systemctl start YT + systemctl status YT // source gunicorn_start.sh
8. remove .gitkeeps
9. apt install ffmpeg