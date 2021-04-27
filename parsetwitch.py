from selenium import webdriver
import time
from lxml import etree

urls = open("gameurl.txt", 'r')

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/PycharmProjects/twitch/geckodriver', options=option)

def update(url):
    driver.get(url)
    time.sleep(3)
    HtmlElement = etree.HTML(driver.page_source)
    HtmlStr = etree.tostring(HtmlElement, encoding="utf-8").decode()
    html = etree.HTML(HtmlStr)
    info = html.xpath("//p[@class='tw-c-text-alt tw-font-size-4']/@title")
    return (info)

with open("updateinfo.txt", 'a') as g:
    for line in urls:
        url = line.strip()
        print(url)
        updateinfo = update(url)
        print(url + ";" + ";".join(updateinfo) + '\n')
        g.write(url + ";" + ";".join(updateinfo) + '\n')
        time.sleep(3)
