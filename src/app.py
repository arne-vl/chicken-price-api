from contextlib import asynccontextmanager
from fastapi import FastAPI
from helper import update, get
from fastapi_utilities import repeat_at

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    update()
    yield

app = FastAPI(lifespan=app_lifespan, debug=True)

@repeat_at(cron="0 * * * *") # every hour
async def get_new_data():
    update()

@app.get("/update")
async def root():
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
async def root():
    price = get()
    if 'null' not in price:
        return {
        "abc": price[0],
        "deinze": price[1]
    }
    return {"error": "some data is missing"}