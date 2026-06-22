def detecter(message):
    message=message.lower()
    if "rtx 4060" in message:
        return "RTX 4060"
    elif "rx 6600" in message:
        return "RX 6600"
    elif "RX 7600" in message:
        return "RX 7600"

    return None