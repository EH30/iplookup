import requests
import sys
import json

def getInfo(IP):
    url = "http://ip-api.com/json/"
    req = requests.get(url + IP)
    json_value = json.loads(req.content.decode())
    
    try:
        print("IP: ", json_value["query"])
        print("status: ", json_value["status"])
        print("country: ", json_value["country"])
        print("countryCode: ", json_value["countryCode"])
        print("region: ", json_value["region"])
        print("regionName: ", json_value["regionName"])
        print("city: ", json_value["city"])
        print("zip: ", json_value["zip"])
        print("lat: ", json_value["lat"])
        print("lon: ", json_value["lon"])
        print("timezone: ", json_value["timezone"])
        print("isp: ", json_value["isp"])
        print("org: ", json_value["org"])
        print("as: ", json_value["as"])
    except KeyError:
        pass


if __name__ == "__main__":
    try:
        getInfo(sys.argv[1])
    except IndexError:
        print("[-]IndexError")
        print("Usage: python iplookup.py IP")
        
