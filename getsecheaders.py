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
import json
import requests


cookies = {'Cookie': '_ga=GA1.2.796598643.1619809601;_gid=GA1.2.67468862.1619809601;_gat=1;_gat_GSA_ENOR0=1;_gat_GSA_ENOR1=1'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

data = requests.get("https://www.sec.gov//litigation/litreleases/2017/lr23978.htm", headers, timeout=10)

print(data.content)