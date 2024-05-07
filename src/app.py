from fastapi import FastAPI
from helper import update, get
from fastapi_utilities import repeat_at

app = FastAPI()

@app.on_event("startup")
@repeat_at(cron="0 * * * *") # every hour
async def get_new_data():
    update()

@app.get("/update")
async def root():
    updated = update()

    if updated[0] and updated[1]:
        return {"message": "Updated ABC & Deinze"}
    if updated[0] and not updated[1]:
        return {"message": "Updated ABC"}
    if not updated[0] and updated[1]:
        return {"message": "Updated Deinze"}
    return {"message": "Updated nothing"}

@app.get("/price")
async def root():
    price = get()
    if 'null' not in price:
        return {
        "abc": price[0],
        "deinze": price[1]
    }
    return {"error": "some data is missing"}