import discord
import os
from discord.ext import commands
import asyncio
from discord.utils import get
import random

client = commands.Bot(command_prefix='+')
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


    

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
