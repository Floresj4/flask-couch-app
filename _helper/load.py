import requests, json
import logging
import time
import os

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    #sleep a bit to allow the couch instance to come online
    time.sleep(5)

    # load data to encode and post via requests
    data_json = './data/players.json'
    print('loading data file {}'.format(data_json))
    with open(data_json, encoding = 'utf-8') as r:
        players = json.load(r)

    headers = {
        "content-type": "application/json"
    }

    response = requests.put('http://couch:5984/baseball?n=1', headers = headers)
    print(response.status_code)
    response = requests.post('http://couch:5984/baseball/_bulk_docs', headers = headers, data = json.dumps(players))
    print(response.status_code)
    print(response.text)
