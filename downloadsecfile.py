from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
from tqdm import tqdm
import unicodedata
import requests
from tika import parser # pip install tika

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

with open('supplement.csv', 'r') as file:
    reader = csv.reader(file)
    for row in tqdm(reader):
        download_url = "https://www.sec.gov" + row[1]
        type = row[1].split(".")[-1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        if type == "pdf":
            with open('/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERpdf/%s.pdf' %row[0], 'wb') as f:
                data = requests.get(download_url, headers, timeout=10)
                f.write(data.content)
        else:
            with open("/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERtxt/%s.txt" % row[0], 'w') as g:
                data = requests.get(download_url, headers, timeout=10)
                page = etree.HTML(data.content)
                if int(row[4])>2017:
                    context = page.xpath("//div[@id='main-content']//text()")
                elif int(row[4])!=2010:
                    context = page.xpath("//table/tr/td[3]//text()")
                else:
                    context = page.xpath("//table[@style='width: 100%;']/tr/td//text()")
                info = ";".join(context).strip()
                g.write(info)





