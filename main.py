import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from conversation import handle_greetings
from starwars import get_swapi_data

# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuração do bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Habilitar a leitura do conteúdo das mensagens
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento: Bot está pronto
@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

# Evento: Mensagem recebida
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Verifica se a mensagem é uma saudação e responde
    response = handle_greetings(message.content)
    if response:
        await message.channel.send(response)
        return  # Impede que o bot processe outros comandos após uma saudação

    # Agora, busca por informações na SWAPI com base na mensagem atual
    response = await get_swapi_data(message.content)
    if response:  # Verifica se houve correspondência na SWAPI
        await message.channel.send(response)
        return

    # Se não for uma saudação nem um termo da SWAPI, continua com outros comandos
    await bot.process_commands(message)

# Rodar o bot
if __name__ == "__main__":
    bot.run(TOKEN)
