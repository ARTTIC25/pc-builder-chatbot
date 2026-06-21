
import json
with open("components.json","r") as files:
    components=json.load(files)
def recommedn(budget):
    ram =components["ram"][0]
    if budget <= 50000:
            cpu = components["cpus"][0]
            gpus = components["gpus"][0]
        
    elif budget <=80000:
        
            cpu = components["cpus"][2]
            gpus = components["gpus"][2]
        
    else:
        
            cpu = components["cpus"][1]
            gpus = components["gpus"][1]
        
    return {
          "cpu":cpu["name"],
          "gpus":gpus["name"],
          "ram":ram["name"]

          
    }
        