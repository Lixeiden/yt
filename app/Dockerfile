# официальный образ Python как базовый образ
FROM python:3.10-slim-buster

# Аргумент сборки для определения окружения
ARG ENV

# переменная среды ENV
ENV ENV=${ENV}

# рабочий каталог в /app
WORKDIR /app

# файл requirements.txt из локального каталога в рабочий каталог в контейнере
COPY requirements.txt requirements.txt

# pip и зависимости
RUN pip install pip -U && pip install --no-cache-dir -r requirements.txt

# все файлы из локального каталога в рабочий каталог в контейнере, исключая файлы, указанные в .dockerignore
COPY . .

# Сообщаем Docker, что приложение слушает на указанном порту во время выполнения
EXPOSE 8002

# Запустить приложение в зависимости от окружения
CMD if [ "$ENV" = "PROD" ] ; then gunicorn --workers=3 --threads=2 --worker-class=gthread --bind=0.0.0.0:8002 'app:create_app(testing=False)' ; else flask run --host=0.0.0.0 ; fi
