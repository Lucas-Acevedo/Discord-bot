import discord
import asyncio
from config import TOKEN, intents
from discord.ext import commands

#Este código es el encargado de inicializar el bot.

bot = commands.Bot(command_prefix='!',intents=intents)

#Mensaje en la terminal cuando el bot se conecte
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    
#Importar los comandos con Cog (todavía no sé que es)
async def main():
    async with bot: 
        await bot.load_extension("commands.ping")
        await bot.load_extension("commands.fun")
        await bot.start(TOKEN)

asyncio.run(main())