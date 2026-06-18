import json

with open("components.json","r") as file:
    components=json.load(file)
print(components)