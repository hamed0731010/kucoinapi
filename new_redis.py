import redis
from redis.commands.json.path import Path
import json
import threading
import  requests

def conv(lst1,lst2):
    res={lst1[i]:lst2[i] for i in range(0,len(lst1))}
    return res
def new_redis():
    base_url = 'https://api.kucoin.com'
    path = '/api/v1/market/allTickers'
    threading.Timer(5.0, new_redis).start()
    u = requests.get(base_url + path)
    re = u.json()
    client1=redis.Redis(host='redis-19031.c232.us-east-1-2.ec2.cloud.redislabs.com',db=0, port=19031, password="4ENg0qBfOv9at2MUvzsMQ8mxXE3NZEvs")
    d = client1.json().set('person:1', Path.root_path(), re)

def rate_list():
    base_url = 'https://api.kucoin.com'
    path = '/api/v1/market/allTickers'
    threading.Timer(5.0, new_redis).start()
    u = requests.get(base_url + path)
    re = u.json()
    client1 = redis.Redis(host='redis-19031.c232.us-east-1-2.ec2.cloud.redislabs.com', db=0, port=19031,
                          password="4ENg0qBfOv9at2MUvzsMQ8mxXE3NZEvs")
    #rem = client1.json().set('person:2', Path.root_path(), re)
    jn = re['data']['ticker']
    a=[]
    b=[]

    for x in jn:
        a.append(x['symbol'])
        b.append(x['sell'])

    s=conv(a,b)

    client1.set('foo', json.dumps(s))





























