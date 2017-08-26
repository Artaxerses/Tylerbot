# imports discord library and the commands
import discord
from discord.ext import commands
from random import randint

# Tyler Quotes
quotes = []

# Defines Bot, Bot prefix, and bot description
bot = commands.Bot(command_prefix = 'test$', description = 'Hopefully this works!')

# Bot event notifies users when it logs on
@bot.event
async def on_ready():
	print('Tylerbot has awakened')

@bot.command()
async def hello():
	await bot.say("Hello$")

@bot.command()
async def prime():
	listLength = len(quotes) 
	randomInteger = randint(0, listLength)
	await bot.say(quotes[randomInteger])

bot.run('MzUwMTI2MzEwMDk1MzIzMTM4.DH_h_g.jxUX0josU7SPHqBCZwb4N-yGSf8')

