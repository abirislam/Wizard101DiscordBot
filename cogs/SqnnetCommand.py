import discord
from discord.ext import commands

class SqnnetCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("sqnnetCommand.py is online.")

    @commands.command()
    async def sqnnet(self, ctx):
        sqnnetEmbed = discord.Embed(title="Sqnnet's Universal Support Soulful Knights", color=discord.Color.random())
        sqnnetEmbed.add_field(name="", value=
        "Please see the image below for Sqnnet's Universal Support Bases! These Pets Pools were designed to allow you to create different variations of Universal Resistance, Healing and Support builds.\n\nSqnnet has supplied the Kiosk with 1 of each body and will be refreshing them regularly. If you can't find any in the Kiosk,  then they are all on cooldown and you can try again later.")

        file = discord.File("./images/sqnnet.png", filename="sqnnet.png")
        sqnnetEmbed.set_image(url="attachment://sqnnet.png")

        await ctx.send(embed=sqnnetEmbed, file=file)


def setup(client):
    client.add_cog(SqnnetCommand(client))
    print("SqnnetCommand.py added")
