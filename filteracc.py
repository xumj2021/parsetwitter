import re
from tqdm import tqdm
import csv

twlist=open("fulltwacclist.txt","r")

def filteracc(a):
	twaccount = re.findall("\((@.*)\)",a)[0]
	twname = re.findall("(.*)\s\(@",a)[0].replace('\t','')
	return([twname,twaccount])

	

with open('fullfinaltwacclist.csv','w') as f:
	g = csv.writer(f)
	for line in tqdm(twlist):
		info = line.split(";")
		conm = info[0]
		try:
			out = filteracc(info[1])
			g.writerow([conm,out[0],out[1]])
		except:
			pass
