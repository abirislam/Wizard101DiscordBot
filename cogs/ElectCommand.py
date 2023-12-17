import discord
from discord.ext import commands

class ElectCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ElectCommand.py is online.")

    @commands.command()
    async def elect(self, ctx):
        electEmbed = discord.Embed(title="Elect pet body", color=discord.Color.random())
        electEmbed.add_field(name="Elect pet body embed", value="Please see the image below for Elect's 'Hex Buff Variant' Universal Support Bases! \n\nThese Pets Pools were designed to allow you to create different variations of Universal Resistance, Healing and Support builds with Willcast Hex. Elect has supplied the Kiosk with copies of the body that have different manifests and will be refreshing them regularly. If you can't find any in the Kiosk, then they are all on cooldown and you can try again later. You can also look for the Sqnnet Pool that does not have Willcast Hex. \n\nPlease be on the lookout for future Full Pool projects by Elect and others and if you have a copy of this Full Pool, please consider putting it in the Kiosk for others!")

        file = discord.File("./images/elect.png", filename="elect.png")
        electEmbed.set_image(url="attachment://elect.png")

        await ctx.send(embed=electEmbed, file=file)


def setup(client):
    client.add_cog(ElectCommand(client))
    print("ElectCommand.py added")
