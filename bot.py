import discord
from config import TOKEN, intents
from discord.ext import commands

#Este código es el encargado de inicializar el bot.

bot = commands.Bot(command_prefix='!',intents=intents)

#Mensaje en la terminal cuando el bot se conecte
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    
#Importar los comandos con Cog (todavía no sé que es)
bot.load_extension("commands.ping")

bot.run(TOKEN)