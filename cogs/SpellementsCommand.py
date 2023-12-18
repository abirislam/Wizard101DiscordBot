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
        spellementsEmbed.add_field(name="This is the best way to farm spellements as of December 2023", value=
        "Rank 1 Spellements - Make new characters and finish WC, you'll receive 75 rank 1 spellements from Abner K. Doodle\n\nNote: For rank 2-6 spellements you MUST not have completed Celestia on your character\nRank 2-6 Elemental & Balance Spellements - Boris BlackRock in the Crucible, Dragonspyre\nRank 2-6 Spiritual & Balance Spellements - Vasek AshWeaver in Vault 1933, Grand Chasm, Dragonspyre\n\nLoremaster spells now drop at the following gold key bosses:\nTakanobu the Masterless in Cave of Solitude, Mooshu\nDrowned Dan in Science Center, Celestia\nLambent Fire in Crystal Caves, Avalon\nBaron Von Bracken in Tanglewood Way, Wysteria\nIxcax CursedWing in Three Points, Azteca\nHigh Loremagus in the Atheneum, Dragonspyre\nLady Stonegaze in Garden of Hesperides, Aquila\nKing Borr in Savarstaad Pass, Grizzleheim\nSpirit of Ignorance, Crab Alley\n\nKaramelle, Lemuria, Novus, and Wallaru spellements I will add later")

        # file = discord.File("./images/spellements.png", filename="spellements.png")
        # spellementsEmbed.set_image(url="attachment://spellements.png")

        await ctx.send(embed=spellementsEmbed)
                       #, file=file)


def setup(client):
    client.add_cog(SpellementsCommand(client))
    print("SpellementsCommand.py added")
