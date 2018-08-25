# imports discord library and the commands
import discord
from discord.ext import commands
from random import randint

# Defines Bot, Bot prefix, and bot description
bot = commands.Bot(command_prefix = '$', description = 'Hopefully this works!')

# Bot event notifies users when it logs on
@bot.event
async def on_ready():
        await bot.change_presence(game=discord.Game(name='Diplomacy'))
        await bot.send_message(bot.get_channel('336262010033405952'), 'Tylerbot has awakened')

@bot.event
async def on_reaction_add(reaction, user):
        if reaction.emoji == '\N{THUMBS UP SIGN}' and reaction.count == 8:
                message = reaction.message.content.split('"')[1]
                with open("quotes.txt", 'a') as quotefile:
                        quotefile.writelines('\n'+message)
                await bot.send_message(reaction.message.channel,'Quote "'+message+'" recorded!')
                await bot.delete_message(reaction.message)
        try:
                if reaction.emoji.name == 'Tyler' and reaction.count == 1:
                        polling = bot.get_channel('344566152535474186')
                        general = bot.get_channel('335560493454327808')
                        bot_chat = bot.get_channel('336262010033405952')
                        await bot.send_message(general, 'Voting for "'+reaction.message.content+'" has begun in '+polling.mention)
                        message = await bot.send_message(polling, 'Emoji this to add it to quotes (we need 8): "'+reaction.message.content+'"')
                        await bot.add_reaction(message, '\N{THUMBS UP SIGN}')
        except:
                pass
@bot.command()
async def hello():
    await bot.say("Hey")

@bot.command()
async def tylerdanh(arg):
    quotes = []
    with open("quotes.txt", 'r') as quotefile:
        for line in quotefile:
            quotes.append(line.strip())
    await bot.say(quotes[arg])

@bot.command()
async def tyler():
    quotes = []
    with open("quotes.txt", 'r') as quotefile:
        for line in quotefile:
            quotes.append(line.strip())
    await bot.say(quotes[randint(0, len(quotes)-1)])

@bot.command(pass_context = True)
async def shutdown(ctx):
    if ctx.message.author.id == '196866248984887296':
        await bot.send_message(bot.get_channel('336262010033405952'), 'i gotta throw my croissants in the oven')
        await bot.close()
    else:
        await bot.say('That sounds like a threat!')

bot.run('super secret token here')

