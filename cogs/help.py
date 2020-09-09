import discord
from discord.ext import commands
import asyncio
import datetime

class HelpCog(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == ".help":
            embed = discord.Embed(title="Help Page", description="This is the documentation for the bot.") #,color=Hex code
             
            embed.add_field(name='.addCollection "collection name" "category name..."', value= 'Creates a new collection. Requires 1 collection name' + 
                                                'and at least 1 category name (all collections are automatically created with a unique ID category).\n \n Ex. .addCollection Waypoints')
            
            embed.add_field(name='.lsCollection', value="Lists all the collection(s). Requires nothing\n \n Ex. .allCollectionsMultiple\n\n Ex. .getItem Waypoints Name House X-Coordinate 30")
            
            embed.add_field(name='.rmCollection "collection name"', value="Deletes the collection. Requires 1 collection name.\n\n" + 
                                                                "Ex. .rmCollection Waypoints")
                                                                
            embed.add_field(name= '.addCat "collection name" "category name..."', value="Adds a new category to the collection" + 
                                    "Requires 1 collection name and at least 1 category name. \n\n" +     
                                    "Singular Ex. .addCat Waypoints X-Coordinate \n\n" + "Multiple Ex. .addCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate") 

            embed.add_field(name= '.lsCat "collection name"' ,value="Lists all categories in the collection. Requires 1 collection name.\n\n" + 
                                                            "Ex. .lsCat Waypoints")
            
            embed.add_field(name= '.rmCat "collection name" "category name..."', value="Removes category/categories from the collection. Requires 1 collection name"  + 
                                                                        "and at least 1 category name (not recommended to remove the ID category).\n\n" + "Singular Ex. .rmCat Waypoints X-Coordinate\n" + 
                                                                        "Multiple Ex. .rmCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate")
            
            embed.add_field(name= '.addItem "collection name" "Category Value..."', value="Adds item(s) to the collection. Requires 1 collection name and 1" + 
                                                                        "category value for each category in the collection (excluding unique ID) for each item" + 
                                                                        "you are trying to add.\n\n Singular Ex. .addItem Waypoints House 30 30 30" + 
                                                                        "Multiple Ex. addItem Waypoints House 30 30 30 Farm 40 40 40")

            embed.add_field(name=' .lsItem "collection name"', value="Gets all item(s) from the collection. Requires 1 collection name\n\n Ex. .getAll Waypoints")

            embed.add_field(name='.findItem "collection name" "category name" "category value"', value="Finds item(s) that meet certain search critera from the collection" +  
                                                                "Requires 1 collection name and at least 1 category name and corresponding category value.\n" +
                                                                "Singular Ex. .findItem Waypoints Name House\n\n" + "Multiple Ex. .findItem Waypoints Name House X-Coordinate 30")

            embed.add_field(name='.updItem "collection name" "ID" "category name..." "category value..."', value="Updates the category value(s) for specific item. Requires 1" +
                                                                "collection name and at least 1 category name and corresponding category value. To find the ID, please use findItem.\n\n" + 
                                                                "Singular Ex. .updItem Waypoints 1 X-Coordinate 35\n\n" + "Multiple Ex. .updItem Waypoints 1 X-Coordinate 35 Y-Coordinate 35")
            
            embed.add_field(name= '.rmItem "collection name" "ID"', value="Removes item(s) at the specified IDs. Requires 1 collection name and 1 ID for each" +
                                                                        "item you are trying to remove. To find the ID, please use findItem.\n\n" + "Singular Ex. .rmItem Waypoints 1\n\n"
                                                                        + "Multiple Ex. .rmItem Waypoints 1 3 5 7")
                                                        
            embed.add_field(name='.clearItem "collection name"', value="Removes all item(s) in the collection. Requires 1 collection name.\n\n" + "Ex. .clearItem Waypoints")
                                                 
                                    
            await message.author.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(HelpCog(bot))
    print("Help Cog is loaded")

"""
Commands:

.addCollection "collection name" "category name..."
Creates a new collection. Requires 1 collection name and at least 1 category name (all collections are automatically created with a unique ID category).
Ex. .addCollection Waypoints Name

.lsCollection
Lists all the collections. Requires nothing.
Ex. .getItem Waypoints Name House X-Coordinate 30

.rmCollection "collection name"
Deletes the collection. Requires 1 collection name.
Ex. .rmCollection Waypoints

.addCat "collection name" "category name..."
Adds a new category to the collection. Requires 1 collection name and at least 1 category name.
Singular Ex. .addCat Waypoints X-Coordinate
Multiple Ex. .addCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate

.lsCat "collection name"
Lists all categories in the collection. Requires 1 collection name.
Ex. .lsCat Waypoints

.rmCat "collection name" "category name..."
Removes a category from the collection. Requires 1 collection name and at least 1 category name (not recommended to remove ID category).
Singular Ex. .rmCat Waypoints X-Coordinate
Multiple Ex. .rmCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate

.addItem "collection name" "Category Value..."
Adds item(s) to the collection. Requires 1 collection name and 1 category value for each category in the collection (excluding unique ID) for each item you are trying to add.
Singular Ex. .addItem Waypoints House 30 30 30
Multiple Ex. addItem Waypoints House 30 30 30 Farm 40 40 40

.lsItem "collection name"
Gets all items from the collection. Requires 1 collection name
Ex. .getAll Waypoints

.findItem "collection name" "category name" "category value"
Finds item(s) that meet certain search critera from the collection. Requires 1 collection name and at least 1 category name and corresponding category value.
Singular Ex. .getItem Waypoints Name House
Multiple Ex. .getItem Waypoints Name House X-Coordinate 30


.updItem "collection name" "ID" "category name..." "category value..."
Updates the category value(s) for specific item. Requires 1 collection name and at least 1 category name and corresponding category value. To find the ID, please use .findItem.
Singular Ex. .updItem Waypoints 1 X-Coordinate 35
Multiple Ex. .updItem Waypoints 1 X-Coordinate 35 Y-Coordinate 35

.rmItem "collection name" "ID"
Removes item(s) at the specified IDs. Requires 1 collection name and 1 ID for each item you are trying to remove. To find the ID, please use .findItem.
Singular Ex. .rmItem Waypoints 1
Multiple Ex. .rmItem Waypoints 1 3 5 7

.clearItem "collection name"
Removes all items in the collection. Requires 1 collection name.
Ex. .clearCollection Waypoints

"""


