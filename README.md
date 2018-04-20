*Flash Memory Card with Raspian Disk Image  
(Instruction Here: https://www.raspberrypi.org/documentation/installation/installing-images/)  
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

*Install Azure Module (You may need to run this command multiple times for all packages to install)  
sudo pip3 install azure  

*Clone BSF Folder  
git clone https://github.com/rashaadfontenot/BSF.git  

Open file Pi_Table_Storage.py  
Update BIN_ID to current Bin Number  
Save file

*Run Program at Startup on PI  
sudo nano /etc/rc.local  
Add the below command in the line above exit 0  
sudo python3 /home/pi/BSF/Pi_Table_Storage.py &  
Exit and Save
sudo reboot  

Check to see if data is uploading
