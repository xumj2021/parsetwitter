from lxml import etree
import re
import csv

content = open("test.html",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
html = etree.HTML(HtmlStr)

def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

accinfo = html.xpath("//div[@class='YouTubeUserTopInfo']//text()")
acc = translist(accinfo)
print(acc)
gradeinfo = html.xpath("//div[@style='float: left; width: 900px; height: 150px;']//text()")
grade = translist(gradeinfo)
print(grade)
		
