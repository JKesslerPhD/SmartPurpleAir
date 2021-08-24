import requests
import uuid

class TPLink():
    def __init__(self, username, password):
        """
        

        Parameters
        ----------
        username : string
            Your TP-Link account login name
        password : string
            Your TP-Link account password

        Returns
        -------
        None.

        """
        self.token = self.getKasaToken(username, password)
        self.devices = self.getDevices(self.token)
        

    def getKasaToken(self, username, password):
        """
        

        Parameters
        ----------
        username : string
           Your TP-Link account login name
        password : string
            Your TP-Link account password

        Raises
        ------
        Exception
            Unable to login to TP-Link Account

        Returns
        -------
        token : string
            The information necessary to utilize devices on your TP-Link Account

        """
    
        payload = {
        "method":"login",
        "params": {
            "appType":"Kasa_Android",
            "cloudUserName":username,
            "cloudPassword": password,
            "terminalUUID":str(uuid.uuid4())
            }
        }
        
        r = requests.post("https://wap.tplinkcloud.com", json=payload)
        obj = r.json()
        try:
            token = obj["result"]["token"]
        except:
            raise Exception("There was an error logging into your TP-Link Account.  Check your username and password.")
        return token
        
    def getDevices(self, token):
        """
        

        Parameters
        ----------
        token : string
            The token affiliated with a valid TP-Link account login

        Returns
        -------
        device_list : list
            list of all devices on your TP-Link account

        """
        payload = {"method": "getDeviceList"}
        device_list = requests.post("https://wap.tplinkcloud.com?token={}".format(token), json=payload)
        d = device_list.json()
        device_list = {}
        for element in d['result']['deviceList']:
            device_list[element["alias"]] = KasaDevice(element["alias"], self.token, element["deviceId"])
        return device_list
        
    def findDevice(self, kasa_name):
        """
        

        Parameters
        ----------
        kasa_name : string
            Will return the device associated with the name you specified in your Kasa TP-Link device setup

        Raises
        ------
        Exception
            The device could not be found

        Returns
        -------
        TYPE
            device object, which can be turned off or on.

        """
        for d in self.devices.keys():
            if kasa_name in d:
                return self.devices[d]
        raise Exception("Device named %s not found on TP-Link Account" % kasa_name)
        
        


class KasaDevice():
    def __init__(self, alias, token, deviceID):
        self.alias = alias
        self.token = token
        self.deviceID = deviceID
        
    def TurnOn(self):
        try:
            self.modifyKasaDeviceState(1)
        except:
            raise Exception("Unable to turn device '%s' on" % self.alias)
    
    def TurnOff(self):
        try:
            self.modifyKasaDeviceState(0)
        except:
            raise Exception("Unable to turn device '%s' off" % self.alias)
        
    def modifyKasaDeviceState(self, deviceState):
        payload = {
                "method": "passthrough",
                "params": {
                    "deviceId": self.deviceID,
                    "requestData":
                        '{\"system\":{\"set_relay_state\":{\"state\":' + str(deviceState) + '}}}'
                }
            }
        r = requests.post(url="https://use1-wap.tplinkcloud.com/?token={}".format(self.token), json=payload)
    
    

    
    
