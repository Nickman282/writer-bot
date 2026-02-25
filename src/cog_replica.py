import random
import discord
import asyncio
import time
import os
import re 
import random
from datetime import datetime
from discord.ext import tasks, commands

#call_pattern = "писе[ц|тс]|pisets"

# Define a call pattern for the bot (case-insensitive)
call_pattern = ".*жонни|johnny"
user_pattern = "#User#"
specuser_pattern = "#SpecUser#"

# Load in replicas
path = f"{os.getcwd()}/Data/johnny_quotes.txt"
list_of_replicas = []
with open(path, 'r') as f:
    for line in f:
        list_of_replicas.append(line)

# Callabale function used to define if bot should respond to message
def bot_callable(bot, message):
    msg_content = message.content
    matches = re.findall(call_pattern, msg_content, re.IGNORECASE)
    if matches != []:
        command_prefix = f'{msg_content.split(' ')[0]}'
    else:
        command_prefix = call_pattern
    return command_prefix

class Replicas(commands.Cog):

    def __init__(self, bot, channel):
        self.bot = bot

        if isinstance(channel, int):
            self.channel = channel
        else:
            try:
                self.channel = int(channel)
            except:
                raise TypeError("Only integers are allowed") 
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        elif message.channel.id == self.channel:
            msg_content = message.content
            matches = re.findall(call_pattern, msg_content, re.IGNORECASE)
            if matches != []:
                # Select a random replica
                rand_index = random.randint(0, len(list_of_replicas)-1)
                replica = list_of_replicas[rand_index]

                # Check if quote contains user_pattern
                user_matches = re.findall(user_pattern, replica, re.IGNORECASE)
                if user_matches != []:
                    author = message.author.id # Get "Member" instance, then the name string from it
                    replica = replica.replace(user_pattern, f'<@{author}>')

                # Check if quote contains specuser_pattern
                specuser_matches = re.findall(specuser_pattern, replica, re.IGNORECASE)
                if specuser_matches != []:
                    spec_author = message.author.guild.owner_id # Get "Member" instance, then "Guild", then its owner
                    replica = replica.replace(specuser_pattern, f'<@{spec_author}>')
                
                await message.channel.send(replica)