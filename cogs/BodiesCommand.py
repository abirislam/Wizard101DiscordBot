import discord
from discord.ext import commands

class BodiesCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("BodiesCommand.py is online.")
        
    @commands.command()
    async def bodies(self, ctx):
        bodiesEmbed = discord.Embed(title="All available pet bodies.", color=discord.Color.random())
        bodiesEmbed.add_field(name="!elect", value="Elect's Willcast Hex Utility Soulful Knights", inline=False)
        bodiesEmbed.add_field(name="!montoso", value="Montoso's Piercer Variant Beguiled Gargoyles", inline=False)
        bodiesEmbed.add_field(name="!montoso2", value="Montoso's Rounder Variant Dark Hounds", inline=False)
        bodiesEmbed.add_field(name="!psy", value="Psyduckian's Ward Pool Clockwork Paladins", inline=False)
        bodiesEmbed.add_field(name="!rin", value="Rin's Quint Damage Piercer Variant Quetzals", inline=False)
        bodiesEmbed.add_field(name="!rin2", value="Rin's Mega Piercer Variant Beguiled Gargoyles", inline=False)
        bodiesEmbed.add_field(name="!sqnnet", value="Sqnnet's Universal Support Soulful Knights", inline=False)
        bodiesEmbed.add_field(name="!chang", value="TheChang's & CustomPets9174's Universal Energy/Utility Detolli's Dragons", inline=False)

        await ctx.send(embed=bodiesEmbed)

def setup(client):
    client.add_cog(BodiesCommand(client))
    print("BodiesCommand.py added")
