import json 
with open("components.json","r") as files: components=json.load(files)
def recommend(budget, purpose,pref_gpu):
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

    if pref_gpu:
        for g in components["gpus"]:
            if g["name"]==pref_gpu:
                gpus=g
    

    if cpu["socket"]=="AM4":
        motherboard=components["motherboards"][0]
    else:
        motherboard=components["motherboards"][1]

    return {
        "cpu": cpu,
        "gpus": gpus,
        "ram":ram,
        "motherboard":motherboard
    }