'''
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |
'''

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import os
import config

import sys, traceback


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = [',']


    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# cogs
async def load():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"cogs.{name}")

bot = commands.Bot(command_prefix=get_prefix, description='meow')



# Bot Connect

@bot.event
async def on_ready():
    await load()
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\ncode by wiiired')


# Txt Logs open
@bot.event
async def on_message(message):
    file1 = open("logs.txt", "a") # Open or create the logs file
    file1.write(f'Message: {message.content} | Sent by: {str(message.author)}, at {message.created_at}, in #{message.channel.name}') #Log content
    file1.write("\n") # Separate between lines
    file1.close() 

# Bot token
bot.run("TOKEN HERE OWO", bot=True, reconnect=True)