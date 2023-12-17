import discord
from discord.ext import commands

class PsyCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("MontosoCommand.py is online.")

    @commands.command()
    async def psy(self, ctx):
        psyEmbed = discord.Embed(title="Psyduckian's Ward Pool Clockwork Paladins", color=discord.Color.random())
        psyEmbed.add_field(name="", value=
        "Please see the image below for Psyduckian's Ward Pool Universal Support Bases!\n\nThis Pool was designed by Psyduckian to allow you to create different variations of Universal and School Ward Pets. Psy has supplied the Kiosk with copies of the Adult Base on Clockwork Paladin's that have different manifests and will be refreshing them regularly.  If you can't find any in the Kiosk, then they are all on cooldown and you can try again later.\n\nMorpheus has also supplied the Kiosk with copies of the Pool on Mega Lord of Summer's for those looking for specific combinations of Manifested Talents. You can find all of Morph's Mega copies in the Pet Catalog under the Universal - Ward School Category.\n\nPlease be on the lookout for future Full Pool projects by Psyduckian and others and if you have a copy of this Full Pool, please consider putting it in the Kiosk for others!")

        file = discord.File("./images/psy.png", filename="psy.png")
        psyEmbed.set_image(url="attachment://psy.png")

        await ctx.send(embed=psyEmbed, file=file)


def setup(client):
    client.add_cog(PsyCommand(client))
    print("PsyCommand.py added")
