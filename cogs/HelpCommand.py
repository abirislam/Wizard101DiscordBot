import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand.py is online.")

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title="Here is a list of commands.", color=discord.Color.random())
        helpEmbed.add_field(name="!bodies", value="View all pet bodies; the pet body commands won't be listed here", inline=False)
        helpEmbed.add_field(name="!catalog", value="View Ferricord's pet catalog", inline=False)
        helpEmbed.add_field(name="!spellements", value="View spellements guide", inline=False)

        await ctx.send(embed=helpEmbed)

def setup(client):
    client.remove_command('help')
    client.add_cog(HelpCommand(client))
    print("HelpCommand.py added")
