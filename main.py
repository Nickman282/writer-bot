# Johnny Bot

import random
import discord
import asyncio
import time
import os
from datetime import datetime
from discord.ext import tasks
from dotenv import load_dotenv

from src.cog_replica import Replicas, bot_callable

# Load tokens

load_dotenv("./venv/tokens.env")

CHANNEL_ID = os.getenv('CHANNEL_ID')

if not isinstance(CHANNEL_ID, int):
    CHANNEL_ID = int(CHANNEL_ID)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create Bot class instance, initialize on_ready coroutine, run

intents = discord.Intents.default()
intents.message_content = True

client = discord.ext.commands.Bot(command_prefix = bot_callable, intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Add a replica Cog
    replica = Replicas(client, CHANNEL_ID)
    await client.add_cog(replica)

client.run(BOT_TOKEN)

