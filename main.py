import os
import discord
from discord import app_commands
from discord.ext import commands
import asyncio


client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is up and ready!")

def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded Cog: {filename[:-3]}")
setup_hook()

client.run(os.environ['BOT_TOKEN'])
