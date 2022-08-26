FROM python:3.9.13-alpine
#FROM python:3.8-slim-buster

ENV PATH="/scripts:${PATH}"

COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./dashboard /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmd -R 755 /vol/web
USER user

# COPY cmd.sh /  
# RUN chmod +x /cmd.sh

CMD ["entrypoint.sh"]