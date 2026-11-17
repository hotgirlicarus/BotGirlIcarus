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


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="say", 
        brief="make me repeat after you")
    async def cmd_say(self,
        ctx, 
        *, arg: str = commands.parameter( # "*, arg" means that all text after the prefix is considered one argument
            default="BEEP", # if no argument is given, fallback to "BEEP"
            description=": text you want me to say",
            displayed_default=None
        )):
        print(f'{ctx.author} asked me to say "{arg}"')
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(name="roll",
        aliases=["r"],
        brief="roll dice",
        description="roll dice! e.g. >roll 2d6 to roll a 6-sided die twice")
    async def cmd_roll(self,
        ctx,
        *, roll: str = commands.parameter(
            default="",
            description=": the dice you'd like to roll (e.g. 2d6 to roll a 6-sided die twice)",
            displayed_default=None
        ),):
        if roll == "":
            await ctx.send("NO ROLL PROVIDED")
            return

        # valid strings that can be dynamically used in written keys

        try:
            message = ""
            mod = int(0)
            roll = roll.replace(" ","")
            print(roll)

            if(roll.count("+")>0):
                roll = roll.split("+")
                mod = roll[1]
                mod = int(mod)
                roll = roll[0]

            roll = roll.split("d")
            print(roll)

            dice = roll[0] 
            dice = int(dice)
            sides = roll[1]
            sides = int(sides)
            total = int(0)

            loop_count = dice
            for loop in range(loop_count):
                current_roll = np.random.randint(1,sides)
                message += ("Roll " + str(loop + 1) + " = " + str(current_roll) + "\n" )
                total =  total + current_roll

            total = str(total + mod)

            message += ("Modifier: +" + str(mod) + "\n")
            await ctx.send(message + 'You have rolled ' + total)
        except:
            await ctx.send("oops make sure you've formatted correctly! (e.g. 2d6, 1d4+2, 3d8 + 1)")

    @commands.command(name="advice",
        brief="ask me for advice !!!!",
        description="ask me for advice !!  i'll do my best !!!")
    async def cmd_advice(self, ctx):
        print("i was asked for advice !")
        phrase = ""
        phrase_length = random.randint(1,2)
        for i in range(0,phrase_length):
            pre_verb = [
                "ALWAYS",       "NEVER",        "SOMETIMES",
                "MAYBE",        "YOU SHOULD",   "PLEASE",       "DON'T",
                "UH MAYBE DON'T"
            ]

            emphasis = [
                "SUPER",            "VERY",             "QUITE",            "REALLY"
            ]
            adjective = [
                "ODD",              "STUPID",           "WEIRD",            "BIG",
                "SMALL",            "FUNNY",            "WET",              "CLEAR",
                "SCARY",            "MYSTERIOUS",       "HUGE",             "WEIRD LITTLE",
                "LITTLE",           "LOUD",             "FUCKEN",
            ]

            verb = [
                "REMEMBER",         "RUN",              "BITE",             "BREAK",
                "SCREAM",           "SING",             "PLEASE",           "WRITE",
                "FORGET",           "SMELL",            "EAT",              "KILL",
                "LOVE",             "WIN",              "MOVE",             "CONSUME",
                "TOUCH",            "TAKE",             "BECOME",           "MAKE",
                "NOT",              "DO NOT",           "THROW",            "PAINT",
                "PROTECT",          "PICK UP",          "LOOK",             "SEE",
                "DO",               "ROMP",             "DANCE",            "TRY",
                "FUCK",             "KISS"
            ]

            preposition = random.choice([
                "AT ","ON ","IN ","WITH ","FOR ","TO " #"NEAR"
            ]) if random.randint(1,2) == 1 else ""
            noun_plural = random.choice([True, False])
            noun_suffix = f'{"S" if noun_plural else ""}'
            noun = [
                ("FISHIES" if noun_plural else "FISH"),     f"DOG{noun_suffix}",
                f"ROSE{noun_suffix}",                       f"THOUGHT{noun_suffix}",
                f"CAR{noun_suffix}",                        f"VESSEL{noun_suffix}",
                f"GAME{noun_suffix}"                        f"RACE{noun_suffix}",
                f"RABBIT{noun_suffix}",                     f"IDEA{noun_suffix}",
                f"HOUSE{noun_suffix}",                      f"BALL{noun_suffix}",
                ("CITIES" if noun_plural else "CITY"),      f"DINOSAUR{noun_suffix}",
                f"MOTH{noun_suffix}",                       f"CODE{noun_suffix}",
                f"DRAGON{noun_suffix}",                     f"BRICK{noun_suffix}",
                f"NEIGHBOR{noun_suffix}",                   f"STAR{noun_suffix}",
                f"CAN{noun_suffix}",                        f"OWL{noun_suffix}",
                f"ANIMAL{noun_suffix}",                     f"MOOSE{noun_suffix}",
                f"LIZARD{noun_suffix}",                     f"SKELETON{noun_suffix}",
                f"PLUSHIE{noun_suffix}",                    f"SONG{noun_suffix}",
                f"PIANO{noun_suffix}",                      f"BEAST{noun_suffix}",
                f"ROBOT{noun_suffix}",                      f"CAN{noun_suffix}",
                ("BIRDIES" if noun_plural else "BIRDY"),    ("TIDDIES" if noun_plural else "TITTY")
            ]
            selected_noun = random.choice(noun)
            selected_noun = ((random.choice(emphasis) + " " if random.randint(1,8) == 1 else "") + random.choice(adjective) + " " if random.randint(1,5) == 1 else "") + selected_noun
            end = [
                f'{preposition}{"" if noun_plural else ("AN " if selected_noun[0].lower() in ["a","e","i","o","u"] else "A ")}{selected_noun}',
                f'{preposition}{random.choice(["THESE", "THOSE"]) if noun_plural else random.choice(["THIS", "THAT"])} {selected_noun}',
                f'',
                f'{preposition}{random.choice(["HIM", "HER", "THEM", "IT", "ME", "YOURSELF"])}',
                f'{preposition}{random.choice(["YOUR", "THY"]) } {selected_noun}',
                f'TO {random.choice(verb)}'
            ]
            conjunction = [
                "AND",  "OR",   "BUT",  f"IF {random.choice(["YOU", "THEY"])}"
            ]

            phrase = phrase + (random.choice(pre_verb)+" " if random.randint(1,3)==3 else "")
            phrase = phrase + random.choice(verb) + " "
            phrase = phrase + random.choice(end) + " "
            if i < phrase_length - 1:
                phrase = phrase + random.choice(conjunction) + " "
        
        emoji = ["🎉","🎊","🀄","🃏","🐶","🐕","🦖","🐦‍🔥","🦎","🍀","🍂","🏁","🏳️‍⚧️","🏳️‍🌈","🫴","👍","😈","💞","❤️","⬆️","⚠️","🚫","☢️","✅","🫟","ℹ️","🦋","🫄","🪷",":)"]
        phrase = phrase + (random.choice(emoji) if random.randint(1,5)>3 else "")
        print(phrase)
        await ctx.send(phrase)
        print("done!\n")

    @commands.command(name="yt",
        aliases=["youtube"],
        brief="Pull the top youtube result")
    async def cmd_yt(self, ctx,
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
                query_string = urllib.parse.urlencode({'search_query': search})
                htm_content = urllib.request.urlopen(
                    'http://www.youtube.com/results?' + query_string)
                search_results = re.findall(r'/watch\?v=(.{11})',
                                            htm_content.read().decode())
                if len(search_results) == 0:
                    await ctx.send("No results :(")
                else:
                    await ctx.send(str('http://www.youtube.com/watch?v=' + search_results[0]))

    @commands.command(name="8ball",
        brief="ask the magic 8 ball",
        description="ask a yes or no question and the magic 8 ball will answer")
    async def cmd_8ball(self, ctx):
        phrase = ""
        answer = [
            "It is certain",       "It is decidedly so",        "Without a doubt",
            "Yes definitely",        "You may rely on it",   "As I see it, yes",       "Most likely",
            "Outlook good",         "Yes",          "Signs point to yes",
            "Reply hazy, try again",        "Ask again later",          "Better not tell you now",
            "Cannot predict now",           "Concentrate and ask again",        "Do not count on it",
            "My reply is no",       "My sources say no",           "Outlook not so good",
            "Very doubtful",        "Fuck no :/",       "HELL YEAH BROTHERRRRR",
        ]

            
        selected_answer = random.choice(answer)
            
        print(selected_answer)
        await ctx.send(selected_answer)

    @commands.command(name="dtdd",
        aliases=["doesthedogdie","tw","cw"],
        brief="pulls the link for Does The Dog Die",
        description="pulls the link for the media requested Does The Dog Die")
    async def cmd_dtdd(self, ctx,
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
                search = search.replace(" ", "%20")
                headers = {
                'X-API-KEY': 'ddd_f17000053a9cf9b606119849caab1c7a',
                }

                response = requests.get(('https://www.doesthedogdie.com/api/v3/items?q=' + search), headers=headers)
                response = response.json()

                dtdd_response = response[0]
                print(dtdd_response['id'])
                dtdd_id = str(dtdd_response['id'])
                await ctx.send("https://www.doesthedogdie.com/media/" + dtdd_id)

    @commands.command(name="define",
        aliases=["definition","def"],
        brief="pulls the definition of word",
        description="pulls the definition of the requested word from Merriam-Webster")
    async def cmd_define(self, ctx,
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
                response = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + search + "?key=c1001f88-14b7-45c6-aad9-7227a1e2cbdc")
                response = response.json()
                def_response = response[0]

                ID = str(def_response['meta']['id'])
                FL = str(def_response['fl'])
                shortdef = str(def_response['shortdef'])

                await ctx.send(ID + " - " + FL + "\n" + shortdef)
                
    @commands.command(name="thesaurus",
        aliases=["thes","synonym","syn","ant","antonym"],
        brief="pulls the synonyms and antonyms of word",
        description="pulls the synonyms and antonyms of the requested word from Merriam-Webster")
    async def cmd_define(self, ctx,
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
                response = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + search + "?key=c1001f88-14b7-45c6-aad9-7227a1e2cbdc")
                response = response.json()
                def_response = response[0]

                ID = str(def_response['meta']['id'])
                FL = str(def_response['fl'])
                shortdef = str(def_response['shortdef'])

                response = requests.get('https://dictionaryapi.com/api/v3/references/thesaurus/json/' + search + "?key=060f56e1-4053-49a7-8462-35de7c8238ce")
                response = response.json()
                def_response = response[0]

                # ID = str(def_response['meta']['id'])
                syns = str(def_response['meta']['syns'])
                ants = str(def_response['meta']['ants'])

                await ctx.send(ID + " - " + FL + "\n" + shortdef + "\n\nSynonyms: " + syns + "\n\nAntonyms: " + ants)

    @commands.command(name="choose",
        brief='Make bot choose for you! List options separated by commas',
        description='Indecisive? Make Bot choose for you')
    async def cmd_choose(self, ctx, *, choices):
        if "," in choices:
            choices = choices.replace(", ",",")
            splitter = ","
        else:
            splitter = " "
        choices = choices.split(splitter)
        await ctx.send(random.choice(choices))








async def setup(bot):
    await bot.add_cog(UserCommands(bot))
    print('attached cog "UserCommands"')
