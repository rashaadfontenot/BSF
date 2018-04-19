from azure.cosmosdb.table import TableService
from datetime import datetime
import random
import time

#Setup connection to database
the_connection_string = "DefaultEndpointsProtocol=https;AccountName=urbanfamingbsf;AccountKey=Bp31zHqd3KFn44Y3doAfXLlAZjLal8mSzjGEtRRarP0z5AfXWI8VuPfSPvq0thTc1JQvUKx07mMkQz0sF1WNVw==;TableEndpoint=https://urbanfamingbsf.table.cosmosdb.azure.com:443/;"
table_service = TableService(endpoint_suffix = "table.cosmosdb.azure.com", connection_string = the_connection_string)

#create table
#table = table_service.create_table('UrbanFarming_BSF')


rowkey = 0
while True:
    rowkey += 1
    #read and print out humidity and temperature from sensor
    humidity = random.randrange(25, 84)
    temp = random.randrange(34, 99)
    print('Temp={0:0.1f}*F Humidity={1:0.1f}%'.format(temp, humidity))

    # ensure that timestamp string is formatted properly
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")

    #create entity object
    data = {'PartitionKey': 'Bin_101', 'RowKey': str(rowkey), 'temperature' : temp, 'humidity' : humidity, 'datetime' : now}
    table_service.insert_entity('UrbanFarming_BSF', data)
    time.sleep(10)
