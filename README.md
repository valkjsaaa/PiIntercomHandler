Raspberry Pi Intercom Handler
============================
[Jackie (Junrui) Yang](https://jackieyang.me)
----------------------------

This a project about using a fax modem to automatically unlock the door when some one calls using the building intercom system.

To run the program, you need to install the following packages:
```
python3 -m pip install pyserial
```

To run the program, you need to change the path to the serial port in the main.py file, and then run the following command:
```
python3 main.py
```

To run the program as a service, you also need to change the path to the script in the pi_intercom.service file, and then run the following command:
```
sudo cp pi_intercom.service /etc/systemd/system/
sudo systemctl enable pi_intercom.service
sudo systemctl start pi_intercom.service
```
