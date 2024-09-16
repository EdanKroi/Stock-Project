#client
from polygon import RESTClient
import config 
import json
from typing import cast 
from urllib3 import HTTPResponse

client = RESTClient(config.API_KEY)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        'BCE', 
        1, 
        'day',
        '2024-01-01',
        '2024-05-10',
        raw = True
    ),


)

data = json.loads(aggs.data)
for item in data:
    if item == 'results':
        rawData = data[item]
closelist= []
for bar in rawData:
    for category in bar:
        if category == 'c':
            closelist.append(bar[category])

print(closelist)
