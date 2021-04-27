from lxml import etree
import re
import csv

content = open("test.html",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
html = etree.HTML(HtmlStr)


acc = html.xpath("//h3[@class='LC20lb DKV0Md']/text()")
with open("firmtwitteracchash.csv",'a') as f:
	w = csv.writer(f)
	for i in acc:
		if re.search("\) \| Twitter",i):
			print(i)
			w.writerow(["delta",i])
		if re.search("hashtag",i):
			print(i)
			w.writerow(["delta",i])
