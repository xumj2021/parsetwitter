from lxml import etree
import re
import csv
import pandas as pd
import unicodedata

content = open("test.html",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf8").decode()
html = etree.HTML(HtmlStr)

def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

href = html.xpath("//table[@cellspacing='7']/tbody/tr/td[1]/a/@href")
index = html.xpath("//table[@cellspacing='7']/tbody/tr/td[1]/a/text()")
date = html.xpath("//table[@cellspacing='7']/tbody/tr/td[2]/text()")
entity = html.xpath("//table[@cellspacing='7']/tbody/tr/td[3]/text()[1]")
releaseno = html.xpath("//table[@cellspacing='7']/tbody/tr/td[3]/text()[2]")

print(len(translist(entity)))
print(len(href))
print(len(date))
print(len(index))
print(len(releaseno))

for i in range(len(releaseno)):
	print(i)
	print(entity[i])
	print(releaseno[i])