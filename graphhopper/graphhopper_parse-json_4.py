import requests 
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
#loc1 = "Washington, D.C."

key = "8f15d6a0-daf5-4264-826f-ac6bbcc402c7"
#key = "9f15d6a0-daf5-4264-826f-ac6bbcc402c7"


def geocoding(location, key):
    while location == "":
        location = input("Enter the location again: ")
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": 1, "key": key})
    replydata = requests.get(url)
    json_status = replydata.status_code
    json_data = replydata.json()
    if json_status == 200 and len(json_data["hits"]) != 0:
       
        lat = json_data['hits'][0]['point']['lat']    
        lng =  json_data['hits'][0]['point']['lng']  
        name = json_data["hits"][0]["name"] 
        value = json_data["hits"][0]["osm_value"] 
         
        if "country" in json_data["hits"][0]: 
            country = json_data["hits"][0]["country"] 
        else: 
            country="" 
         
        if "state" in json_data["hits"][0]: 
            state = json_data["hits"][0]["state"] 
        else: 
            state="" 
         
        if len(state) !=0 and len(country) !=0: 
            new_loc = name + ", " + state + ", " + country 
        elif len(state) !=0: 
            new_loc = name + ", " + country 
        else: 
            new_loc = name         
         
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url) 

    else: 
        lat="null" 
        lng="null" 
        new_loc=location 
        if json_status != 200:
            print(f"Geocode API status: {str(json_status)} + \n Error message: {json_data['message']}")
    return json_status,lat,lng,new_loc
    
while 1:
    loc1 = input("Starting Location: ")
    if loc1 == "quit" or loc1 =="q":
        break
    orig = geocoding(loc1,key) 
    print(orig)
    loc2 = input("Ending Location: ")
    if loc2 == "quit" or loc1 =="q":
        break
    dest = geocoding(loc2,key)
    print(dest)