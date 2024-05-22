import sys

import requests
from selectorlib import Extractor
import pandas as pd
import re
import Extract
List = []
df = pd.read_excel(r"C:\Users\admin\PycharmProjects\N11-POC\Amazone\Amazone1.xls")
for i in df["URL"]:

    # url = "https://www.amazon.com.tr/s?bbn=12466668031&rh=n%3A13028019031&fs=true&ref=lp_13028019031_sar"
    url = i
    proxies = {"http": "http://HWF:Hybrid2022_country-tr@geo.iproyal.com:12323"}

    e = Extractor.from_yaml_file('page.yml')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    # headers = {
    #     'authority': 'www.amazon.com.tr',
    #     'pragma': 'no-cache',
    #     'cache-control': 'no-cache',
    #     'dnt': '1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'sec-fetch-site': 'none',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-dest': 'document',
    #     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #     'viewport-width': '1366',
    #     'sec-ch-ua-mobile': '?1'}
    # Download the page using requests
    print("pagination %s" % url)
    r = requests.get(url, headers=headers, proxies=proxies)

    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
    links = e.extract(r.text)
    # print(links)
    x = links["pages"]
    print(x)
    try:
        for i in range(2, int(x)):
            if i is not "None":
                try:
                    # z = (
                    #     "https://www.amazon.com.tr/s?i=electronics&bbn=13709883031&rh=n%3A12466496031%2Cn%3A13709883031%2Cn%3A13709935031&dc&fs=true&page={}&qid=1653563154&rnid=13709883031&ref=sr_pg_{}").format(i, i)
                    x = re.sub("page=2", "page={}", url)

                    z = re.sub("sr_pg_2", "sr_pg_{}", x).format(i,i)
                    print(z)
                    Extract.page(url=z)
                    df["URL"].drop(i)
                except:
                    print("Exception: ", sys.exc_info())
                    List.append(z)
                    pass
    except:
        "None"

print(List)
