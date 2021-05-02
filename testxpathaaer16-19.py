from lxml import etree
import re
import csv
import pandas as pd
import unicodedata

content = open("test.html",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf8").decode()
html = etree.HTML(HtmlStr)

href = html.xpath("//table[@id='mainlist']/tbody/tr/td[1]/a/@href")
date = html.xpath("//table[@id='mainlist']/tbody/tr/td[2]/text()")
releaseno = html.xpath("//table[@id='mainlist']/tbody/tr/td[3]/text()[2]")
entity = html.xpath("//table[@id='mainlist']/tbody/tr/td[3]/text()[1]")
index = html.xpath("//table[@id='mainlist']/tbody/tr/td[1]/a/text()")

with open("test.csv",'w') as f:
	g = csv.writer(f)
	for i in range(5):
		entityu = unicodedata.normalize('NFD', entity[i]).encode('ascii', 'ignore').decode("utf-8")
		print(entityu)
		g.writerow([index[i],releaseno[i].replace("\xa0","").strip(),href[i],date[i],entityu])
		
