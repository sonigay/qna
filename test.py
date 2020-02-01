import discord
import asyncio
import random
import os


client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지식 안내', type=1))





                        
access_token = os.environ["BOT_TOKEN"]
git_access_token = os.environ["GIT_TOKEN"]
client.run(access_token)
