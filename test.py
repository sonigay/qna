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
from konlpy.tag import Kkma




client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지식 안내', type=1))
	
	

kkma = Kkma()
filter_kkma = ['NNG',  #보통명사
	       'NNP',  #고유명사
	       'OL' ,  #외국어
	      ]

def tokenize_kkma(doc):
	jpype.attachThreadToJVM()
	token_doc = ['/'.join(word) for word in kkma.pos(doc)]
	return token_doc
	
def tokenize_kkma_noun(doc):
	jpype.attachThreadToJVM()
	token_doc = ['/'.join(word) for word in kkma.pos(doc) if word[1] in filter_kkma]
	return token_doc
	

	
token_faqs = []
for i in range(len(faqs)):
	token_faqs.append([tokenize_kkma_noun(faqs['제목'][i]), i ])
	
	
tagged_faqs = [TaggedDocument(d, [int(c)]) for d, c in token_faqs]


# make model
cores = multiprocessing.cpu_count()
d2v_faqs = doc2vec.Doc2Vec(
	vector_size=100,
	alpha=0.025,
	min_alpha=0.025,
	hs=1,
	negative=0,
	dm=0,
	window=3,
	dbow_words = 1,
	min_count = 1,
	workers = cores,
	seed=0,
	epochs=100
	)
d2v_faqs.build_vocab(tagged_faqs)

# train document vectors
for epoch in range(50):
	d2v_faqs.train(tagged_faqs,
		       total_examples = d2v_faqs.corpus_count,
		       epochs = d2v_faqs.epochs
		      )
	d2v_faqs.alpha -= 0.0025 # decrease the learning rate
	d2v_faqs.min_alpha = d2v_faqs.alpha # fix the learning rate, no decay


	
@client.event
async def on_message(message):
	
	if message.content == '!테스트':
		faqs = pd.read_csv(('test.csv'), encoding='CP949')
		faqs = faqs[['순번', '제목', '내용']]
		await client.send_message(message.channel, faqs)
		




                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
