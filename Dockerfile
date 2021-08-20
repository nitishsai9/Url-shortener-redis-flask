FROM python:3.7

WORKDIR /app
EXPOSE 3000

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .