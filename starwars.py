import aiohttp
import random

SWAPI_BASE_URL = "https://swapi.dev/api/"

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

# Função para buscar na SWAPI
async def fetch_swapi_data(endpoint, search):
    url = f"{SWAPI_BASE_URL}{endpoint}/?search={search}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("results", [])
    return []

# Função principal de busca
async def get_swapi_data(query):
    query = query.lower()

    # Buscar em People
    people = await fetch_swapi_data("people", query)
    if people:
        person = people[0]
        response = random.choice(PEOPLE_RESPONSES).format(
            name=person["name"], info=person.get("gender", "um grande mistério")
        )
        return response

    # Buscar em Planets
    planets = await fetch_swapi_data("planets", query)
    if planets:
        planet = planets[0]
        response = random.choice(PLANET_RESPONSES).format(
            name=planet["name"], info=planet.get("climate", "muito peculiar")
        )
        return response

    # Buscar em Starships
    starships = await fetch_swapi_data("starships", query)
    if starships:
        starship = starships[0]
        response = random.choice(STARSHIP_RESPONSES).format(
            name=starship["name"], info=starship.get("model", "fascinante")
        )
        return response

    return "Desculpe, não encontrei nenhuma informação relevante."
