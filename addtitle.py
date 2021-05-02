import os
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from tqdm import tqdm

file_list = os.listdir("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone")

def addrow(file_name):
	df = pd.read_csv("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/%s"%file_name,header=None)
	df.loc[-1] =  ["tweet_created_time","tweet_id","tweet_content","retweet_num","reply_num","like_num",
	"vaderSentiment","neg_prob","neu_prob","pos_prob","compound_tone"]
	df.index = df.index + 1
	df.sort_index(inplace=True) 
	df.to_csv("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone_withtitle/%s"%file_name, encoding='utf-8', index=False, header=False)

for file in tqdm(file_list):
	try:
		addrow(file)
	except:
		print(file)
