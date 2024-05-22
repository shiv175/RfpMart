import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import json
from pymongo import MongoClient
import TrendyolPage
import csv

links = []
session = requests.session()
proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
root_url  = "https://www.trendyol.com/tencere-x-c1191"
html = requests.get(root_url,proxies=proxies, allow_redirects=False)
soup = BeautifulSoup(html.text, 'html.parser')

i = 2
for i in range(2,98):
    try:
        url = str(root_url+"?pi="+str(i))
        print(url)
        time.sleep(3)
        i = i + 1
        print(i)
        html = requests.get(url, proxies=proxies, allow_redirects=False)
        print(html.text)
        if html:
            soup = BeautifulSoup(html.text, 'html.parser')
            links.append(url)
            TrendyolPage.pageExtraction(url=url)
            print("hii")
    except:
        break
# print(links)
# for l in links:
#