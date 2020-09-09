import discord
from discord.ext import commands
import asyncio
import datetime

class WelcomeCog(commands.Cog, name="Welcome"):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(title="Welcome to the Server!", description="For more information on the commands please use .help.")
        embed.add_field(name = "DB_Bot", value="This bot is used to store and retrive information from a database")
        embed.add_field(name = "Collections", value="Collections store your items. Each collection has certain categories.")
        embed.add_field(name = "Categories", value ="Categories are the specific fields of information that you want to collect.")
        embed.add_field(name = "Items", value = "Items are the specific pieces of information that you want to store. They have values corresponding to your collection's categories.")
        
        await member.send(embed = embed)


    
def setup(bot):
    bot.add_cog(WelcomeCog(bot))
    print("Welcome Cog is loaded")


"""

Description:

Welcome to the server!

This bot is used to store and retrieve information from a database. The bot works off of collections, categories, and items.

Collections store your items. Each collection has certain categories.

Categories are the specific fields of information that you want to collect.

Items are the specific pieces of information that you want to store. They have values corresponding to your collection's categories.

For more information on the commands please use .help.

"""