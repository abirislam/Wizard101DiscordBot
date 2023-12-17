import discord
from discord.ext import commands

class MontosoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("MontosoCommand.py is online.")

    @commands.command()
    async def montoso(self, ctx):
        montosoEmbed = discord.Embed(title="Montoso's Piercer Variant Beguiled Gargoyles", color=discord.Color.random())
        montosoEmbed.add_field(name="", value=
        "Please see the image below for Montoso's Piercer Variant Beguiled Gargoyles.\n\nMontoso has Retired their copies of these Gargoyles as of April 15th 2023, however, you may still find copies of these Gargoyles in the Pet Kiosk made by other players. If you can't find any then either nobody is supplying them anymore or they are all on cooldown. You can also find Rin's version of the Piercer Pool by using the ?Rin Command.\n\nPlease be on the lookout for future Full Pool projects by Montoso and others and if you have a copy of these Gargoyles please consider putting then in the Kiosk for others!")

        file = discord.File("./images/montoso.png", filename="montoso.png")
        montosoEmbed.set_image(url="attachment://montoso.png")

        await ctx.send(embed=montosoEmbed, file=file)


def setup(client):
    client.add_cog(MontosoCommand(client))
    print("MontosoCommand.py added")
