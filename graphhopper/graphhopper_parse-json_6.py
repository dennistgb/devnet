import requests 
import urllib.parse
import math

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
    print("\n+++++++++++++++++++++++++++++++++++++++++++++") 
    print("Vehicle profiles available on Graphhopper:") 
    print("+++++++++++++++++++++++++++++++++++++++++++++") 
    print("car, bike, foot") 
    print("+++++++++++++++++++++++++++++++++++++++++++++") 
    profile=["car", "bike", "foot"] 
    vehicle = input("Enter a vehicle profile from the list above: ") 
    if vehicle == "quit" or vehicle == "q": 
        break 
    elif vehicle in profile: 
        vehicle = vehicle 
    else:  
        vehicle = "car" 
    print("No valid vehicle profile was entered. Using the car profile.")
    loc1 = input("Starting Location: ")
    if loc1 == "quit" or loc1 =="q":
        break
    orig = geocoding(loc1,key) 
    print(orig)
    loc2 = input("Ending Location: ")
    if loc2 == "quit" or loc1 =="q":
        break
    dest = geocoding(loc2,key)
    print("================================================")
    if orig[0] == 200 and dest[0] == 200:
        op="&point="+str(orig[1])+"%2C"+str(orig[2]) 
        dp="&point="+str(dest[1])+"%2C"+str(dest[2]) 
        paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle": vehicle}) + op + dp 
        paths_status = requests.get(paths_url).status_code 
        paths_data = requests.get(paths_url).json() 
        print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url) 
        print("=================================================") 
        print("Directions from " + orig[3] + " to " + dest[3] + "by" + vehicle) 
        print("=================================================") 
        if paths_status == 200:
            km = (paths_data["paths"][0]["distance"])/1000
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60) 
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)
            print("Distance Traveled: " + str(round(km, 2)) + " km") 
            print(f"Trip Duration:  {hr}:{min}:{sec}") 
            print("=================================================")
            for each in range(len(paths_data["paths"][0]["instructions"])): 
                path = paths_data["paths"][0]["instructions"][each]["text"] 
                distance = paths_data["paths"][0]["instructions"][each]["distance"] 
                print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, 
                distance/1000/1.61)) 
            print("=============================================")
        else:
            print("Error message: " + paths_data["message"])
            print("*********************************")