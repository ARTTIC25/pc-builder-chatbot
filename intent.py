def purpose(message):
    message=message.lower()

    if "gaming" in message:
        return "gaming"
    elif "editing" in message:
        return "editing"
    elif "programming" in message:
        return "programming"
    else:
        return "general"