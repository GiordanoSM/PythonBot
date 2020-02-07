import discord
from discord.ext import commands

import os

bot = commands.Bot(command_prefix='.')

@bot.event 
async def on_member_join(member):
    print(f'{member} has joined the server.')

@bot.event 
async def on_member_remove(member):
    print(f'{member} has left the server.')

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