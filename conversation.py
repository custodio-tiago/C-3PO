def handle_greetings(message):
    greetings = ["oi", "olá", "hello", "hi"]
    if any(greeting in message.lower() for greeting in greetings):
        return "Olá! Como posso ajudá-lo hoje?"
    return None
