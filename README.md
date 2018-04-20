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
cd ..  

*Install Azure Module  
sudo pip3 install azure  
cd ..  

*Clone BSF Folder  
git clone https://github.com/rashaadfontenot/BSF.git  

Open file Pi_Table_Storage.py  
Update Bin number  

*Run Program at Startup on PI  
sudo nano /etc/rc.local  
sudo python3 /home/pi/BSF/Pi_Table_Storage.py &  
sudo reboot  

Check to see if data is uploading
