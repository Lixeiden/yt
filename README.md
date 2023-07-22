# yt
Flask app for video download based on yt-dlp

* put ./.env
* put ./nginx/server.conf
* set up host nginx as reverse proxy to :8002
* docker compose -f docker-compose.prod.yml up --build -d
