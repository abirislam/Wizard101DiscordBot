import discord
from discord.ext import commands

class SpellementsCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("spellementsCommand.py is online.")

    @commands.command()
    async def spellements(self, ctx):
        spellementsEmbed = discord.Embed(title="Blade's Spellement Farming Guide", color=discord.Color.random())
        spellementsEmbed.add_field(name="", value=
        "This embed is WIP, check back later!")

        # file = discord.File("./images/spellements.png", filename="spellements.png")
        # spellementsEmbed.set_image(url="attachment://spellements.png")

        await ctx.send(embed=spellementsEmbed)
                       #, file=file)


def setup(client):
    client.add_cog(SpellementsCommand(client))
    print("SpellementsCommand.py added")
