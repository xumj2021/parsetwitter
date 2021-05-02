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

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0"
}

with open('secaaer.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        download_url = "https://www.sec.gov" + row[1]
        type = row[1].split(".")[-1]
        if type == "pdf":
            with open('/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERfile/%s.pdf' % row[0], 'wb') as f:
                data = requests.get(download_url, headers, timeout=10)
                f.write(data.content)
                print(row[0])
        else:
            with open("/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERfile/%s.txt" % row[0], 'w') as g:
                data = requests.get(download_url, headers, timeout=10)
                page = etree.HTML(data)
                context = page.xpath("//div[@id='main-content']//text()")
                print(context)
                f.write(context)
