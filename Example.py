# import sqlite3
# import discord

# SQLite3 Connection Example
def ConnectSQLite(Type, Command):
    Database = sqlite3.connect("database name here.db")
    Cursor = Database.cursor()
    Cursor.execute(Command)
    if Type == "Get":
        AllData = Cursor.fetchall()
        Database.close()
        return AllData
    elif Type == "Set":
        Database.commit()
        Database.close()
        
# This is the formula i created for calculating the item worth in my discord bot level system.

            Item_Order1 = (1 * Data[0][7]) #digit 7 means the column order where it multiplies the "1" with the amount u currently have.
            Calculate = Item_Order1 + Adding_Another_Item
            str(Calculate)
            
# Easy Bot Command Example
if message.content.startswith('-examplecommand'):
        
        Embed = discord.Embed(
            title = "BotName Commands",
            description = "Text That u want to be viewed",
            color = 0x0094ff
        )
        await message.channel.send(embed = Embed)
        
# Discord Status Example
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Status of your bot'))
    
    # Code Made By Sloth And SleepWalking (Milan)
