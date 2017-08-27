# imports discord library and the commands
import discord
from discord.ext import commands
from random import randint

# Tyler Quotes
quotes = ['idk I dont look at bills','if it means we get to kill some islams im all for it', 'I dont do handshakes >.>\n I dont want people to touch my hands', 'I hate black people, why would I do that (refers to handshake)','I dont shake hands. I dont like other people touching me', 'I love the burning feeling of eye drops', 'it feels like youre burning the allergens off your eyeball >.>', 'idk anyone who sits in economy', 'I have to civilize brown people who prefer dirt roads to paved','All I want is peace for the realm', 'and the middle class, of which I\' a part', 'tbh I\'m more interested in vic2 mp, it\'s not actually that shit considering I can be more racist','yes but we assimilated, unlike the sand niggers','trust me we have the money to fund a startup if we think the investment is lucrative', 'youd probably prefer to be a drone pilot to, that way you can kill civilians too -Ghost\nyeah probably - Tyler', 'no i would never vote for a muslim to hold public office\nNEVER','a bunch of my floormates were muslim last year -Ghost\nThat would be scary -Tyler', 'If this is how poor people feel I don\'t want to be poor','I sail and swim though\nam I going to get shit on for owning a boat >.>','and gays are freaks now -Ghost\nYes - Tyler', 'look im just saying the final solution is what id advocate for','im not racist','I\'m with these people and they are complaing about $175000 in lost assets\nso dumb\n its only 175000','I hate the left\nalways trying to get us to feel bad for not getting involved in domestic dispute in small countries like africa just fucking drop a bomb on them colonize and repurpose the territory',']

# Defines Bot, Bot prefix, and bot description
bot = commands.Bot(command_prefix = 'test$', description = 'Hopefully this works!')

# Bot event notifies users when it logs on
@bot.event
async def on_ready():
	print('Tylerbot has awakened')

@bot.command()
async def hello():
	await bot.say("Hey")

@bot.command()
async def prime():
	listLength = len(quotes) 
	randomInteger = randint(0, listLength)
	await bot.say('/tts' + quotes[randomInteger])

bot.run('MzUwMTI2MzEwMDk1MzIzMTM4.DH_h_g.jxUX0josU7SPHqBCZwb4N-yGSf8')

