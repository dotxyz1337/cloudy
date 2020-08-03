import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
  print('Bot is ready!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! 🏓 {round(client.latency * 1000)}ms')

@client.command()
async def purge(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

@client.command()
async def dancepls(ctx):
  await ctx.send('🕺')

@client.command()
async def owo(ctx):
  await ctx.send('uwu :heart:')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('Kicked :heart:')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send('Banned :heart:')

client.run(os.environ['TOKEN'])
