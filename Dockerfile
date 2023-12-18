FROM python:3.10-slim

RUN mkdir /telegram_bot_prozorro

WORKDIR /telegram_bot_prozorro

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh
