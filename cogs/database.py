import discord
from discord.ext import commands
import asyncio
import datetime

class DatabaseCog(commands.Cog, name="Database"):
    def __init__(self, client):
        self.client = client




#create table

#add point 

#remove point 

# pull point by key


# pull x amount of points

# pull all points

# list tables 

# delete table 

# empty table 

# get table length 

#default table functionality 




##TODO: HELP COG FOR HELP MESSAGES 
  

def setup(bot):
    bot.add_DatabaseCog(bot)
    print("Moderation Cog is loaded")