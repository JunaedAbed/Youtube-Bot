import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=".",intents = intents)
	
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} loaded!')
	
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} unloaded!')
	
@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} unloaded!')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} loaded!')
	
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')
	
@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount+1)
	
client.run(os.environ.get('BOT_TOKEN'))