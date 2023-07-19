FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY server.conf /etc/nginx/conf.d/server.conf

WORKDIR /static

COPY robots.txt robots.txt

COPY favicon.ico favicon.ico
