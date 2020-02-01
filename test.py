import discord
import asyncio
import random
import os
import warnings
from gensim.models import doc2vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
import jpype
import multiprocessing
from konlpy.tag import Twitter





faqs = pd.read_csv(('test.csv'), encoding='CP949')




Twitter = Twitter()
filter_Twitter = ['NNG',  #보통명사
	       'NNP',  #고유명사
	       'OL' ,  #외국어
	       ]

def tokenize_kkma(doc):
	token_doc = ['/'.join(word) for word in Twitter.pos(doc)]
	return token_doc

print(twitter.pos("히라마블로그에온걸환영해!"))



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
		faqs = faqs[['순번', '제목', '내용']]
		await client.send_message(message.channel, faqs)
		




                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
