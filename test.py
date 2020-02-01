import discord
import asyncio
import random
import os
import warnings
from gensim.models import doc2vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
from google.colab import drive

drive.mount('/content/drive/')

client = discord.Client()

faqs = pd.read_csv(os.path.join('data','/content/drive/My Drive/test.csv'), encoding='CP949')

@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지식 안내', type=1))





                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
