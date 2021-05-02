import pandas as pd
import re

df=pd.read_csv('/Users/mengjiexu/Documents/Projects/Twitter/AQ/secaaerpreta.csv')

def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

conamelist = []
for line in df["entity"]:
	line = line.replace("and",",")
	coname = re.findall("(.*Inc.)|(.*Corporation)|(.*Corp)|(.* International)|(.*international)|(.*Co\.)|(.*Company)|(.*plc)|(.*PLC)|(.*Group)",line)
	conamelist.append(";".join(translist(coname[0])))

df['Coname'] = conamelist 

df.to_csv("/Users/mengjiexu/Documents/Projects/Twitter/AQ/secaaerpretawithcik.csv", encoding='utf-8', index=False, header=False)


