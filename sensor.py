import sys
from arduino import Arduino
import time
import serial

'''Connect to Azure IOT hub'''
CONNECTION_STRING = "HostName=BlackSoldierFly.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=xOiEuZJhNRslxtkio3guAyoVAkGtBRKHElBvh5xuF1I=[IoTHub Connection String]"
DEVICE_ID = "GasSensor1"

sys.path.append('/home/pi/Downloads/Python-Arduino-Proto-API-v2-master/arduino')

ard = Arduino('/dev/ttyACM0', 115200)
#digital pins that the sensors are on
mq136 = 0
mq137 = 1

while True:
    
    print(ard.analogRead(mq136))
    print(ard.analogRead(mq137))
    time.sleep(1)
