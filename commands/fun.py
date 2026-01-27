from discord.ext import commands
import requests

#Comandos para divertirse.
#No tiene un tema en específico.

class Apoyo(commands.Cog): #Comando !apoyo que tira apoyo.
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def apoyo(self, ctx):
        await ctx.send("APOYOOOOOOOO")
    
class Poke(commands.Cog):#Comando !poke que devuelve la imagen del Pokemon solicitado.
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poke(self,ctx,arg: str):
        try:
            pokemon = arg.lower()
            result = requests.get("https://pokeapi.co/api/v2/pokemon/"+ pokemon)
            if result.text == "Not Found":
                await ctx.send("Pokemon no encontrado")
            else:
                image_url = result.json()['sprites']['front_default']
                print(image_url)
                await ctx.send(image_url)

        except Exception as e:
            print("Error: ", e)

    async def cog_command_error(self, ctx, error):#Manda un mensaje cuando no se recibe un argumento obligatorio.
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Falta un argumento, boludazo")

async def setup(bot):
    await bot.add_cog(Poke(bot))
    await bot.add_cog(Apoyo(bot)) 