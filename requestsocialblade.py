from selenium import webdriver
import time
import json
from lxml import etree
import csv
from lxml import etree
import re
from tqdm import tqdm
import requests

f=open("/Users/mengjiexu/Dropbox/Pythoncodes/filteredtwacclist.txt",'r')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Origin": "https://socialblade.com",
    "Connection": "keep-alive",
    "Referer": "https://socialblade.com/",
    "Host": "stats.g.doubleclick.net"}

def get_content(firm):
    with open("cookies.txt", "r")as f:
        cookies = f.read()
        cookies = json.loads(cookies)
        session = requests.session()
        html = session.get("https://socialblade.com/twitter/user/%s"%firm, headers=headers, cookies=cookies)
        time.sleep(3)
        with open('test.html','w') as g:
        	g.write(html.text)
    return(html.text)


def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

def twinfo(content):
	html = etree.HTML(content)
	accinfo = html.xpath("//div[@class='YouTubeUserTopInfo']//text()")
	acc = translist(accinfo)
	gradeinfo = html.xpath("//div[@style='float: left; width: 900px; height: 150px;']//text()")
	grade = translist(gradeinfo)
	out = [",".join(acc),",".join(grade)]
	return(out)

for line in tqdm(f):
	with open('/Users/mengjiexu/Dropbox/Pythoncodes/socialtw.csv','a') as g:
		h=csv.writer(g)
		acc = line.split(";")[-1].strip()
		print(acc)
		out = twinfo(get_content(acc))
		print(out)
		h.writerow(out)


