import discord
from discord.ext import commands

class ChangCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("changCommand.py is online.")

    @commands.command()
    async def chang(self, ctx):
        changEmbed = discord.Embed(title="TheChang's & CustomPets9174's Universal Energy/Utility Bases", color=discord.Color.random())
        changEmbed.add_field(name="", value=
        "Please see the image below for TheChang's & CustomPets9174's Universal Energy/Utility Bases! These Pets Pools were designed to allow you to create different variations of Maximum Energy, Fishing Luck and School Retriever or Scout builds to best suit your individual needs.\n\nTheChang & Custom have supplied the Kiosk with 2 of each body and will be refreshing them regularly. If you can't find any in the Kiosk,  then they are all on cooldown and you can try again later.")

        file = discord.File("./images/chang.png", filename="chang.png")
        changEmbed.set_image(url="attachment://chang.png")

        await ctx.send(embed=changEmbed, file=file)


def setup(client):
    client.add_cog(ChangCommand(client))
    print("ChangCommand.py added")
