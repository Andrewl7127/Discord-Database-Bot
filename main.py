import discord
import config
from discord.ext import commands
from datetime import datetime
import asyncio
import sys
import traceback


client  = commands.Bot(command_prefix = ".", case_insensitive = "true")

@client.event
async def on_ready():
    print("Bot ready")

initial_extensions = ['cogs.moderation']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Extension Load Failed: `{extension}`', file=sys.stderr)
            traceback.print_exc()

@client.event
async def on_member_join(member):
    embed = discord.Embed(color = 0x95efcc, description=f"Welcome to the server! You are member {len(list(member.guild.members))}`")
    embed.timestamp = datetime.datetime.utcnow()


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(config.bot_key)

