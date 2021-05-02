from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
from tqdm import tqdm
import unicodedata

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2);
fp.set_preference("browser.download.manager.showWhenStarting",True)
fp.set_preference("browser.download.dir", "/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERfile/")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
option = webdriver.FirefoxOptions()
option.add_argument('-headless')

driver = webdriver.Firefox(executable_path='/Users/mengjiexu/PycharmProjects/twitch/geckodriver', firefox_profile=fp)

def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

def parseinfo(year):
	driver.get("https://www.sec.gov/divisions/enforce/friactions/friactions%s.shtml"%year)
	time.sleep(3)
	HtmlElement = etree.HTML(driver.page_source)
	HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
	html = etree.HTML(HtmlStr)

	with open("test.html",'w') as f:
		f.write(driver.page_source)

	href = html.xpath("//table[@cellspacing='7']/tbody/tr/td[1]/a/@href")
	index = html.xpath("//table[@cellspacing='7']/tbody/tr/td[1]/a/text()")
	date = html.xpath("//table[@cellspacing='7']/tbody/tr/td[2]/text()")
	entity = html.xpath("//table[@cellspacing='7']/tbody/tr/td[3]/text()[1]")
	#releaseno = html.xpath("//table[@cellspacing='7']/tbody/tr/td[3]/text()[2]")

	entity_trans = translist(entity)
	print(len(href))

	with open("test.csv",'a') as f:
		g = csv.writer(f)
		for i in range(len(href)):
			driver.get("https://www.sec.gov"+href[i])
			time.sleep(2)
			entityu = unicodedata.normalize('NFD', entity_trans[i]).encode('ascii', 'ignore').decode("utf-8")
			g.writerow([index[i],href[i],date[i],entityu])

for year in range(2009,2016):
	parseinfo(year)
	print("year %s completed"%year)




