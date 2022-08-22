import json

class ReadData:

    # method for open, read and close json file
    # loaded to "data" variable
    def read_json(self):
        with open("configClear_v2.json","r") as file:
            x = file.read()
            data = json.loads(x)
            return data

    # method for open BDI part of json file
    def read_BDI(self):
        read_data = ReadData()
        data = read_data.read_json()
        data = data["frinx-uniconfig-topology:configuration"]
        data_cisco = data["Cisco-IOS-XE-native:native"]
        data_interface = data_cisco["interface"]
        data_bdi = data_interface["BDI"]
        return data_bdi