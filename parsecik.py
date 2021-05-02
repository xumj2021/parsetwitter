import time
from lxml import etree
import csv
import re
from tqdm import tqdm
import requests
import json
import pandas as pd
import csv

df=pd.read_csv('/Users/mengjiexu/Documents/Projects/Twitter/AQ/secaaerpretaprecik_manualchecked.csv')
outlist =[]
linklist = []

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
"content-type": "application/json",
"Host": "sec.report",
"Connection": "keep-alive"
}

def getcik(firm):
    with open("seccookies.txt", "r")as f:
        cookies = f.read()
        cookies = json.loads(cookies)
        session = requests.session()

        url = "https://sec.report/CIK/Search/%s"%firm
        data = session.get(url, headers=headers, cookies = cookies)
        time.sleep(1)
        with open("test.html",'wb') as f:
            f.write(data.content)
        page = etree.HTML(data.content)

        cik = page.xpath("//div[@class='jumbotron']/div[2]/div/div[2]/table/tr/td[2]/text()")
        coname = page.xpath("//div[@class='jumbotron']/div[2]/div/div[2]/table/tr/td[1]/a/text()")
        out = dict(zip(coname,cik))
        outlist.append(out)

        linklist.append(url)

        return(out)
        

for i in tqdm(range(len(df))):
    out = getcik(df['FirmName'][i].strip())
    with open("/Users/mengjiexu/Documents/Projects/Twitter/AQ/cikmeta.csv",'a') as g:
        h = csv.writer(g)
        if out=={}:
            info = df.iloc[[i]].values.tolist()[0]+[""]
            h.writerow(info)
        else:
            coname = list(out.keys())
            cik = list(out.values())
            for j in range(len(cik)):
                info = df.iloc[[i]].values.tolist()[0]+[cik[j],coname[j]]
                h.writerow(info)


df["Urls"] = linklist
df["Cik"] = outlist
df.to_csv('/Users/mengjiexu/Documents/Projects/Twitter/AQ/secaaerpretawithcik.csv', index=False)



