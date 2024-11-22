import re

def handle_greetings(message):
    greetings = ["oi", "olá", "hello", "hi"]
    # Verifica se qualquer saudação é encontrada como uma palavra isolada
    for greeting in greetings:
        # A expressão regular busca a saudação isolada (exemplo: " oi ", " oi!" ou "oi.")
        if re.search(r'\b' + re.escape(greeting) + r'\b', message.lower()):
            return "Olá! Como posso ajudá-lo hoje?"
    return None
