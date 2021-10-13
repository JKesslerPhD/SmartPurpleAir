# SmartPurpleAir
 This is a python script to trigger TP-Link devices based on a Purple Air Sensor's reading.  Coded to support Python3

## Getting Started (Setup)

- Install Python
- Install Dependencies:

`pip install requests`

`pip install uuid`

`pip install configparser`

`pip install matplotlib`

`pip install numpy`


- Define settings in config.ini

This program utilizes your TP-Link Kasa login information, as well as a specific Purple Air Sensor to function.  You will need to find your TP-Link login information and enter that into the `config.ini` file.  For the program to work, you will need:

- your TP-Link account username
- your TP-link account password
- the name of the TP-link device you want to control
- the sensor ID for a specific Purple Air Monitor

A sample `config_example.ini` has been created - copy it or create a new `config.ini` for your own config.

## Running the Script

The `aqi_trigger.py` file contains the example code to turn a specific TP-Link device on and off based on an AQI readings for specified purple air sensors.
For my use case, I've gone ahead and set this script up on a cloud server, and have used a cron job to run the script every 5 minutes.  If the AQI in my house goes above 30, a TP-Link plug will turn on.  This TP-Link plug is connected to a BlueAir 211 air purifier.
Additionally, I bought a "smart" air purifier to see how it would compare to my BlueAir setup. Given some days in CA with extremely poor air quality, I found a second air purifier was necessary to improve indoor air quality.  This is a Carrier air purifier, which has a
built-in PM monitor.  This monitor is not anywhere near as accurate as the Purple Air monitor inside my home.  As such, I've set this air purifier to turn on in the event that outdoor air quality is not good, or in the event that my indoor air quality is not good.  Because
this unit has an initial startup cycle, my off trigger for the unit is based on exceptionally high quality indoor and outdoor air quality.

```sh
python aqi_trigger.py
```

## Details

The script is useful for triggering TP-Link smart devices based on Purple Air sensor data. I am using this alongside indoor and outdoor Purple Air monitors to improve the air quality in my home.  If you have a sensor in your house, or close to your house, this will allow you to turn various things on or off.  

Additionally, I have modified the code to also allow for a TP-Link bulb to be used to reflect the Air Quality as indicated by a PA sensor.  This can be used to create your own "Real Time" AQI indicators in your house or elsewhere by using cheap, smart LED lights.
