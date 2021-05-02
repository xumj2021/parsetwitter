from lxml import etree
import re
import csv

content = open("test.html",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
html = etree.HTML(HtmlStr)

cik = html.xpath("//div[@class='jumbotron']/div[2]/div/div[2]/table/tr/td[2]/text()")
coname = html.xpath("//div[@class='jumbotron']/div[2]/div/div[2]/table/tr/td[1]/a/text()")
out = dict(zip(coname,cik))
print(out)
print(coname)