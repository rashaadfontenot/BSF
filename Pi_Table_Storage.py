#!/usr/bin/env python3

from datetime import datetime
import random
import time
import requests
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import urllib
from datetime import datetime
import Adafruit_DHT as dht

#Id of Bin
Bin_ID = 'Bin_101'

# type of sensor that we're using
SENSOR = dht.DHT22 	

# pin which reads the temperature and humidity from sensor
PIN = 4			

# Connect to Azure Table service
table_service = TableService(account_name='urbanfarmingbsf', account_key='cXEulUA2YXEq0WEkGKvhTAZ2N64BUqBQ6MNMKxhrHpd2DfqnMVqi4p+ji2CbeY9WzQFTxs+umzLKa4d1Y6hVxA==')

# Connect to Azure Cosmos DB
cosmoDB_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=urbanfamingbsf;AccountKey=Bp31zHqd3KFn44Y3doAfXLlAZjLal8mSzjGEtRRarP0z5AfXWI8VuPfSPvq0thTc1JQvUKx07mMkQz0sF1WNVw==;TableEndpoint=https://urbanfamingbsf.table.cosmosdb.azure.com:443/;')


# create table
#new_table = table_service.create_table('NewUrbanFarmTable')


while True:
    rowkey = random.random()
    # read and print out humidity and temperature from sensor
    humidity,temp = dht.read_retry(SENSOR, PIN)
    temp = temp * 9/5.0 + 32
    print('Temp={0:0.1f}*F Humidity={1:0.1f}%'.format(temp, humidity))

    # ensure that timestamp string is formatted properly
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")

    # create entity object
    data = {'PartitionKey': Bin_ID, 'RowKey': str(rowkey), 'temperature': temp, 'humidity': humidity, 'datetime': now}
    table_service.insert_entity('NewUrbanFarmTable', data)
    time.sleep(30)
