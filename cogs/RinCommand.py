import discord
from discord.ext import commands

class RinCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("rinCommand.py is online.")

    @commands.command()
    async def rin(self, ctx):
        rinEmbed = discord.Embed(title="Rin's Piercer Variant Quetzals", color=discord.Color.random())
        rinEmbed.add_field(name="", value=
        "Please see the image below for Rin's Piercer Variant Quetzals! These pets are copies of Montoso's Piercer Variant Full Pool but on school-coordinated bodies to help make tracking them easier.\n\nRin has supplied the Kiosk with 5 of each body and will be refreshing them regularly. If you can't find any in the Kiosk,  then they are all on cooldown and you can try again later.")

        file = discord.File("./images/rin.png", filename="rin.png")
        rinEmbed.set_image(url="attachment://rin.png")

        await ctx.send(embed=rinEmbed, file=file)


def setup(client):
    client.add_cog(RinCommand(client))
    print("RinCommand.py added")
