from fastapi import FastAPI
from helper import update, get
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging

app = FastAPI()
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

def scheduledjob():
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Checking Price")
    update()

scheduler = BackgroundScheduler()
scheduler.add_job(scheduledjob, 'interval', minutes=1)
scheduler.start()

@app.on_event("startup")
def startup_event():
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Started")
    update()

@app.get("/update")
def root():
    updated = update()

    msg = "Updated nothing"

    if updated[0] and updated[1]:
        msg = "Updated ABC & Deinze"
        return {"message": msg}
    if updated[0] and not updated[1]:
        msg = "Updated ABC"
        return {"message": msg}
    if not updated[0] and updated[1]:
        msg = "Updated Deinze"
        return {"message": msg}

    return {"message": msg}

@app.get("/price")
def root():
    price = get()
    if 'null' not in price:
        return {
        "abc": price[0],
        "deinze": price[1]
    }
    return {"error": "some data is missing"}

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
