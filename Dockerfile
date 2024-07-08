FROM python:3.11-slim-bookworm

RUN apt-get update
RUN apt-get update && apt-get -y install cron curl
RUN service cron start

WORKDIR /api

COPY . .

RUN chmod 0644 /api/scripts/update.sh
RUN crontab -l | { cat; echo "*/1 * * * * bash /api/scripts/update.sh"; } | crontab -

RUN pip install -r requirements.txt

RUN mkdir -p /data

EXPOSE 8000

CMD ["fastapi", "run", "src/app.py"]