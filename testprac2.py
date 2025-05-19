import json

with open('coo.json', 'r') as file:
    data = json.load(file)
# parse x:


# the result is a Python dictionary:
print(data["address"]["city"]) 