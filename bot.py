import discord
from discord.ext import commands

TOKEN = 'MzQ3MDA2NDk5Njc3MTQzMDQx.DHSGgQ.QjWW-IBOR1DJcqfADTthpr1Eavc'

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
	print('REady')

@bot.command()
async def test(ctx):
	await ctx.send('Working!')

bot.run(TOKEN)