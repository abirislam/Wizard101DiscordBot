import discord
from discord.ext import commands

class Montoso2Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Montoso2Command.py is online.")

    @commands.command()
    async def montoso2(self, ctx):
        montoso2Embed = discord.Embed(title="Montoso's Rounder Variant Dark Hounds", color=discord.Color.random())
        montoso2Embed.add_field(name="", value=
        "Please see the image below for Montoso's Rounder Variant Dark Hounds! You may notice that these Full Pool Pets are pretty similar to the Piercer Variant Gargoyles and Quetzals, and that's because these pets are a brand new Full Pool project released by Montoso on May 15th to replace them!\n\nMontoso has supplied the Kiosk with 5 of each body and will be refreshing them regularly. If you can't find any in the Kiosk,  then they are all on cooldown and you can try again later.")

        file = discord.File("./images/montoso2.png", filename="montoso2.png")
        montoso2Embed.set_image(url="attachment://montoso2.png")

        await ctx.send(embed=montoso2Embed, file=file)


def setup(client):
    client.add_cog(Montoso2Command(client))
    print("Montoso2Command.py added")
