import json
import yaml

with open('myfile.json') as file:
    newjson = json.load(file)
print(newjson)

accesstk = newjson["access_token"]
expiry = newjson["expires_in"]
print(f"The access token is: {accesstk}")
print(f"The token expires in: {expiry}")

newyaml = yaml.dump(newjson)
print(newyaml)