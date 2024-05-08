FROM python:3.11-slim-bookworm

COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p /data

EXPOSE 8000

CMD ["fastapi", "run", "src/app.py"]