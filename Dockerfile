FROM python:3.10-slim

RUN mkdir /telegram_bot_prozorroz

WORKDIR /telegram_bot_prozorroz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD ["./bot_prozorro_run.bat"]
#CMD ["sh", "bot_prozorro_run.sh"]
