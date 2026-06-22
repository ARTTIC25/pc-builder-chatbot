def compact(cpu,motherboard,ram):
    if cpu["socket"]== motherboard["socket"]:
        if ram["ram_type"] == motherboard["ram_type"]:
            return True
    else:
        False