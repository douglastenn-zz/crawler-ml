FROM python:3.6-dev

RUN apk add --update git tzdata \
    && rm -rf /var/cache/apk/* \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" | tee /etc/TZ /etc/timezone \
    && apk del tzdata

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "crawler_ml.py", "start"]
