from fastapi import FastAPI
from helper import update, get

app = FastAPI()


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
    print(price)
    if 'null' not in price:
        return {
        "abc": price[0],
        "deinze": price[1]
    }
    return {"error": "some data is missing"}
    