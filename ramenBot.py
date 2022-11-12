import random
import discord
import asyncio
from dependencies.gameList import gameList
from dependencies.ramenMoments import ramenMoments
from dependencies.gifList import gifList
#from dependencies.841776273793613926 import 841776273793613926
from discord import app_commands
import typing

class aclient(discord.Client): #Setup code
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=841776273793613926))
            self.synced = True
        print(f"Successfully logged in as {self.user}.")
        #await channelMsgJoke()
        await messageLoop()

client = aclient()
tree = app_commands.CommandTree(client)

async def messageLoop(): #Sends random gif in general chat every couple hours
    while True:
        waitTime = random.randint(28000, 34000)
        await asyncio.sleep(waitTime)

        channel = client.get_channel(841776274246467584)
        randGif = random.choice(gifList)
        await channel.send(f"{randGif}")

#async def horcruxJoke():
#    channel = client.get_channel(931570568334016542)
#    await channel.send("This is true.")

async def channelMsgJoke():
    channel = client.get_channel(841776317712039958)
    await channel.send("gAAAAABjTyrhtEgq7KK-90BzddPw68-NjUnfNRmhlT0fbT783HqoBECXId1uoe6PuR6YPpUPW52BsNeZ8u1M0cmSPd5hMv2lBQ==")

@tree.command(name="ramen", description="Ramen Moment :)", guild=discord.Object(id=841776273793613926)) #Sends random messages pulled from a list
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(ramenMoments))

@tree.command(name="soup", description="Spicy Soup :)", guild=discord.Object(id=841776273793613926)) #Sends a message which includes the users name (interaction.user.mention)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"YOOOO GUYS! YOU WON'T BELIEVE THIS!!!!! {interaction.user.mention} JUST HAD THE SPICIEST SOUP IN THEIR ENTIRE LIFE!!!!!! (I'm talking tons of powdered red chili and black people) IT....... IT FEELS LIKE {interaction.user.mention} IS ALIVE AGAIN!!!!!! {interaction.user.mention} FEELS VERY GOOD (For the moment) while they were drinking it, they couldn't help but wonder how would you eat it.....")

@tree.command(name="eldenring", description="{insert-game-here} is just like elden ring fr fr ong bro", guild=discord.Object(id=841776273793613926)) #Sends random message pulled from a list
async def self(interaction: discord.Interaction):
    randGame = random.choice(gameList)
    await interaction.response.send_message(f"{randGame} is just like elden ring now that I think about it")

@tree.command(name="shit", description=":Fa5:", guild=discord.Object(id=841776273793613926)) #Sends a gif to chat
async def self(interaction: discord.Interaction, ping: typing.Optional[str]):
    if ping != None:
    
        newPing = ping.replace("<@", "") 
        newPingFinal = newPing.replace(">", "") #Replacing <@ and > with nothing in <@{example-text}> to get {example-text} on its own (btw example-text would actually be a string of numbers)
        userPing = f"<@!{newPingFinal}>"

        await interaction.response.send_message(f"{userPing}", file=discord.File(".\\assets\\competitive-shitting-shitting.gif"))

    else:
        await interaction.response.send_message(file=discord.File(".\\assets\\competitive-shitting-shitting.gif"))

@tree.command(name="gak", description="g-g-g-gakster!?!??!*!^£(^£(", guild=discord.Object(id=841776273793613926)) #Sends a gif to chat
async def self(interaction: discord.Interaction, ping: typing.Optional[str]):

    if ping != None:

        newPing = ping.replace("<@", "")
        newPingFinal = newPing.replace(">", "")
        userPing = f"<@!{newPingFinal}>"

        await interaction.response.send_message(f"{userPing}", file=discord.File(".\\assets\\IMG_0787.png"))

    else:
        await interaction.response.send_message(file=discord.File(".\\assets\\IMG_0787.png"))
        

@tree.command(name="command_help", description="Lists all available commands.", guild=discord.Object(id=841776273793613926)) #Lists all commands
async def self(interaction: discord.Interaction):
    message = """The current commands are:
/ramen
/soup
/eldenring
/shit (optional: ping)
/gak (optional: ping)
/command_help"""
    await interaction.response.send_message(message)

with open(".\\token\\token.env", "r")as token:
    token = token.read()

if __name__ == "__main__":
    client.run(token)