FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR /usr/app

RUN apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

COPY ./ ./