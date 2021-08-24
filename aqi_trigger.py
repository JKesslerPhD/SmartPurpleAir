import kasaAPI as kapi
import purpleair as pa
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')


# Load Relevant Settings
pa_sensor_id = config["PurpleAir"]["sensor_id"]
username = config["Kasa"]["username"]
password = config["Kasa"]["password"]
kasa_name = config["Kasa"]["device_name"]


# Connect to your Kasa Account
c = kapi.TPLink(username, password)

# Select the device to be turned on/off
device = c.findDevice(kasa_name)

# Check a specific Purple Air sensor
m = pa.Monitor(pa_sensor_id)

#print("Sensor's Air Quality is {} (considered '{}')".format(m.aqi, m.status))
 
# Turn on or off smart switch based on AQI trigger
# This can also be set to a relevant status; e.g. != "Good"
# Check purpleair.py AQI class for status codes, or PrupleAir API docs
if m.aqi > 30:
    device.TurnOn()
else:
    device.TurnOff()