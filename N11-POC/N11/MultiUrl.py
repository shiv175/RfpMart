import requests
from bs4 import BeautifulSoup
import N11page

List_url = ["https://www.n11.com/video-oyun-konsol"]

for url in List_url:
    links = []
    session = requests.session()
    proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    # root_url = "https://www.n11.com/video-oyun-konsol"
    html = requests.get(url, proxies=proxies, allow_redirects=False)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.prettify())
    pages = []
    paging = soup.find("div", {"class": "pagination"}).findAll('a')
    # start_page = paging[1].text
    # last_page = paging[len(paging)-2].text
    # print(last_page)
    # print(paging)
    for i in paging:
        # print(i.get('href'))
        links.append(i.get('href'))

    for paging in soup:
        i = links[-1]
        html = requests.get(i)
        soup = BeautifulSoup(html.text, 'html.parser')
        paging = soup.find("div", {"class": "pagination"}).findAll('a')

        for i in paging:
            # print(i.get('href'))
            links.append(i.get('href'))
    new = set(links)
    links = list(new)
    # print(len(links))

    # for x in links:
    #     # pages.append(i + str(i))
    #     # N11page.pageExtraction(url=url.get('href').split("?")[0] +"?sf={}".format(j))
    #     # pages.append(url.get('href').split("?")[0] +"?sf={}".format(j))
    #     N11page.pageExtraction(url=x)
    #     print(x)
    for i in range(1, len(links) + 1):
        pages.append(url + "?sf={}".format(i))
        N11page.pageExtraction(url=url + "?sf={}".format(i))
        print(url + "?sf={}".format(i))

