import discord
from discord.ext import commands

class CatalogCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("spellementsCommand.py is online.")

    @commands.command()
    async def catalog(self, ctx):
        catalogEmbed = discord.Embed(title="Ferricord's Pet Catalog", color=discord.Color.random())
        catalogEmbed.add_field(name="", value=
        "You can find the Pet Catalog at the following link ⬇️\nhttps://tinyurl.com/FerricordPetCatalog")

        # file = discord.File("./images/spellements.png", filename="spellements.png")
        # spellementsEmbed.set_image(url="attachment://spellements.png")

        await ctx.send(embed=catalogEmbed)
                       #, file=file)


def setup(client):
    client.add_cog(CatalogCommand(client))
    print("CatalogCommand.py added")
