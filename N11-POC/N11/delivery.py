import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/arama?q=telefonu"
session = requests.session()
proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
# url = "https://www.n11.com/arama?q=telefonu"
# source_code = requests.get(url)
source_code = session.get(url, proxies=proxies, allow_redirects=False)
# print(source_code)
links = []
plain_text = source_code.text
# print(plain_text)
# source_code.headers['content-type']
soup = BeautifulSoup(plain_text, 'html.parser')
# print(soup)
# print(soup.prettify())
z = 0
for link in soup.find_all('a', {'class': 'plink'}):
    links.append(link.get('href'))
    # print(links)

for i in links:
    source_code = requests.get(i, proxies=proxies, allow_redirects=False)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    productList = soup.findAll('script', {"type": "application/ld+json"})[1]
    print(productList)
    try:
        for link in soup.find('div', {'class': 'price'}).findAll('span'):
            y = (link.text).rstrip()
            print(y)


    except:
        print(1)
        pass
print(len(links))
    # links.append(link.text)[-2]
    # print(links)
