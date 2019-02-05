import discord
from mcrcon import MCRcon
codes = ['§1','§2','§3','§4','§5','§6','§7','§8','§9','§c','§a','§f','§r']
from discord.ext import commands
import random
description = '''A bot to keep Admins connected on the go!'''
bot = commands.Bot(command_prefix='/', description=description)

IDs = ["<Admin user id>"]

mcr = MCRcon("<IP>","<Pass>")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def connect(ctx):
    '''Starts a rcon session'''
    if ctx.message.author.id in IDs:
        try:
            mcr.connect()
            await bot.say('Rcon connected')
        except:
            await bot.say('Connection Failed!')
    else:
        bot.say('Denied')
    
@bot.command()
async def disconnect():
    '''Closes the rcon connection'''
    if ctx.message.author.id in IDs:
        try:
            mcr.disconnect()
            await bot.say('Rcon disconnected!')
        except:
            await bot.say('Error!')
    else:
        await bot.say('Denied')
    
@bot.command(pass_context=True)
async def rcon(ctx, * comm : str):
    '''Sends commands to console'''
    comm = ' '.join(comm)
    fc = 0
    connected = True
    try:
        resp = mcr.command(comm)
    except:
        await bot.say('Rcon is not connected!')
    while connected:
        while fc != 13:
            resp = resp.replace(codes[fc], '')
            fc = fc + 1
        if ctx.message.author.id in IDs:
            await bot.say(resp)
            fc = 0
            connected = False
        else:
            print('Denied')
            connected = False

@bot.command(pass_context = True, hidden = True)
async def relog(ctx):
    '''Relogs The Bot'''
    if ctx.message.author.id not in IDs:
        await bot.say("INVALID")
        return
    else:
        await bot.say("Relogging...")
        await bot.logout()
            
if __name__ == '__main__':
    bot.run('<Bot_Token>')
