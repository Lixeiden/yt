source ./venv/bin/activate
gunicorn --workers=3 --threads=2 --worker-class=gthread --bind=127.0.0.1:8002 'app:create_app(testing=False)'

# *************************

# equivalent to 'from hello import app'
#$ gunicorn -w 4 'hello:app'

# equivalent to 'from hello import create_app; create_app()'
#$ gunicorn -w 4 'hello:create_app()'

# The -w option specifies the number of processes to run; a starting value could be CPU * 2. The default is only 1 worker, which is probably not what you want for the default worker type.
# Logs for each request aren’t shown by default, only worker info and errors are shown. To show access logs on stdout, use the --access-logfile=- option.
