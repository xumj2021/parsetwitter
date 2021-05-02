from lxml import etree
import re
import csv
import pandas as pd
import unicodedata

content = open("test.htm",'r').read()
HtmlElement = etree.HTML(content)
HtmlStr = etree.tostring(HtmlElement, encoding="utf8").decode()
html = etree.HTML(HtmlStr)

content = html.xpath("//table[@style='width: 100%;']/tr/td//text()")
print(content)

