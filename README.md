# BSF
Code For Black Soldier Fly Project


Reference this https://github.com/adafruit/Adafruit_Python_DHT to get library


Python IOT Hub 
https://github.com/Azure-Samples/iot-hub-python-raspberrypi-client-app


Download Azure IOT managment
pip install azure-mgmt-iothub


Install Linux SDK on Pi's
https://github.com/Azure/azure-iot-sdk-python/blob/master/doc/python-devbox-setup.md

Follow Steps
https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-python-getstarted

*Flash Memory Card with Raspian Disk Image
Insert memory card
Open Etcher

*Update Pi local preferences 
PI Menu > Preferences > Raspberry PI Configuration > Localisation > Update all categories to US
Click OK, Reboot PI

*Connect to Wifi

*Download Adafruit Python Sensor Library
Open Terminal
sudo apt-get update
sudo apt-get install python3-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install

*Install Azure Module
sudo pip3 install azure
git clone git://github.com/Azure/azure-sdk-for-python.git
cd azure-sdk-for-python
sudo python3 setup.py install
cd ..

*Clone BSF Folder
git clone https://github.com/rashaadfontenot/BSF.git

