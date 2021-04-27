from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
from tqdm import tqdm

firmlist = open("googlesearchtwlist.txt",'r')

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/PycharmProjects/twitch/geckodriver')

def parsetwacc(firm):
    driver.get("https://www.google.com/webhp")
    time.sleep(3)
    try:
        driver.execute_script("window.scrollTo(0,1000)")
        driver.find_element_by_xpath("//div[contains(text(),'Ich stimme zu')]").click()
    except:
        pass
    driver.find_element_by_xpath("//input[@title='Suche']").send_keys('%s twitter accounts'%firm)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@title='Suche']").send_keys(Keys.ENTER)
    time.sleep(1)
    HtmlElement = etree.HTML(driver.page_source)
    HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
    html = etree.HTML(HtmlStr)
    acc = html.xpath("//h3[@class='LC20lb DKV0Md']/text()")
    with open("firmtwitteracchash.csv",'a') as f:
        w = csv.writer(f)
        for twacc in acc:
            if re.search("\) \| Twitter",twacc):
                w.writerow([firm,twacc])
            if re.search("hashtag",twacc):
                w.writerow([firm,twacc])


for firm in tqdm(firmlist):
    parsetwacc(firm.strip())
    time.sleep(1)
