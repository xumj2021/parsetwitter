from selenium import webdriver
import time
import json

option = webdriver.FirefoxOptions()
option.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/Users/mengjiexu/Dropbox/Pythoncodes/Bleier/geckodriver')

driver.get("https://sec.report/CIK/Search/Comscore,%20Inc.")
time.sleep(5)    

orcookies = driver.get_cookies()
print(orcookies)
cookies = {}
for item in orcookies:
    cookies[item['name']] = item['value']
with open("seccookies.txt", "w") as f:
    f.write(json.dumps(cookies))
