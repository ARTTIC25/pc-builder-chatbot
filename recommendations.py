import json 

def load_json(filename):
    with open("filename","r") as file:
        return json.load(file)
cpus = load_json("data/cpus.json")
gpus = load_json("data/gpus.json")
motherboards = load_json("data/motherboards.json")
rams = load_json("data/ram.json")
ssds=load_json("data/psu.json")
psus=load_json("data/psu.json")
cabinets=load_json("data/cabinets.json")
coolers=load_json("data/coolers.json")


def recommend(budget, purpose,pref_gpu):
    selected_ssd = ssds[0]

    candidate_cpus=[]
    for cpu in cpus:
        if purpose in cpu["purpose"]:
            if cpu["price"]<=budget *0.25:
                candidate_cpus.append(cpu)
    cpu=max(candidate_cpus,key= lambda x :x["cores"])

    
    candidate_gpus = []
    for gpu in gpus:
        if purpose in gpu["purpose"]:
            if gpu["price"] <= budget * 0.40:
                candidate_gpus.append(gpu)

    if pref_gpu:
        for gpu in gpus:
            if gpu["name"] == pref_gpu:
                selected_gpu = gpu
                break
    selected_gpu = max(candidate_gpus,key=lambda x: x["vram"])
    
    for board in motherboards:
        if board["socket"] == cpu["socket"]:
            motherboard = board
            break

    for memory in rams:
        if memory["ram_type"] == motherboard["ram_type"]:
            ram = memory
            break
    for ssd in ssds:
        if ssd["capacity"] == user_storage:
            selected_ssd = ssd
            break

    required = gpu["recommended_psu"]
    for psu in psus:
        if psu["wattage"] >= required:
            selected_psu = psu
            break
    

    return {
        "cpu": cpu,
        "gpus": gpus,
        "ram":ram,
        "motherboard":motherboard
    }