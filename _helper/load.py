import requests, json
import logging
import time
import os

logging.basicConfig(
    level = logging.INFO,
    handlers = [logging.StreamHandler()])
logger = logging.getLogger(__name__)

headers = {
    "content-type": "application/json"
}

'''
Improve the bulk loading process.  Curling @data files encountered an encoding issue
so this python script corrects while loading the datafile and post/put against the
database using requests==2.22.0+.

bulking: https://docs.couchdb.org/en/2.3.1/api/database/bulk-api.html?highlight=bulk#inserting-documents-in-bulk
'''

if __name__ == "__main__":

    #sleep a bit to allow the couch instance to come online
    time.sleep(5)

    try:

        # load data to encode and post via requests
        data_json = './data/players.json'
        print('loading data file {}'.format(data_json))
        with open(data_json, encoding = 'utf-8') as r:
            players = json.load(r)

        url = 'http://couch:5984/baseball?n=1'
        response = requests.put(url, headers = headers)
        if response.status_code not in [201, 412]:
            raise Exception("Database creation failed! {}".format(response.text))
        logger.info('PUT request completed successfully: {}'.format(url))

        url = 'http://couch:5984/baseball/_bulk_docs'
        response = requests.post(url, headers = headers, data = json.dumps(players))
        if(response.status_code != 201):
            raise Exception("Loading team data failed! {}".format(response.text))
        logger.info('POST request completed successfully: {}'.format(url))
        logger.info('Database loading completed successfully.')
    
    except Exception as e:
        logger.error("An error occurred during database setup. {}".format(e))
