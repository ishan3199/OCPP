import requests

d={'id_tag':'e1'}
URL='php url'
param={'api_dev_key': 'key-rest',
        'data':d}


r=requests.post(url=URL,data=param)