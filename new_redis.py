import redis
from redis.commands.json.path import Path
import json
from  kucoin import  kucoin
import threading
import  requests
def new_redis():
    base_url = 'https://api.kucoin.com'
    path = '/api/v1/market/histories'
    threading.Timer(10.0, new_redis).start()
    u = requests.get(base_url + path, params={'symbol': 'XLM-USDT'})
    re = u.json()
    client1=redis.Redis(host='redis-19031.c232.us-east-1-2.ec2.cloud.redislabs.com',db=0, port=19031, password="4ENg0qBfOv9at2MUvzsMQ8mxXE3NZEvs")
    d = client1.json().set('person:1', Path.root_path(), re)

















