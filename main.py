from typing import Union
from new_redis import new_redis
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Depends
import  threading
import redis
import json
#from kucoin import kucoin
app = FastAPI()
#obj1=kucoin()
data=new_redis()
#f=open('sample.json')
#data=json.load(f)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    data
    client1 = redis.Redis(host='redis-19031.c232.us-east-1-2.ec2.cloud.redislabs.com', db=0, port=19031,
                          password="4ENg0qBfOv9at2MUvzsMQ8mxXE3NZEvs")
    d = client1.json().get('person:1')
    return d

async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}
