from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from V2"}

@app.get("/items/{item_id}")
async def read_item(item_id):

    x = requests.get(f'http://backend:8000/items/{item_id}')
    return {
        "item_id_v2": item_id,
        "item_id_v1": x.text
        }