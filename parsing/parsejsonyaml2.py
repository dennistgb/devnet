import json, yaml

with open("myfile.yaml") as file:
    ouryaml = yaml.safe_load(file)

print(ouryaml)

accestk = ouryaml["access_token"]
expiry = ouryaml["expires_in"]

print( accestk)
print(expiry)

jsonyaml = json.dumps(ouryaml, indent=4)

print(jsonyaml)