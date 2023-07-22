FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY server_name.conf /etc/nginx/snippets/server_name.conf

WORKDIR /static

COPY robots.txt robots.txt

COPY favicon.ico favicon.ico
