FROM python:3.11-slim-bookworm

COPY . .

RUN apt-get update
RUN apt-get -y install cron curl
RUN service cron start
RUN chmod 0644 /scripts/update.sh
RUN crontab -l | { cat; echo "*/1 * * * * bash /scripts/update.sh"; } | crontab -

RUN pip install -r requirements.txt

RUN mkdir -p /data

EXPOSE 8000

CMD ["fastapi", "run", "src/app.py"]