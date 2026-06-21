import json 
with open("components.json","r") as files: components=json.load(files)
def recommend(budget, purpose):
    ram =components["ram"][0]

    if purpose == "gaming":

        if budget <= 50000:
            cpu = components["cpus"][0]
            gpus = components["gpus"][0]

        else:
            cpu = components["cpus"][2]
            gpus = components["gpus"][2]

    elif purpose == "editing":

        cpu = components["cpus"][1]
        gpus = components["gpus"][0]

    else:

        cpu = components["cpus"][0]
        gpus = components["gpus"][0]

    return {
        "cpu": cpu["name"],
        "gpus": gpus["name"],
        "ram":ram["name"]
    }