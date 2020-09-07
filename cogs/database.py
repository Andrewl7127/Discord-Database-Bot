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
        self.max_length = 20

    #create a new table 
    @commands.command() 
    async def addCollection(self, ctx, *args):
        try: 
            command = 'CREATE TABLE '
            command += args[0] + ' (ID int NOT NULL AUTO_INCREMENT, '
            for arg in args[1:]:
                command += arg + ' VARCHAR(255), '
            command = command[:-2]
            command += ', PRIMARY KEY (ID))'
            self.mycursor.execute(command)
            await ctx.send(f"`{args[0]}` collection created succesfully with `{len(args)}` categories`")
        except Exception as e:
             print("Exeception occured:{}".format(e))
             await ctx.send("Unable to create table. Sorry :(")

    #add a point to table 
    @commands.command()
    async def addItem(self, ctx, *args):
        try:
            self.mycursor.execute("SELECT count(*) FROM information_schema.columns WHERE table_name = " + "'" + args[0] + "'")
            num_col = self.mycursor.fetchall()[0][0] - 1
            try:
                if len(args) > 1 and (len(args)-1) % num_col == 0:
                    command = 'INSERT INTO ' + args[0] + ' VALUES '
                    if len(args) - 1 == 1:
                        command += "('', '" + args[1] + "')"
                    else:
                        if num_col == 1:
                            for arg in args[1:]:
                                command += "('', '" + arg + "'), "
                        else:
                            count = 1
                            for arg in args[1:]:
                                if count % num_col == 1:
                                    command += "('', '" + arg + "', "
                                elif count % num_col == 0:
                                    command += "'" + arg + "'), "
                                else:
                                    command += "'" + arg + "', "
                                count += 1
                        command = command[:-2] 
                    print (command)
                    self.mycursor.execute(command)
                    self.mydb.commit()
                    await ctx.send("Item(s) successfully added")
                elif len(args) == 1:
                    await ctx.send("You must pass in more than just the table name")
                else:
                    await ctx.send(f"You do not have the correct amount of arguments. The `{args[0]}` collection requires a multiple of `{num_col}` to place values. You currently have `{len(args)-1}` values")
            except Exception as e:
                await ctx.send(f"Adding to databse failed. This is likely not a user error")
                print("Exeception occured:{}".format(e))
        except Exception as e:
            await ctx.send(f"The `{args[0]}` collection does not exist")
            
    #removes all points 
    @commands.command()
    async def rmAllItems(self, ctx, arg):
        try:
            self.mycursor.execute('TRUNCATE TABLE ' + arg)
            self.mydb.commit()
            await ctx.send(f'All items have been successfully removed from the `{arg}` collection')
        except Exception as e:
             print("Exeception occured:{}".format(e))
             await ctx.send('The item(s) could not be deleted :(')

    
    

        

    #undo fucntion? (undoes last command)

    #alter point 
    @commands.command()
    async def updItem(self, ctx, *args):
        if len(args) >= 3:
            if len(args) % 2 == 1:
                await ctx.send('You need a table name and one value for every column')
            else:
                try:
                    command = 'UPDATE ' + args[0] + ' SET '
                    count = 1
                    for arg in args[2:]:
                        if count % 2 == 1:
                            command += arg + ' = '
                        else:
                            command += "'" + arg + "', "
                        count += 1
                    command = command[:-2]
                    command += ' WHERE ID = ' + args[1]
                    self.mycursor.execute(command)
                    self.mydb.commit()
                    await ctx.send(f'The item(s) have been successfully been updated in the `{args[0]}` collection')
                except Exception as e:
                    print("Exeception occured:{}".format(e))
                    await ctx.send('The item(s) could not be modified :(')
        else:
            await ctx.send('You need at least one column to modify')

    #pull point by key
    @commands.command() 
    async def get(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")


    #pull x amount of points
    @commands.command() 
    async def getMany(self, ctx, *args):
        ctx.send("FUNCTION NOT IMPLEMENTED")

    
    #list all tables 
    @commands.command()
    async def lstCol(self, ctx):
        try:
            self.mycursor.execute('SHOW TABLES')
            tables = self.mycursor.fetchall()
            msg = ''
            for table in tables:
                msg += table[0] + ', '
            await ctx.send('You have created the following collections: ' + msg[:-2])
        except Exception as e:
             print("Exeception occured:{}".format(e))
             await ctx.send('Could not list all collections :(')

    # delete table
    @commands.command()
    async def rmCollection(self, ctx, arg):
        try:
            self.mycursor.execute('DROP TABLE ' + arg)
            await ctx.send('The ' + arg + ' collection has successfully been removed')
        except Exception as e:
             print("Exeception occured:{}".format(e))
             await ctx.send('The collection could not be deleted :(')


    #list everything in a specified table 
    @commands.command()
    async def laTable(self, ctx, arg):
        command = "DESCRIBE " + arg
        try: 
            self.mycursor.execute(command)
            table = self.mycursor.fetchall()
            msg = ""
            for i in table:
                msg+=str(i[0]).ljust(self.max_length+6)
            msg+="\n"

            command = "SELECT * FROM " + arg
            self.mycursor.execute(command)
            table = self.mycursor.fetchall()
            for row in range(len(table)):
                for col in range(len (table[0])):
                    msg += str(table[row][col]).ljust(self.max_length+5)
                    msg += " "
                msg += "\n"  

        except Exception as e:
            print("Exeception occured:{}".format(e))
            await ctx.send('The table could not be retrieved')
    
        await ctx.send(msg)


    @commands.command()
    async def lsCat(self, ctx, arg):
        command = 'DESCRIBE ' + arg
        try:
            self.mycursor.execute(command)
            col = self.mycursor.fetchall()
            msg = ""
            for i in col:
                msg+=i[0] + ", "
            await ctx.send(f"The categories for the `{arg}` table are : '{msg[:-2]}`")
        except Exception as e:
            await ctx.send("Could not list. Check to make sure the table name is correct")
    
    #alter table
    @commands.command()
    async def addCat(self, ctx, *args):
        try:
            command = 'ALTER TABLE '
            command += args[0]
            for arg in args[1:]:
                command += ' ADD ' + arg + ' VARCHAR(255), '
            command = command[:-2]
            self.mycursor.execute(command)
            await ctx.send(f"Succesfully added `{len(args)-1}` categories` to `{args[0]}` collection")
        except Exception as e:
                print("Exeception occured:{}".format(e))
                await ctx.send("Unable to create table. Sorry :(")

    @commands.command()
    async def rmCat(self, ctx, *args):
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
