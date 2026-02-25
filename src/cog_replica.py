import random
import discord
import asyncio
import time
import os
import re 
from datetime import datetime
from discord.ext import tasks, commands

call_pattern = "писе[ц|тс]|pisets"

#def bot_callable(bot, )

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
        else:
            msg_content = message.content
            matches = re.findall(call_pattern, msg_content, re.IGNORECASE)
            if matches != []:
                await message.channel.send('Some replica')