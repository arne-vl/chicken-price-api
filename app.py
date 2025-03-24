from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from backend import LocalBackend
from scraper import get_price_abc, get_price_deinze
from custom_types import PriceData
import time
import logging

app = FastAPI()
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

load_dotenv()
backend = LocalBackend()


def scheduledjob():
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Checking Price")
    update()


scheduler = BackgroundScheduler()
scheduler.add_job(scheduledjob, "interval", hours=1)
scheduler.start()


@app.on_event("startup")
def startup_event():
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Started")
    scheduledjob()


@app.get("/update")
def update():
    abc_result = backend.write_abc(get_price_abc())
    deinze_result = backend.write_deinze(get_price_deinze())

    return {
        "abc_updated": abc_result,
        "deinze_updated": deinze_result
    }

@app.get("/current-price")
def get_current_price() -> PriceData:
    return backend.get_current_price()


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
