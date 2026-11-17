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

"""
class ModCommands(commands.Cog):
        def __init__(self, bot):
        self.bot = bot
    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.manage_messages
    async def cog_command_error(self, ctx, error):
        await ctx.send(f"FUCK: {error}")



"""




async def setup(bot):
    await bot.add_cog(ModCommands(bot))
    print('attached cog "ModCommands"')
