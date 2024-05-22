import pandas as pd
df = pd.read_excel(r"C:\Users\admin\Downloads\n11.xls")
# import N11page
import requests
from bs4 import BeautifulSoup
links = []
for i in df["URL"]:
    print(i)

    session = requests.session()
    proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    root_url = i
    html = requests.get(root_url, proxies=proxies, allow_redirects=False)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.prettify())
    pages = []
    paging = soup.find("div", {"class": "pagination"}).findAll('a')
    # start_page = paging[1].text
    # last_page = paging[len(paging)-2].text
    # print(last_page)
    print(paging)
    for i in paging:
        print(i.get('href'))
        links.append(i.get('href'))

    for paging in soup:
        url = links[-1]
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        paging = soup.find("div", {"class": "pagination"}).findAll('a')

        for i in paging:
            print(i.get('href'))
            links.append(i.get('href'))
    new = set(links)
    links = list(new)
    print(len(links))

    for i in range(1, len(links) + 1):
        pages.append(root_url + "?sf={}".format(i))
        # N11page.pageExtraction(url=root_url + "?sf={}".format(i))
        print(root_url + "?sf={}".format(i))