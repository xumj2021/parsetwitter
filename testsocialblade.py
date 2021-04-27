from selenium import webdriver
import time
import json
from lxml import etree
import csv
from lxml import etree
import re
from tqdm import tqdm

f=open("/Users/mengjiexu/Dropbox/Pythoncodes/filteredtwacclist.txt",'r')

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/Dropbox/Pythoncodes/Bleier/geckodriver')

def getinfo(firm):
	driver.get("https://socialblade.com/twitter/user/%s"%firm)
	time.sleep(2)
	HtmlElement = etree.HTML(driver.page_source)
	HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
	html = etree.HTML(HtmlStr)
	accinfo = html.xpath("//div[@class='YouTubeUserTopInfo']//text()")
	return(accinfo)


for line in tqdm(f):
	acc = line.split(";")[-1].strip()
	print(acc)
	out=getinfo(acc)
	print(out)
