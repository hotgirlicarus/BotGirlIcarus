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

bot = commands.Bot(
    command_prefix=[">", "<@[[BOT_ID]]>"], #change these to wahtever you like
    intents=intents,
    strip_after_prefix=True,
    #help_command=None
)

@bot.event
async def on_ready():
    channel = bot.get_channel([[CHANNEL]]) 
    await channel.send("beep boop")



    await bot.load_extension("cogs.admincmds")
    #await bot.load_extension("cogs.modcmds")
    await bot.load_extension("cogs.usercmds")
    await bot.load_extension("cogs.utilitycmds")
    await bot.load_extension("cogs.secretcmds")








# everything below this line is still in progress
"""
@bot.command(name="todo",
    brief="Get yer task list")
async def cmd_todo(ctx, *, arg = ""):
    if arg == "":
            # reading
        print("reading json...", end="")
        data=None
        try:
            with open("document.json", "r+") as f:
                data = json.load(f)
                print("success!!")
        except:
            print("OOPS!!!\nsomething went wrong!\nwhatever it is, we'll just overwrite document.json instead")
            data = {}
        finally:
            try:
                text = ""
                for index, item in enumerate(["a","b","c"], start=1):
                    text = f"{text}{index}. {item}\n"
                await ctx.send(text)
                # mylist=["bla"]
                # mylist.pop(1)

            except:
                await ctx.send("you have no tasks !! yet :)")
    else:
        data=None
        try:
            with open("document.json", "r+") as f:
                data = json.load(f)
                print("success!!")
        except:
            print("OOPS!!!\nsomething went wrong!\nwhatever it is, we'll just overwrite document.json instead")
            data = {}
        finally:
            # await ctx.send(data)
            pass

            # writing
        print("writing to json...")
        id = str(ctx.author.id)
        print(f"your discordly assigned ID is: {id}")

        data.update({id: arg})

        # then, finally, dump it into document.json
        with open("document.json", "w") as f:
            json.dump(data, f)

        print("now the json looks like this:")
        pprint(data)



@bot.command(name="spotify",
    brief="Pull the top Spotify result")
async def cmd_spotify(ctx,
    *, search: str = commands.parameter(
        default="",
        description=": search query",
        displayed_default=None
        ),
    ):
        if search == "":
            await ctx.send("NO SEARCH TERMS PROVIDED")
            return

        else:
           
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="[[CLIENT_ID]]",
                                               client_secret="[[CLIENT_SECRET]]",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope="user-library-read"))

            result = sp.search(q=search, limit=1, offset=0)
            print(result)
            for idx, track in enumerate(result['tracks']['items']):
                print(track['artists'][0]['name'], " – ", track['name'], track['external_urls']['spotify'])
            
                await ctx.send(track['artists'][0]['name'] + " – " + track['name'])
                await ctx.send(track['external_urls']['spotify'] + "/")


class HelpCommand(commands.HelpCommand):
    def __init__(self, bot):
        self.bot = bot
    bot.get_command()
    


"""









bot.run("[[KEY]]")
