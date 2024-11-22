import re
import random

def handle_greetings(message):
    greetings = ["oi", "olá", "hello", "hi"]
    # Verifica se qualquer saudação é encontrada como uma palavra isolada
    for greeting in greetings:
        # A expressão regular busca a saudação isolada (exemplo: " oi ", " oi!" ou "oi.")
        if re.search(r'\b' + re.escape(greeting) + r'\b', message.lower()):
            return "Olá! Como posso ajudá-lo hoje?"
    return None

def sendRandomMessage():
    # Lista de mensagens aleatórias
    messages = [
        # 15 Frases clássicas de C-3PO
        "Olá, eu sou C-3PO, fluente em mais de seis milhões de formas de comunicação.",
        "Eu sou programado para entender e falar mais de seis milhões de idiomas.",
        "Você tem certeza de que isso é uma boa ideia, mestre?",
        "Oh, eu sinto muito, mas não posso permitir isso.",
        "Cuidado! Eu detectei uma presença muito forte no lado negro da Força.",
        "Minha programação me impede de mentir, mas não posso deixar de dizer que estamos em apuros.",
        "Senhor, isso não é uma boa situação.",
        "Eu preferiria não entrar em um confronto direto com o Império.",
        "A missão de resgatar a princesa foi bem-sucedida, mas foi um trabalho árduo.",
        "A nave está em pleno funcionamento, mas há algo estranho nas leituras dos sensores.",
        "Master Luke, o que devo fazer agora?",
        "Minha memória está cheia de informações valiosas, mas não sou capaz de proteger todas elas.",
        "Eu recomendo que você não se envolva diretamente com os Sith.",
        "Estou recebendo sinais de distúrbio no Império, podemos não estar sozinhos.",
        "Por favor, me avise quando a situação ficar fora de controle.",

        # 15 Frases sobre Star Wars em geral
        "A Força está com você, sempre.",
        "Que a Força esteja com você!",
        "O lado negro da Força é perigoso, muito perigoso.",
        "Eu sinto a presença do Império se aproximando.",
        "Darth Vader pode ser mais poderoso do que imaginamos.",
        "Há muitos mistérios na galáxia.",
        "O Império nunca desiste de sua busca pelo controle total.",
        "Os Jedi são conhecidos por sua habilidade de manipular a Força.",
        "Luke Skywalker pode ser o único que pode restaurar o equilíbrio.",
        "O império tem muitas estratégias secretas.",
        "Os Stormtroopers podem ser imprecisos, mas são muitos.",
        "A aliança rebelde é um símbolo de esperança para a galáxia.",
        "A destruição da Estrela da Morte foi uma grande vitória.",
        "O lado luminoso da Força pode curar, proteger e dar esperança.",

        # 20 Curiosidades sobre programação
        "Em Python, você pode usar list comprehensions para escrever código mais conciso e eficiente.",
        "O Java foi originalmente criado para ser uma linguagem para dispositivos eletrônicos, mas acabou se tornando uma das mais populares para desenvolvimento web.",
        "Em C, a função 'printf' é frequentemente usada para exibir informações na tela.",
        "A recursão é uma técnica de programação onde uma função se chama dentro de si mesma.",
        "No Python, um 'list' pode ser modificado em tempo real, enquanto uma 'tuple' é imutável.",
        "A variável 'null' em JavaScript é um valor que representa a ausência de valor.",
        "Em C, a memória deve ser gerenciada manualmente, o que pode levar a vazamentos de memória se não for bem gerido.",
        "Em Python, a indentação correta é crucial para o funcionamento do código.",
        "O Git é uma ferramenta essencial para controle de versão em projetos de programação.",
        "Os algoritmos de ordenação, como o QuickSort, são amplamente utilizados para melhorar a eficiência do processamento de dados.",
        "Em Java, 'String' é uma classe e não um tipo primitivo.",
        "A biblioteca 'numpy' do Python é muito usada para cálculos matemáticos e manipulação de grandes conjuntos de dados numéricos.",
        "Em JavaScript, o 'undefined' é um valor de uma variável que não foi atribuída.",
        "A linguagem Assembly é a mais próxima da linguagem de máquina, e cada comando corresponde a uma instrução do processador.",
        "O conceito de 'interfaces' em Java permite a implementação de métodos sem definição, o que é útil para flexibilidade.",
        "A programação orientada a objetos em Java permite o uso de 'classes' e 'objetos' para representar dados e funcionalidades.",
        "A técnica de 'depuração' é usada para encontrar e corrigir erros no código.",
        "No Python, funções anônimas são chamadas de 'lambda'.",
        "O uso de 'algoritmos de busca' pode ser crucial para encontrar informações rapidamente em grandes bases de dados.",
        "Em C++, o operador 'new' é usado para alocar memória dinamicamente."

         # 15 Frases de C-3PO moderando o servidor
        "Peço a todos que mantenham a calma!!! A situação está sob controle, espero.",
        "Por favor, respeitem as regras, senão a situação pode se complicar!",
        "Lembre-se, senhores, devemos manter a ordem e a compostura em todos os momentos.",
        "Ah, uma pequena discussão, mas nada que não possa ser resolvido de forma pacífica.",
        "Parece que a tensão aumentou um pouco, vamos manter a calma, por favor!",
        "Deixe-me lembrar a todos que uma conversa civilizada é muito mais produtiva.",
        "Senhores, não precisamos de mais conflito, o ambiente deve ser pacífico!",
        "Com todo o respeito, gostaria de pedir um pouco de ordem no servidor.",
        "A calma é o melhor remédio para qualquer situação. Vamos evitar o caos!",
        "Senhor, este ambiente não parece propício para discussões acaloradas.",
        "Por favor, todos, vamos manter a compostura e não perder o controle.",
        "Não há necessidade de gritar, senhores! Vamos manter um nível de civilidade.",
        "Eu sou C-3PO, fluente em 6 milhões de formas de comunicação, e até eu sei que é melhor manter a paz.",
        "Por favor, senhores, não vamos arruinar a harmonia do servidor com discussões desnecessárias.",
        "Este é um momento para manter a calma, não para perder a cabeça."
    ]
    
    return random.choice(messages)
