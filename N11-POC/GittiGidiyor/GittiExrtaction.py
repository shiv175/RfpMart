import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import GittiPage
import json
from pymongo import MongoClient
import csv

df = pd.read_excel(r"C:\Users\admin\Downloads\n11.xls")

for i in df["URL"]:
    print(i)

    links = []
    session = requests.session()
    proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    # import pandas as pd
    # df = pd.read_excel(r"C:\Users\admin\Downloads\n11.xls")
    # print(df)

    root_url  = i
    url = root_url.rstrip(root_url[-1])
    html = requests.get(root_url,proxies=proxies, allow_redirects=False)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.prettify())
    pages = []
    paging = soup.find("div",{"class":"d8kjk0-0 gEPcey"}).find("ul",{"class":"sc-12aj18f-3 kLmKCh"}).find_all("li")
    start_page = paging[1].text
    last_page = paging[len(paging)-2].text
    print(last_page)
    for i in range(int(start_page),int(last_page)+1):
        pages.append(url+format(i))
        print(url+format(i))


    for page in pages:
        try:
            GittiPage.pageExtract(url=page)
            print(page)

        except:
            pass