import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
Category = []
links = []
price = []
Review = []
Rating = []
category = []
ProductDescreption = []
proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

# url = 'https://www.amazon.com.tr/s?k=telefon+k%C4%B1l%C4%B1f%C4%B1&i=electronics&bbn=12466497031&rh=n%3A12466496031%2Cn%3A13709880031%2Cn%3A13709897031%2Cn%3A13710045031&dc&crid=1CDD0QS38YZGE&qid=1646648386&rnid=12466496031&sprefix=telefon+k%C4%B1l%C4%B1f%C4%B1%2Caps%2C190&ref=sr_nr_n_10'
url = "https://www.amazon.com.tr/s?i=electronics&bbn=13709927031&rh=n%3A13709927031%2Cp_n_feature_eight_browse-bin%3A13710998031%7C13710999031%7C13711000031%7C13711001031%7C13711002031%7C13711003031&dc"
# data = requests.get(url,proxies=proxies, allow_redirects=False)
data = requests.get(url, headers=headers, proxies=proxies,allow_redirects=False)
print(data)
soup = BeautifulSoup(data.text, "html.parser")

# print(soup.prettify())

for link in soup.find_all('a', {'class': "a-link-normal s-no-outline"}):
    # print(link)
    links.append('https://www.amazon.com.tr' + link.get('href'))

# for pD in soup.find_all('span',{'class':"a-size-base-plus a-color-base a-text-normal"}):
#     ProductDescreption.append(pD.text)
print(len(links))
for url in links:
    # url = "https://www.amazon.com.tr/Apple-Watch-uyumlu-Silikon-Kay%C4%B1%C5%9F/dp/B08L2B2611/ref=sr_1_4?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=apple&qid=1651129360&s=home-theater&sr=1-4"
    data = requests.get(url, headers=headers, proxies=proxies)
    # print(url)
    soup = BeautifulSoup(data.text, "html.parser")
    # print(soup.prettify())
    pD = soup.find_all('span', {'id': "productTitle"})
    if pD:
        for pD in soup.find_all('span', {'id': "productTitle"}):
            if pD:
                ProductDescreption.append(pD.text)

    else:
        ProductDescreption.append("")

    category = soup.find_all('ul', {'class': "a-unordered-list a-horizontal a-size-small"})
    if category:
        for i in soup.find('ul', {'class': "a-unordered-list a-horizontal a-size-small"}):
            # print(i.text)
            Category.append(i.text)
        for i, n in enumerate(Category):
            Category[i] = n.strip()
        lst = (list(filter(lambda a: '›' not in a, Category)))
        Category.clear()
        z = ''
        final = []
        for i in lst:
            if i == z:
                pass
            else:
                final.append(i)
        try:
            if final[0]:
                category1 = final[0]
        except:
            category1 = ""

        try:
            if final[1]:
                category2 = final[1]
        except:
            category2 = ""

        try:
            if final[2]:
                category3 = final[2]
        except:
            category3 = ""

        try:
            if final[3]:
                category4 = final[3]
        except:
            category4 = ""
    else:
        category1 = ""
        category2 = ""
        category3 = ""
        category4 = ""
    print(category1)
    print(category2)
    print(category3)
    print(category4)

    rew = soup.find_all('span', {"id": "acrCustomerReviewText"})
    if rew:
        for i in soup.find_all('span', {"id": "acrCustomerReviewText"}):
            if i:
                # print(i)
                Review.append(i.text)
    else:
        Review.append("")

    rat = soup.find_all('span', {"class": "a-size-medium a-color-base"})
    if rat:
        for i in soup.find_all('span', {"class": "a-size-medium a-color-base"}):
            if i:
                # print(i)
                Rating.append(i.text.split("/")[0])
    else:
        Rating.append("")

    prc = soup.find_all('span', {"class": "a-price aok-align-center"})
    if prc:
        for i in soup.find_all('span', {'class': 'a-price aok-align-center'}):
            if i:
                price.append(i.text.split("TL")[0] + "TL")
                # print(i.text)
    else:
        price.append("")


#     print(url)
# print(len(ProductDescreption))

    if pD or prc:
        df = pd.DataFrame({ "Company": "Amazon" , "Category" : "Elektronic",
                              "ProductLink": url, "Descreption": ProductDescreption,
                              "Price": price, "Rating": Rating, "Review": Review,
                                "category 1" : category1 , "category 2" : category2,
                                "category 3" : category3 , "category 4" : category4})
        client = MongoClient('localhost', 27017)
        db = client['N11']
        collection = db['Amazon']
        collection.insert_many(df.to_dict('records'))

        print(df)
        price.clear()
        Rating.clear()
        Review.clear()
        ProductDescreption.clear()
    else:
        print(df)
        price.clear()
        Rating.clear()
        Review.clear()
        ProductDescreption.clear()
        pass
