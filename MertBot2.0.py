import discord
from discord.ext import commands
import asyncio
import random
import pyperclip
import re

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
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
async def bitcoinminer(context):
    await client.send_message(context.message.channel, "pong")

@client.command(pass_context=True)
async def summon(context):
    summoned_channel = context.message.author.voice_channel
    #if the command user isn't in voice chat
    if summoned_channel is None:
        await client.send_message(context.message.channel, "You are not in a voice channel.")
        return False
    #else place the bot in the voice chat
    #this step needs checks if the bot is in another server's chat but we'll only be in one for this bot
    voice = await client.join_voice_channel(summoned_channel)
    #TODO remember the server.id that our bot is in and we can tell if in different channel based on server id
    print(voice.user.name)

@client.command(pass_context=True)
async def disconnect(context):
    #i think coroutine messages need await???
    if client.is_voice_connected(context.message.server):
        #this botVoice is what will make the youtube player or ffmpeg player
        botVoice = client.voice_client_in(context.message.server)
        print(botVoice.is_connected())
        await botVoice.disconnect()

@client.command(pass_context=True)
async def play(context, url : str):
    opts = {
            'default_search': 'auto',
            'quiet': True,
            }
    #going to need link checks and error handling
    if client.is_voice_connected(context.message.server):
        botVoice = client.voice_client_in(context.message.server)
        player = await botVoice.create_ytdl_player(url, ytdl_options=opts)
        player.start()

@client.command(pass_context=True)
async def soundemote(context):
    if client.is_voice_connected(context.message.server):
        botVoice = client.voice_client_in(context.message.server)
        player = botVoice.create_ffmpeg_player('nocopysound.wav')
        player.start()


client.run('NDEyNzI4NDg3NzMyOTY5NDcy.DWOe9Q.7W2-xUZxIbaVbIE0EeKEKYSLE5o')
