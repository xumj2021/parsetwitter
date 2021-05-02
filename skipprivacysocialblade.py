from selenium import webdriver
import time
import json
from lxml import etree
import csv
from lxml import etree
import re
from tqdm import tqdm
import random

f=open("/Users/mengjiexu/Dropbox/Pythoncodes/filteredtwacclist.txt",'r')

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/Dropbox/Pythoncodes/Bleier/geckodriver')
email = 'a.bleier@fs.de'
pw = 'influencer2020'

def login(email, pw):
    driver.get(
        "https://socialblade.com/login")
    time.sleep(3)
    driver.find_element_by_xpath("//div/input[@name = 'dashboard_email']").send_keys(email)
    driver.find_element_by_xpath("//div/input[@name = 'dashboard_password']").send_keys(pw)
    driver.find_element_by_xpath("//div/input[@type = 'submit']").click()
    time.sleep(1)
    
login(email, pw)


def translist(infolist):
	out = list(filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), [i.strip() for i in infolist]))
	return(out)

def twinfo(firm):
	driver.get("https://socialblade.com/twitter/user/%s"%firm)
	time.sleep(random.randint(4, 10))
	HtmlElement = etree.HTML(driver.page_source)
	HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
	html = etree.HTML(HtmlStr)
	accinfo = html.xpath("//div[@class='YouTubeUserTopInfo']//text()")
	acc = translist(accinfo)
	gradeinfo = html.xpath("//div[@style='float: left; width: 900px; height: 150px;']//text()")
	grade = translist(gradeinfo)
	out = [firm,",".join(acc),",".join(grade)]
	return(out)

for line in tqdm(f):
	with open('/Users/mengjiexu/Dropbox/Pythoncodes/socialtw.csv','a') as g:
		h=csv.writer(g)
		acc = line.split(";")[-1].strip()
		out = twinfo(acc)
		h.writerow(out)


