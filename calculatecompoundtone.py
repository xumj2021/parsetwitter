import os
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from tqdm import tqdm


g = os.walk("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/")

def gettone(file_name):
	try:
		data = pd.read_csv("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/%s"%file_name,header=None)
		pos_ave = data.iloc[:,9].mean()
		pos_nonzero = data.iloc[:,9].astype(bool).sum(axis=0)
		neg_ave = data.iloc[:,7].mean()
		neg_nonzero = data.iloc[:,7].astype(bool).sum(axis=0)
		neu_ave = data.iloc[:,8].mean()
		neu_nonzero = data.iloc[:,8].astype(bool).sum(axis=0)
		compound_ave = data.iloc[:,10].mean()
		compound_nonzero = data.iloc[:,10].astype(bool).sum(axis=0)
		retweet_ave = data.iloc[:,3].mean()
		retweet_nonzero = data.iloc[:,3].astype(bool).sum(axis=0)
		reply_ave = data.iloc[:,4].mean()
		reply_nonzero = data.iloc[:,4].astype(bool).sum(axis=0)
		like_ave = data.iloc[:,5].mean()
		like_nonzero = data.iloc[:,5].astype(bool).sum(axis=0)
		tweetnum = len(data)
		firm = file_name.split(".")[0]
		info  = [firm, pos_ave, pos_nonzero, neg_ave, neg_nonzero, neu_ave, neu_nonzero, 
		compound_ave, compound_nonzero, retweet_ave, retweet_nonzero, reply_ave, reply_nonzero,
		like_ave,like_nonzero, tweetnum]
		return(info)
	except:
		pass

	
with open("/Users/mengjiexu/Documents/TwitterParsing/results/avetone.csv",'w') as f:
	w = csv.writer(f)
	w.writerow(["firm", "pos_ave", "pos_nonzero", "neg_ave", "neg_nonzero", "neu_ave", "neu_nonzero", 
			"compound_ave", "compound_nonzero", "retweet_ave", "retweet_nonzero", "reply_ave", "reply_nonzero",
			"like_ave","like_nonzero", "tweetnum"])
	for path,dir_list,file_list in g:
		for file_name in tqdm(file_list):
			try:
				info  = gettone(file_name)
				w.writerow(info)
			except:
				print(file_name)


