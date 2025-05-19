import requests
import urllib.parse

route_url ="http://library.demo.local/api/v1/"

def retrieveBooks():
    json_data = requests.get(route_url+"books").json()
    return json_data

def print3(data):
    for i in data:
        if  i['id'] == 3:
            print(i)
        else:
            print("no match")
        

print3(retrieveBooks())
