import discord
from discord.ext import commands, tasks
from itertools import cycle

import random

class Example(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.games = cycle(['Mundo da lua', 'LoLzin'])

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is ready.')
    await self.change_status.start()

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'pong {round(self.bot.latency*1000)} ms')

  @commands.command()
  async def clear(self, ctx, amount=50):
    await ctx.channel.purge(limit=amount)

  @commands.command(aliases=['8ball', 'rand'])
  async def _8ball(self, ctx, *, question):
    responses = ['Sim.', "Não, mas o Zedu sim.", 'Talvez.']
    await ctx.send(f'{random.choice(responses)}')

  @tasks.loop(seconds=10)
  async def change_status(self):
    await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(next(self.games)))


def setup(bot):
  bot.add_cog(Example(bot))