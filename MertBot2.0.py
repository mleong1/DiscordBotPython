import discord
import asyncio
import random
import pickle
import pyperclip

client = discord.Client();

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('matt'):
        await client.send_message(message.channel, 'Of course')
        
client.run('NDEyNzI4NDg3NzMyOTY5NDcy.DWOe9Q.7W2-xUZxIbaVbIE0EeKEKYSLE5o')
