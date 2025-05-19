import json
import yaml

with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.dump(yaml_file)

print(ouryaml)

