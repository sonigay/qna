import discord
import asyncio
import random
import os
import warnings
from gensim.models import doc2vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd

faqs = pd.read_csv(('test.csv'), encoding='CP949')


client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지식 안내', type=1))

	
@client.event
async def on_message(message):
	
	if message.content == '!테스트':
		faqs = pd.read_csv(('test.csv'), encoding='CP949')
		await client.send_message(message.channel, faqs)
		




                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
