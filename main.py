# imports discord library and the commands
import discord
from discord.ext import commands
from random import randint

# Defines Bot, Bot prefix, and bot description
bot = commands.Bot(command_prefix = '$', description = 'Hopefully this works!')

# Bot event notifies users when it logs on
@bot.event
async def on_ready():
	print('Tylerbot has awakened')

@bot.event
async def on_reaction_add(reaction, user):
    quote = reaction.message
    if reaction.emoji.name == 'Tyler' and reaction.count == 10:
        with open("quotes.txt", 'a') as quotefile:
            quotefile.writelines('\n'+quote.content)
        await bot.send_message(reaction.message.channel,'Quote "'+reaction.message.content+'" recorded!')

@bot.command()
async def hello():
	await bot.say("Hey")

@bot.command()
async def tyler():
    quotes = []
    index = 0
    with open("quotes.txt", 'r') as quotefile:
        for line in quotefile:
            quotes.append(line.strip())
        if (index == len(quotes)):
        	index = 0
    await bot.say(quotes[index])
    index += 1

bot.run('//insert key here)
