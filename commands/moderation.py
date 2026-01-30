from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)

    async def clear(self,ctx, amount: int): #Ingresar la cantidad de mensajes para borrar del chat.
        await ctx.channel.purge(limit=amount +1)


    @clear.error #Manejo de errores
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tenés que decirme cuántos mensajes querés que borre, capo.")
        if isinstance(error, commands.BadArgument):
            await ctx.send("EL número tiene que ser un entero.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tenés permitido hacer eso, maquina.")

async def setup(bot):
    await bot.add_cog(moderation(bot))