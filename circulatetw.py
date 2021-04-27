import os
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from tqdm import tqdm

g = os.walk("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1")

def gettone(file_name):
	data = pd.read_csv("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1/%s"%file_name,header=None)
	try:
		tweets = data.iloc[:,2]
		analyzer = SentimentIntensityAnalyzer()
		with open("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/%s_Tone.csv"%file_name,'a') as f:
			w = csv.writer(f)
			for i in range(len(tweets)):
				vs = analyzer.polarity_scores(tweets[i])
				baseinfo = data.iloc[[i]].values.tolist()[0]+[vs]
				w.writerow(baseinfo)
	except:
		print("%s has error"%file_name)
		with open("/Users/mengjiexu/Documents/TwitterParsing/results/error.txt",'a') as h:
			h.write(file_name)

for path,dir_list,file_list in g:
    for file_name in tqdm(file_list):
    	a = os.path.join(path, file_name)
    	gettone(file_name)

