FROM python:latest

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "crawler_ml.py", "start"]
