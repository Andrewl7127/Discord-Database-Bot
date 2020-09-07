import discord
from discord.ext import commands
import asyncio
import datetime

class WelcomeCog(commands.Cog, name="Welcome"):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(color = 0x95efcc, description=f"Welcome to the server! You are member {len(list(member.guild.members))}`")
        



def setup(bot):
    bot.add_cog(WelcomeCog(bot))
    print("Welcome Cog is loaded")