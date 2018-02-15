import discord
from discord.ext import commands
import asyncio
import random
import pyperclip
import re


#client is essentially our bot
#client = discord.Client();
client = commands.Bot(command_prefix="!")
prefix = "cmd";
filterOn = True;
kickWords = ['fuck', 'shit', 'bitch'];
#TODO can use tinydb to hold number of swears for a ban
#switch statement definitions NOTE: this is not currently used
##def helpMe(message):
##    print("got here")
##    print(message.channel)
##    client.send_message(message.channel, "Here is a list of cmd commands:")
##    
##switcher = {
##    "helpMe": helpMe
##    }

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.listen()
async def on_message(message):
    global filterOn
    if "mert" in message.content:
        await client.send_message(message.channel, message.content.replace("mert", "*Golden God*"))
    if filterOn:
        for curse in kickWords:
            searchObj = re.search(curse, message.content, re.I)
            if searchObj:
                await client.delete_message(message)
                await client.send_message(message.channel, "Profane message deleted")
                break 
    if message.content.startswith(prefix):
        msg = message.content[len(prefix):]
        #print(msg)
        msgList = msg.split()
        #python has no switch statements
        #print(msgList[0])
        #using if elses for now
        if(msgList[0].lower() == "helpme"):
            await client.send_message(message.channel, "Here is a list of cmd commands:")
        elif(msgList[0].lower() == "filteroff"):
            await client.send_message(message.channel, "Filter off")
            filterOn = False;
        elif(msgList[0].lower() == "filteron"):
            await client.send_message(message.channel, "Filter on")
            filterOn = True;
        else:
            await client.send_message(message.channel, "Invalid command")
            
@client.command(pass_context=True)
#need at least one param in a comman ctx which stands for context
async def ping(context):
    await client.send_message(context.message.channel, "pong")

#can't have two on_messages

client.run('NDEyNzI4NDg3NzMyOTY5NDcy.DWOe9Q.7W2-xUZxIbaVbIE0EeKEKYSLE5o')
