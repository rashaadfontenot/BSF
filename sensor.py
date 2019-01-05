#!/usr/bin/env python3

import serial
from datetime import datetime
import random
import time
import requests
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import urllib
from datetime import datetime
	

# Connect to Azure Table service
table_service = TableService(account_name='urbanfarmingbsf', account_key='KEY')

# Connect to Azure Cosmos DB
cosmoDB_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=urbanfamingbsf;AccountKey=TableEndpoint=https://urbanfamingbsf.table.cosmosdb.azure.com:443/;')


# create table
#new_table = table_service.create_table('NewUrbanFarmTable')

ser = serial.Serial('/dev/ttyACM0',9600)
sensor_id = 'Gas_Sensor_1'

while True:
    value = int(ser.readline().strip())
    rowkey = random.random()

    # ensure that timestamp string is formatted properly
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")

    # create entity object
    data = {'PartitionKey': sensor_id, 'RowKey': str(rowkey), 'ammonia': value, 'hydrogen_sulfide': value, 'datetime': now}
    table_service.insert_entity('GasSensor', data)
    time.sleep(1)
