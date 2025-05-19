import requests 
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
#loc1 = "Washington, D.C."
loc1 = "Rome, Italy"
loc2 = "Baltimore, Maryland"
key = "8f15d6a0-daf5-4264-826f-ac6bbcc402c7"

url = geocode_url + urllib.parse.urlencode({"q": loc1, "limit": 1, "key": key})
replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

if json_status == 200:
    print(f"Geocoding API URL for {loc1} \n {url}")