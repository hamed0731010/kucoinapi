import redis
from redis.commands.json.path import Path
import json
from  kucoin import  kucoin
import threading
import  requests
def new_redis():
    base_url = 'https://api.kucoin.com'
    path = '/api/v1/market/histories'
    threading.Timer(5.0, new_redis).start()
    u = requests.get(base_url + path, params={'symbol': 'XLM-USDT'})
    re = u.json()
    client1=redis.Redis(host='redis-19031.c232.us-east-1-2.ec2.cloud.redislabs.com',db=0, port=19031, password="4ENg0qBfOv9at2MUvzsMQ8mxXE3NZEvs")
    d = client1.json().set('person:1', Path.root_path(), re)












    
    #g=rj.jsonset('obj', Path.rootPath(), data)
    #client1 = redis.ConnectionPool(host='localhost', port=6379)
    #client1.mset({"key-1":"value1","key2":"value2"})
    #c=client1.set(1,"hello")




    #g=client1.get("key1")
    #g1=redis.Redis.execute_command('JSON.SET','abc','.',json.dumps(data))
    #g=redis.StrictRedis(connection_pool=client1)
    # client1 = Client(, decode_responses=True)
    # data=kucoin()
    # f=open('sample.json')
    # data=json.load(f)
    # threading.Timer(10, new_redis()).start()