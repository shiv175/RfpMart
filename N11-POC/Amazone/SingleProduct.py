import requests
from bs4 import BeautifulSoup

proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}


links = []
price = []
Review = []
Rating = []
Category = []
ProductDescreption = []
url = "https://www.amazon.com.tr/WOON-WN32DAL04-READY-LED-TRWNDLD032138800/dp/B08R6422RJ/ref=sr_1_17?qid=1651211465&refinements=p_n_feature_eight_browse-bin%3A13710998031%7C13710999031%7C13711000031%7C13711001031%7C13711002031%7C13711003031&s=home-theater&sr=1-17"
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
        print(i.text)
        Category.append(i.text)
    for i, n in enumerate(Category):
        Category[i] = n.strip()
    lst = (list(filter(lambda a: '›' not in a, Category)))
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
    for i in range(1,4):
        category[i] = ""


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

print(url)
print(category1)
print(category2)
print(category3)
print(category4)
# print(Category)
new = []
# for i in Category:
#     if '\n' in i:
#         i.replace('\n','')
#         new.append(i)
#         print(i)

# for i in new:
#     if i == "\n":
#         i = i.replace("\n", " ")
# print(new)



