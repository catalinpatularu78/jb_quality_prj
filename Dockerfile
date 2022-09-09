FROM tiangolo/uwsgi-nginx:python3.8

LABEL NAME=my_app Version=0.0.1

EXPOSE 8000
ENV LISTEN_PORT=8000

ENV UWSGI_INI uwsgi.ini

ADD . /app
WORKDIR /app

RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3

RUN python -m pip install -r requirements.txt
