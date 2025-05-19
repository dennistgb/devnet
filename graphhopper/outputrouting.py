import requests
import urllib.parse
import math
# No need to import sys for this terminal redirection method

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
#loc1 = "Washington, D.C."

key = "8f15d6a0-daf5-4264-826f-ac6bbcc402c7"
#key = "9f15d6a0-daf5-4264-826f-ac6bbcc402c7"


def geocoding(location, key):
    # Note: Prompts inside this function will still appear in the terminal
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

        # Improved location formatting logic
        new_loc_parts = [name]
        if state:
            new_loc_parts.append(state)
        if country:
             new_loc_parts.append(country)
        new_loc = ", ".join(new_loc_parts)


        # This print will be redirected to the file by the terminal
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)

    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:
            error_message = json_data.get('message', 'Unknown API error')
            # This print will be redirected to the file
            print(f"Geocode API status: {str(json_status)} \n Error message: {error_message}")
        elif len(json_data["hits"]) == 0:
             # This print will be redirected to the file
             print("No location found for: " + location)
    return json_status,lat,lng,new_loc

# --- Main Script Logic ---
# Messages printed here will be redirected to the file
print("GraphHopper Routing Script")
print("Enter 'quit' or 'q' at any input prompt to exit.")


while 1:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    vehicle_input = input("Enter a vehicle profile from the list above: ") # This input stays in terminal
    profile=["car", "bike", "foot"] 
    # Clean and normalize the input
    vehicle = vehicle_input.strip().lower()

    if vehicle == "quit" or vehicle == "q":
        break
    elif vehicle in profile:
        pass # vehicle is already set to the cleaned input
    else:
        vehicle = "car"
        # This print will be redirected to the file
        print("No valid vehicle profile was entered. Using the car profile.")

    loc1 = input("Starting Location: ") # This input stays in terminal
    if loc1 == "quit" or loc1 =="q":
        break
    orig = geocoding(loc1,key)
    # This print will be redirected to the file
    print(f"Origin Geocoding Result: {orig}")

    loc2 = input("Ending Location: ") # This input stays in terminal
    # Corrected the quit condition check to use loc2
    if loc2 == "quit" or loc2 =="q":
        break
    dest = geocoding(loc2,key)
    # This print will be redirected to the file
    print(f"Destination Geocoding Result: {dest}")


    # Messages printed here will be redirected to the file
    print("================================================")
    if orig[0] == 200 and dest[0] == 200:
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle": vehicle}) + op + dp

        paths_response = requests.get(paths_url)
        paths_status = paths_response.status_code
        paths_data = paths_response.json()

        print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url)
        print("=================================================")
        print("Directions from " + orig[3] + " to " + dest[3] + " by " + vehicle)
        print("=================================================")
        if paths_status == 200:
            if "paths" in paths_data and len(paths_data["paths"]) > 0:
                km = (paths_data["paths"][0]["distance"])/1000
                sec = int(paths_data["paths"][0]["time"]/1000%60)
                min = int(paths_data["paths"][0]["time"]/1000/60%60)
                hr = int(paths_data["paths"][0]["time"]/1000/60/60)
                print("Distance Traveled: " + str(round(km, 2)) + " km")
                print(f"Trip Duration:  {hr}:{min}:{sec}")
                print("=================================================")
                if "instructions" in paths_data["paths"][0]:
                    for each in range(len(paths_data["paths"][0]["instructions"])):
                        instruction = paths_data["paths"][0]["instructions"][each]
                        if "text" in instruction and "distance" in instruction:
                             path = instruction["text"]
                             distance = instruction["distance"]
                             print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000,
                             distance/1000/1.61))
                        else:
                             print("Missing instruction data in API response.")
                else:
                     print("No instructions found for this route.")
                print("=============================================")
            else:
                 print("No path found for this route.")
                 print("*********************************")

        else:
            if "message" in paths_data:
                 print("Error message: " + paths_data["message"])
            else:
                 print("Unknown error occurred during routing.")
            print("*********************************")
    else:
        print("Could not perform routing. Geocoding failed for one or both locations.")
        print("*********************************")

# Final message - This will also be redirected to the file
print("\nScript execution finished.")