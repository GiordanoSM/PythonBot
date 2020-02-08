import discord
from discord.ext import commands

import json
import os

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f: #le do arquivo
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.' #adiciona prefixo do server

    with open('prefixes.json', 'w') as f: #escreve no arquivo
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f: #le do arquivo
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #remove prefixo do server

    with open('prefixes.json', 'w') as f: #escreve no arquivo
        json.dump(prefixes, f, indent=4)

@bot.event 
async def on_member_join(member):
    print(f'{member} has joined the server.')

@bot.event 
async def on_member_remove(member):
    print(f'{member} has left the server.')

@bot.command(aliases=['pf'])
async def change_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f: #le do arquivo
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix #modifica prefixo do server

    with open('prefixes.json', 'w') as f: #escreve no arquivo
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}') #cogs=nome da pasta

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}') #cogs=nome da pasta

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}') #cogs=nome da pasta
    bot.load_extension(f'cogs.{extension}') #cogs=nome da pasta

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #removendo .py da string

bot.run(os.environ['BOTTOKEN'])