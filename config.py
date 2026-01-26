import os
import discord
from dotenv import load_dotenv

#Todo lo "sensible" se guarda acá

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True