import discord
import config
from discord.ext import commands
from datetime import datetime
import asyncio


client  = commands.Bot(command_prefix = ".", case_insensitive = "true")

@client.event
async def on_ready():
    print("Bot ready")

@client.event
async def on_member_join(member):
    embed = discord.Embed(color = discord.Color(0x95efcc), description="Welcome to the server!" +
    "you are the {} member", timestamp=datetime.datetime.utcfromtimestamp(1553629094))


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(config.bot_key)

