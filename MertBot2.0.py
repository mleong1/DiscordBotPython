import discord
import asyncio
import random
import pickle
import pyperclip

#client is essentially our bot
client = discord.Client();
prefix = "cmd"

#switch statement definitions
def helpMe(message):
    client.send_message(message.channel, "Here is a list of cmd commands:")
    
switcher = {
    "helpMe": helpMe
    }
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if "mert" in message.content:
        await client.send_message(message.channel, message.content.replace(word, "*Golden God*"))
    if message.content.startswith(prefix):
        msg = message.content[len(prefix):]
        print(msg)
        msgList = msg.split()
        #python has no switch statements
        print(msgList[0])
        switcher[msgList[0]](message)
        
        
#can't have two on_messages

client.run('NDEyNzI4NDg3NzMyOTY5NDcy.DWOe9Q.7W2-xUZxIbaVbIE0EeKEKYSLE5o')
