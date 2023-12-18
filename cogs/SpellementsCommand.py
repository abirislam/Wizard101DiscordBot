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
        "Rank 1 Spellements - Make new characters and finish WC, you'll receive 75 rank 1 spellements from Abner K. Doodle\n\nNote: For rank 2-6 spellements you must **NOT** have completed Celestia on your character\n__**Rank 2-6 Elemental & Balance Spellements**__ - **Boris BlackRock** in the **Crucible, Dragonspyre**\n__**Rank 2-6 Spiritual & Balance Spellements**__ - **Vasek AshWeaver** in **Vault 1933, Grand Chasm, Dragonspyre**\n\nLoremaster spells now drop at the following gold key bosses:\n**Takanobu the Masterless** in **Cave of Solitude, Mooshu**\n**Drowned Dan** in **Science Center, Celestia**\n**Lambent Fire** in **Crystal Caves, Avalon**\n**Baron Von Bracken** in **Tanglewood Way, Wysteria**\n**Ixcax CursedWing** in **Three Points, Azteca**\n**High Loremagus** in the **Atheneum, Dragonspyre**\n**Lady Stonegaze** in **Garden of Hesperides, Aquila**\n**King Borr in Savarstaad Pass, Grizzleheim**\n**Spirit of Ignorance** in **Crab Alley**\n\nKaramelle, Lemuria, Novus, and Wallaru spellements I will add later")

        # file = discord.File("./images/spellements.png", filename="spellements.png")
        # spellementsEmbed.set_image(url="attachment://spellements.png")

        await ctx.send(embed=spellementsEmbed)
                       #, file=file)


def setup(client):
    client.add_cog(SpellementsCommand(client))
    print("SpellementsCommand.py added")
