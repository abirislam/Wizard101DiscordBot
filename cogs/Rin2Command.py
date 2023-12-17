import discord
from discord.ext import commands

class Rin2Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("rin2Command.py is online.")

    @commands.command()
    async def rin2(self, ctx):
        rin2Embed = discord.Embed(title="Rin's Mega Piercer Variant Beguiled Gargoyles", color=discord.Color.random())
        rin2Embed.add_field(name="", value=
        "Please see the image below for Rin's Mega Piercer Variant Beguiled Gargoyles! These pets are copies of Rin's Piercer Variant Quetzals but on Mega Pets that have 5/10 Talents manifested as opposed to 2/10 on Adult Bases.\n\nRin has supplied the Kiosk with copies of each body and will be refreshing them regularly. If you can't find any in the Kiosk,  then they are all on cooldown and you can try again later.")

        file = discord.File("./images/rin2.png", filename="rin2.png")
        rin2Embed.set_image(url="attachment://rin2.png")

        await ctx.send(embed=rin2Embed, file=file)


def setup(client):
    client.add_cog(Rin2Command(client))
    print("Rin2Command.py added")
