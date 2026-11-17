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


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.administrator
    async def cog_command_error(self, ctx, error):
        await ctx.send(f"FUCK: {error}")

    @commands.command(name="goodnight", 
        aliases=["goodbye","gn"],
        brief="puts me to sleep ⚠️ i will have to be restarted manually !!!",
        hidden=True)
    async def cmd_goodnight(self, ctx):
        await ctx.send("OK GOODNIGHT !")
        await self.bot.close() # this stops the bot entirely. BEe careful with this

    @commands.command(name="id", 
        brief="get discord id",
        hidden=True)
    async def cmd_id(self, ctx):
        print("got pinged!") # this prints to the terminal, and is not seen from discord. its useful for logging
        print(f"Your ID: {ctx.author.id}")








async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
    print('attached cog "AdminCommands"')
