import os
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from tqdm import tqdm

file_list = os.listdir("/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone")

for file in file_list:
	oldname = "/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/%s"%file
	newname = "/Users/mengjiexu/Documents/TwitterParsing/results/2013Q1_Tone/%s_Tone.csv"%file.split(".")[0]
	os.rename(oldname,newname) 

