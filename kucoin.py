import threading
import  requests

base_url='https://api.kucoin.com'
path='/api/v1/market/histories'


def kucoin():

    threading.Timer(10, kucoin).start()
    u=requests.get(base_url+path , params={'symbol':'XLM-USDT'})
    re=u.json()
    return re






