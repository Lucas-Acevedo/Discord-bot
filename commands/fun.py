from bot import bot
from discord.ext import commands
import requests
#Comandos para divertirse.
#No tiene un tema en específico.

@bot.event
async def on_message(message):
    # evitar que el bot se responda a sí mismo
    if message.author.DiscordBot == bot.user:
        return

    if message.content == "!apoyo":
        await message.channel.send("APOYOOOOOO")

@bot.command() #Comando !poke que devuelve la imagen del Pokemon solicitado
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0] #Elimina espacios en el argumento recibido. Recibe únicamente el primer argumento.
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()['sprites']['front_default']
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error: ", e)

@poke.error #Mensaje de error si no se recibe ningún argumento
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Tenés que pasarme un Pokemon, maestro...")
