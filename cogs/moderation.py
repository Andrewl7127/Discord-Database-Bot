import discord
from discord.ext import commands
import asyncio
import datetime

class ModerationCog(commands.Cog, name="Moderator"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def purge(self, ctx, *, number:int=None):
        if ctx.message.author.guild_permissions.manage_messages:
            try: 
                if number is None:
                    await ctx.send("You must input a number")
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    await ctx.send(f'Messages purged by `{ctx.message.author}`: `{len(deleted)}`')
            except:
                await ctx.send('I cannot perform this purge command')
        else:
            await ctx.send("You do not have permissions to use this command")
        
    @commands.command()
    async def kick(self, ctx, user:discord.Member, *, reason=None):
        ctx.send("Sorry. This bot cannot be used to kick anyone")

    @commands.command()
    async def ban(self, ctx, user:discord.Member, *, reason=None):
        ctx.send("Sorry, this bot cannot be used to ban anyone")

def setup(bot):
    bot.add_cog(ModerationCog(bot))
    print("Moderation Cog is loaded")
