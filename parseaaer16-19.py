from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
from tqdm import tqdm
import unicodedata

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/PycharmProjects/twitch/geckodriver')
def parseinfo(year):
	if year==2020:
		driver.get("https://www.sec.gov/divisions/enforce/friactions/friactions%s.htm"%year)
	else:
		driver.get("https://www.sec.gov/divisions/enforce/friactions/friactions%s.shtml"%year)
	time.sleep(3)
	HtmlElement = etree.HTML(driver.page_source)
	HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
	html = etree.HTML(HtmlStr)

	with open("test.html",'w') as f:
		f.write(driver.page_source)

	href = html.xpath("//table[@id='mainlist']/tbody/tr/td[1]/a/@href")
	date = html.xpath("//table[@id='mainlist']/tbody/tr/td[2]/text()")
	#releaseno = html.xpath("//table[@id='mainlist']/tbody/tr/td[3]/text()[2]")
	entity = html.xpath("//table[@id='mainlist']/tbody/tr/td[3]/text()[1]")
	index = html.xpath("//table[@id='mainlist']/tbody/tr/td[1]/a/text()")
	year = ["%s"%year]*len(index)

	with open("secaaer.csv",'a') as f:
		g = csv.writer(f)
		for i in range(len(href)):
			entityu = unicodedata.normalize('NFD', entity[i]).encode('ascii', 'ignore').decode("utf-8")
			g.writerow([index[i],href[i],date[i],entityu])
		
for year in range(2016,2021):
	parseinfo(year)
	print("year %s completed"%year)



