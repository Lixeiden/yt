source ./venv/bin/activate
gunicorn --workers=3 --threads=2 --worker-class=gthread --bind=127.0.0.1:8002 'app:create_app(testing=False)'