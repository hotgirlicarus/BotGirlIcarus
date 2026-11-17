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


class UtilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", 
        brief="check if i am responsive")
    async def cmd_ping(self, ctx):
        print("got pinged!") # this prints to the terminal, and is not seen from discord. its useful for logging
        await ctx.send("I AM FUNCTIONAL !") # this sends in the channel that the command was called in (ctx)

    @commands.command(name="time",
        aliases=["currenttime","clock","rn","now"],
        brief="what time is it?",
        description="check to see what time it is currently")
    async def cmd_time(self, 
        ctx):
        await ctx.send(dt.datetime.now().strftime("%G-%m-%d %I:%M %p"))




'''    @commands.command(name="help", 
        brief="sends this message :>",
        description="sends a list of available commands")
    async def cmd_help(self, ctx, *, cmdopt):
        cmdopt = cmdopt.replace(" ","")
        if cmdopt == "":
            await ctx.send('insert list of user commands here')
        elif cmdopt == "mod":
            async def check_any(self, ctx):
                return ctx.author.guild_permissions.manage_messages, ctx.author.guild_permissions.administrator
            async def command_error(self, ctx, error):
                await ctx.send(f"FUCK: {error}")
            await ctx.send('insert list of mod commands here')
        elif cmdopt == "admin":
            async def check(self, ctx):
                return ctx.author.guild_permissions.administrator
            async def command_error(self, ctx, error):
                await ctx.send(f"FUCK: {error}")
            await ctx.send('insert list of admin commands here')'''









async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
    print('attached cog "UtilityCommands"')
