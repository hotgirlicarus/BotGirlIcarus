import discord
import numpy as np
import datetime as dt
import random
import json
import requests
from pprint import pprint # this just makes printed data look more beautiful and readable, heehee


from discord.ext import commands

from discord.utils import get
import urllib.parse, urllib.request, re

import spotipy
from spotipy.oauth2 import SpotifyOAuth

intents = discord.Intents.default()
intents.message_content = True # this lets the bot read message text. i dont think you need this actually feel free to comment it out ??


###


class SecretCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.lower() == "wow":
            await message.channel.send("https://tenor.com/bkl7VKqN0ck.gif")
        elif message.content.lower() == "uwu":
            await message.channel.send("https://cdn.discordapp.com/emojis/709853411134406702.webp?size=96&animated=true")
        #await self.process_commands(message)








async def setup(bot):
    await bot.add_cog(SecretCommands(bot))
    print('attached cog "SecretCommands"')
