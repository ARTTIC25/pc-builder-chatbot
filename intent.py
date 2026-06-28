#purpose detection
def purpose(message):
    message=message.lower()
    
    gaming = [
        "gaming",
        "game",
        "valorant",
        "gta",
        "minecraft",
        "fortnite",
        "pubg",
        "cs2",
        "elden ring"
    ]

    editing = [
        "editing",
        "premiere",
        "after effects",
        "photoshop",
        "davinci",
        "blender"
    ]

    programming = [
        "coding",
        "python",
        "programming",
        "developer",
        "vs code",
        "machine learning"
    ]

    for word in gaming:
        if word in message:
            return "gaming"
        
    for word in editing:
        if word in message:
            return "editing"
        
    for word in programming:
        if word in message:
            return "programming"
   
    return "general"

#brand detection
def detect_cpu(message):

    message = message.lower()

    if "amd" in message:

        return "AMD"

    elif "intel" in message:

        return "Intel"

    return None

#ram detection
def detect_ram(message):

    message = message.lower()

    if "16gb" in message:

        return 16

    elif "32gb" in message:

        return 32

    return None

#detect storage
def detect_storage(message):

    message = message.lower()

    if "512gb" in message:

        return 512

    elif "1tb" in message:

        return 1000

    elif "2tb" in message:

        return 2000

    return None

#detect resolution
def detect_resolution(message):

    message = message.lower()

    if "1080p" in message:

        return "1080p"

    elif "1440p" in message:

        return "1440p"

    elif "4k" in message:

        return "4K"

    return None