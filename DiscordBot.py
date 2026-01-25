import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

@client.event
async def on_message(message):
    # evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("pong 🏓")

client.run(TOKEN)