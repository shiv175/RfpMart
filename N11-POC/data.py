import json

import pandas as pd
import requests
from bs4 import BeautifulSoup




session = requests.session()
proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
url = "https://www.n11.com/arama?q=Shirt"
# source_code = requests.get(url)
source_code = session.get(url, proxies=proxies, allow_redirects=False)
# print(source_code)
links = []
Review = []
Itemdescreption = []
Price = []
Rating = []
oldprice = []
category1 = []
category2 = []
category3 = []
category4 = []
category5 = []
category6 = []
category7 = []
Productlinks = []

plain_text = source_code.text
# print(plain_text)
# source_code.headers['content-type']
soup = BeautifulSoup(plain_text, 'html.parser')
# print(soup)
# print(soup.prettify())


for link in soup.find_all('a', {'class': 'plink'}):
    links.append(link.get('href'))
    # print(links)

for i in links:
    # now = datetime.now()
    source_code = requests.get(i, proxies=proxies, allow_redirects=False)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    Productlinks.append(i)
    print(i)

    productList = soup.findAll('script', {"type": "application/ld+json"})[0]
    # print(productList)
    PDescription = soup.findAll('script', {"type": "application/ld+json"})[1]
    # print(PDescription)
    PDescription.text.replace('<script type="application/ld+json">', "")
    PDescription.text.replace("</script>", "")

    try:
        old = soup.find_all("span", {"class": "ratio"})
        if old:
            for i in old:
                oldprice.append(i.text)
                # print(i.text)

    except:
        oldprice.append("-")
    try:
        for link in soup.find_all('p', {'class': 'info-content'})[-2]:
            y = (link.text).rstrip()
            # print(y)
    except:
        y = ""
    # print(PDescription.text)
    # script =script.remove("</script>]")
    # script=script.replace("[<script type='application/ld+json'>","json")
    json_object = json.loads(PDescription.text, strict=False)
    json_object1 = json.loads(productList.text)
    try:
        rating = json_object["aggregateRating"]['reviewCount']
        # print(rating)
        if rating:
            # print(rating)
            Review.append(rating)
    except:
        Review.append("-")

    try:
        rating = json_object["aggregateRating"]['ratingValue']

        if rating:
            # print(rating)
            Rating.append(rating)
        else:
            Rating.append(0)
    except:
        Rating.append("")

    try:
        rating = json_object["offers"]['lowPrice']
        # print(rating)
        if rating:
            # print(rating)
            Price.append(rating)
        else:
            Price.append(0)
    except:
        Price.append("-")

    try:
        rating = json_object["description"]
        #
        if rating:
            Itemdescreption.append(rating)
            # print(rating)
        else:
            Itemdescreption.append(0)
    except:
        Itemdescreption.append("-")
        # print(0)

    df = pd.DataFrame(
        {
            "Links": Productlinks,
            "Descreption": Itemdescreption, "Price": Price, "Rating": Rating, "Review": Review})
x = pd.ExcelWriter("n11-Shirt.xlsx", engine="xlsxwriter")
df.to_excel(x, sheet_name='Sheet1', index=False)
x.save()
