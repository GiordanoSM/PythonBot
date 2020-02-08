import discord
from discord.ext import commands, tasks
from itertools import cycle

import random

def checking_user(ctx):
    return ctx.author.id == 258346280374370304

class Example(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.games = cycle(['Mundo da lua', 'LoLzin'])

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is ready.')
    await self.change_status.start()

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please pass in all required arguments.')

    elif isinstance(error, commands.CommandNotFound):
      await ctx.send('Comando não existente.')

    elif isinstance(error, commands.MissingPermissions):
      await ctx.send('Sem permissoes suficientes.')

  @commands.command()
  @commands.check(checking_user)
  async def ping(self, ctx):
    await ctx.send(f'Toma pong {ctx.author} {round(self.bot.latency*1000)} ms')

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount : int):
    await ctx.channel.purge(limit=amount)

  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Diga quantas mensagens devem ser deletadas.')

  @commands.command(aliases=['8ball', 'rand'])
  async def _8ball(self, ctx, *, question):
    responses = ['Sim.', "Não, mas o Zedu sim.", 'Talvez.']
    await ctx.send(f'{random.choice(responses)}')

  @tasks.loop(seconds=10)
  async def change_status(self):
    await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(next(self.games)))


def setup(bot):
  bot.add_cog(Example(bot))