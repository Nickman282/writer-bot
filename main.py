# Pisets Bot
# Application ID: 1475883749722816727
# Public Key: d7b771cfed8684b2a709762a340ae4e1ab20fa918f47eb3229f98f1af6c81457

import random
import discord
import asyncio
import time
import os
from datetime import datetime
from discord.ext import tasks
from dotenv import load_dotenv

from src.cog_replica import Replicas

# Load tokens

load_dotenv("./venv/tokens.env")

CHANNEL_ID = os.getenv('CHANNEL_ID')

if not isinstance(CHANNEL_ID, int):
    CHANNEL_ID = int(CHANNEL_ID)

BOT_TOKEN = os.getenv('BOT_TOKEN')



# Create Client class instance

intents = discord.Intents.default()
intents.message_content = True

client = discord.ext.commands.Bot(command_prefix = '', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Add a replica Cog
    replica = Replicas(client, CHANNEL_ID)
    await client.add_cog(replica)
    #custom_event.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

'''
@tasks.loop(seconds=5)
async def custom_event():
    # Get channel 
    message = client.get_channel(CHANNEL_ID)

    # Get timestamp
    ex = 'Tue Feb 24 22:38:00 2026'
    curr_time = time.time()
    if curr_time > time.mktime(time.strptime(ex)):
        await message.send(f'@everyone The time is {time.ctime(curr_time)}')
'''

client.run(BOT_TOKEN)

