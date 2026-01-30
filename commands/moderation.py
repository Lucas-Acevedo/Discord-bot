from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)

    async def clear(sefl,ctx, amount: int): #Ingresar la cantidad de mensajes para borrar del chat. (14 es el máximo que permite la API)
        await ctx.channel.purge(limit=amount +1)

    async def clearall(self,ctx): #Borra todo lo que puede 
        await ctx.channel.purge()

    @clear.error #Manejo de errores
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tenés que decirme cuántos mensajes querés que borre, capo.")
        if isinstance(error, commands.BadArgument):
            await ctx.send("EL número tiene que ser un entero.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tenés permitido hacer eso, maquina.")