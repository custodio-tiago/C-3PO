import aiohttp
import random

SWAPI_BASE_URL = "https://swapi.dev/api/"

# Função para buscar na SWAPI
async def fetch_swapi_data(endpoint, search):
    url = f"{SWAPI_BASE_URL}{endpoint}/?search={search}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("results", [])
    return []

# Frases pré-definidas
PEOPLE_RESPONSES = [
    "Esse {name} parece ser uma pessoa interessante!",
    "O que {name} estaria fazendo agora?",
    "{name} é conhecido por ser {info}.",
    "Eu já ouvi falar sobre {name}. É {info} incrível!",
    "{name}? Parece um grande personagem!",
    "{name} é uma lenda em seu planeta natal!",
    "{name} é famoso por {info}.",
    "Nunca pensei que {name} fosse tão importante!",
    "{name}? Ouvi falar que ele é {info}.",
    "Os Jedi sempre falam sobre {name} com respeito.",
]

PLANET_RESPONSES = [
    "O planeta {name} é conhecido por sua {info}.",
    "{name} parece ser um lugar incrível para visitar!",
    "Ouvi dizer que {name} é um planeta {info}.",
    "Você gostaria de viver em {name}?",
    "As paisagens de {name} são {info}.",
    "Alguns dizem que {name} é o planeta mais {info} da galáxia.",
    "{name} é muito comentado pelos exploradores espaciais.",
    "Espero um dia visitar {name}.",
    "{name} é famoso por ser um local {info}.",
    "A cultura de {name} é bem peculiar.",
]

STARSHIP_RESPONSES = [
    "A nave {name} é conhecida por sua {info}.",
    "{name} é um marco na história das espaçonaves!",
    "Ouvi dizer que {name} é muito {info}.",
    "Se eu tivesse uma nave como {name}, eu viajaria o universo inteiro!",
    "A {name} é famosa por sua velocidade e {info}.",
    "A {name} é muito falada pelos pilotos espaciais.",
    "Dizem que a {name} foi usada em batalhas épicas!",
    "{name} é um dos modelos mais {info} da galáxia.",
    "Você sabia que {name} foi projetada para ser {info}?",
    "A {name} é uma lenda no espaço.",
]

# Função para buscar dados técnicos (ficha técnica)
async def get_technical_sheet(query):
    # Limpeza da entrada para extrair apenas o nome relevante (ex: "luke", "leia")
    cleaned_query = ''.join([char for char in query.strip().lower() if char.isalnum() or char.isspace()]).split()[-1]
    print(f"Consulta limpa para ficha técnica: {cleaned_query}")

    # Buscar em People (Personagens)
    people = await fetch_swapi_data("people", cleaned_query)
    if people:
        person = people[0]
        sheet = f"**Ficha Técnica - {person['name']}**\n"
        sheet += f"Nome: {person['name']}\n"
        sheet += f"Genero: {person.get('gender', 'Desconhecido')}\n"
        sheet += f"Altura: {person.get('height', 'Desconhecida')}\n"
        sheet += f"Cor dos Cabelos: {person.get('hair_color', 'Desconhecida')}\n"
        sheet += f"Cor dos Olhos: {person.get('eye_color', 'Desconhecida')}\n"
        sheet += f"Data de Nascimento: {person.get('birth_year', 'Desconhecida')}\n"
        sheet += f"Espécie: {person.get('species', 'Desconhecida')}\n"
        return sheet

    # Buscar em Planets (Planetas)
    planets = await fetch_swapi_data("planets", cleaned_query)
    if planets:
        planet = planets[0]
        sheet = f"**Ficha Técnica - {planet['name']}**\n"
        sheet += f"Nome: {planet['name']}\n"
        sheet += f"Clima: {planet.get('climate', 'Desconhecido')}\n"
        sheet += f"Terreno: {planet.get('terrain', 'Desconhecido')}\n"
        sheet += f"População: {planet.get('population', 'Desconhecida')}\n"
        return sheet

    # Buscar em Starships (Naves)
    starships = await fetch_swapi_data("starships", cleaned_query)
    if starships:
        starship = starships[0]
        sheet = f"**Ficha Técnica - {starship['name']}**\n"
        sheet += f"Nome: {starship['name']}\n"
        sheet += f"Modelo: {starship.get('model', 'Desconhecido')}\n"
        sheet += f"Fabricante: {starship.get('manufacturer', 'Desconhecido')}\n"
        sheet += f"Capacidade de Passageiros: {starship.get('passengers', 'Desconhecida')}\n"
        sheet += f"Velocidade: {starship.get('max_atmosphering_speed', 'Desconhecida')}\n"
        return sheet

    return "Desculpe, eu sou apenas um droid diplomata!"

# Função para identificar o nome e tipo na frase
def identify_name_and_type(query):
    # Exemplo de busca de padrões (isso pode ser refinado conforme necessário)
    keywords = {
        "people": ["luke", "leia", "han", "chewbacca", "darth", "yoda", "obi-wan"],
        "planet": ["tatooine", "endor", "dagobah", "coruscant", "hoth", "naboo", "jakku"],
        "starship": ["falcon", "death star", "x-wing", "tiefighter", "slave i"]
    }

    # Tenta identificar se o nome é de uma pessoa, planeta ou nave
    cleaned_query = ''.join([char for char in query.strip().lower() if char.isalnum() or char.isspace()])

    for category, names in keywords.items():
        for name in names:
            if name in cleaned_query:
                return name, category
    
    return None, None

# Função principal de busca (manter frases divertidas)
async def get_swapi_data(query):
    # Identificar o nome e tipo
    name, category = identify_name_and_type(query)
    if not name:
        return "Concordo plenamente com você!"

    # Buscar no tipo identificado
    data = await fetch_swapi_data(category, name)
    if category == "people" and data:
        person = data[0]
        response = random.choice(PEOPLE_RESPONSES).format(
            name=person["name"], info=person.get("gender", "um grande mistério")
        )
        return response

    if category == "planet" and data:
        planet = data[0]
        response = random.choice(PLANET_RESPONSES).format(
            name=planet["name"], info=planet.get("climate", "um clima intrigante")
        )
        return response

    if category == "starship" and data:
        starship = data[0]
        response = random.choice(STARSHIP_RESPONSES).format(
            name=starship["name"], info=starship.get("model", "um modelo não identificado")
        )
        return response

    return "Não sei se é bem assim!"
