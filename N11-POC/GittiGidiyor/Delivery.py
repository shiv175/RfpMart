import requests
from bs4 import BeautifulSoup

# url = "https://www.gittigidiyor.com/saat"
session = requests.session()
proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
url = 'https://www.gittigidiyor.com/cep-telefonu-aksesuar/kilif'

source_code = session.get(url, proxies=proxies, allow_redirects=False)

plain_text = source_code.text

soup = BeautifulSoup(plain_text, 'html.parser')

# print(soup.prettify())
links = []
Rating = []
productLinks = []
for link in soup.findAll('a', {'rel': 'bookmark'}):
    # print(link.get('href'))
    links.append(link.get('href'))

    for ProductLinks in links:
        productLinks.append(ProductLinks)
        source_code = session.get(ProductLinks, proxies=proxies, allow_redirects=False)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup.prettify())


        for i in soup.find_all("span", {"class": "shippingTimeDetail"}):
            print(i.text.strip())
            Rating.append(i.text.strip())


print(Rating)