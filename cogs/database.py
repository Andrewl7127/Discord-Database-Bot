import discord
from discord.ext import commands
import asyncio
import datetime
import cogs.config as config
import mysql.connector

class DatabaseCog(commands.Cog, name="Database"):
    def __init__(self, client):
        self.client = client
        self.mydb = mysql.connector.connect(
            host = config.sql_host,
            user = config.sql_username,
            password = config.sql_password,
            database = config.sql_database
        )
        try: 
            self.mycursor = self.mydb.cursor()
        except Exception as e:
             print("Exeception occured:{}".format(e))

        self.mycursor.execute('USE new_schema')

    #create a new table 
    @commands.command() 
    async def addCollection(self, ctx, *args):
        try: 
            command = 'CREATE TABLE '
            command += args[0] + ' ('
            for arg in args[1:]:
                command += arg + ' VARCHAR(255), '
            command = command[:-2]
            command += ')'
            self.mycursor.execute(command)
            await ctx.send(f"`{args[0]}` collection created succesfully with `{len(args)-1}` categorie(s)`")
        except Exception as e:
             print("Exeception occured:{}".format(e))
             await ctx.send("Unable to create table. Sorry :(")

    ##cadd a point to table 
    @commands.command()
    async def addPoint(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    #remove point 
    @commands.command()
    async def remove(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    #pull point by key
    @commands.command() 
    async def get(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")


    #pull x amount of points
    @commands.command() 
    async def getMany(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    #pull all points 
    @commands.command()
    async def getAll(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")
    
    #list all tables 
    @commands.command()
    async def getTables(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    # delete table
    @commands.command()
    async def deleteTable(self, ctx, arg):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    #empty table 
    @commands.command 
    async def delTable(self, ctx, arg):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    #get table length 
    @commands.command()
    async def tableLen(self, ctx, arg):
        ctx.send("FUNCTION NOT IMPLEMENTED")
    
    #alter table
    @commands.command()
    async def addCategory(self, ctx, *args):
        try:
            command = 'ALTER TABLE '
            command += args[0]
            for arg in args[1:]:
                command += ' ADD ' + arg + ' VARCHAR(255), '
            command = command[:-2]
            print(command)
            self.mycursor.execute(command)
            await ctx.send(f"Succesfully added `{len(args)-1}` categories` to `{args[0]}` collection")
        except Exception as e:
                print("Exeception occured:{}".format(e))
                await ctx.send("Unable to create table. Sorry :(")

    @commands.command()
    async def removeCategory(self, ctx, *args):
        try:
            command = 'ALTER TABLE '
            command += args[0]
            for arg in args[1:]:
                command += ' DROP ' + arg + ', '
            command = command[:-2]
            self.mycursor.execute(command)
            await ctx.send(f"Succesfully dropped `{len(args)-1}` categories` from `{args[0]}` collection")
        except Exception as e:
                print("Exeception occured:{}".format(e))
                await ctx.send("Unable to create table. Sorry :(")



#default table functionality 




##TODO: HELP COG FOR HELP MESSAGES 
  

def setup(bot):
    bot.add_cog(DatabaseCog(bot))
    print("Database Cog is loaded")
