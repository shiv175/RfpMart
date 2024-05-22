import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import json
from datetime import datetime

from bs4 import BeautifulSoup

proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}

Rating = []
originalAmount = []
DP = []
merchantlink = []
campName = []
Merchantname = []
Review = []
favourite = []
category1 = []
category2 = []
category3 = []
category4 = []
category5 = []
category6 = []
category7 = []
categoryList = []
sellerName = []
DeliveryStatusName = []
OtherSupplierName = []
OtherSupplierPrice = []
Comments = []
badges = []
xyz = "https://www.trendyol.com/defacto/oversize-fit-pamuklu-kisa-kollu-basic-tisort-p-219038730?boutiqueId=610616&merchantId=1188"
# sourcecode = session.get('https://www.trendyol.com'+l,proxies=proxies, allow_redirects=False)
sourcecode = requests.get(xyz, proxies=proxies, allow_redirects=False)
print(sourcecode)
# link = 'https://www.trendyol.com' + l
# ProductLink = link
plain_text = sourcecode.text
soup = BeautifulSoup(plain_text, 'html.parser')
print(soup.prettify())

for info in soup.find_all('div', {'class': 'product-button-container'}):

    try:
        item = info.find_all_previous('h1', {'class': 'pr-new-br'})[0].text
    except:
        item = ""

    # This code fo finding Amount
    try:
        old_price = info.find_all_previous('span', {'class': 'prc-org'})[0].text.replace("TL","").replace(".","").replace(",",".")
    except:
        old_price = 0

    try :
        new_price = info.find_all_previous('span', {'class': 'prc-dsc'})[0].text.replace("TL","").replace(".","").replace(",",".")
    except:
        new_price = 0

    try:
        discount = (float(new_price)*100)/old_price
    except:
        discount = 0

    # for rating
    try:
        script = soup.findAll('script', {"type": "application/javascript"})
        data = script[1].contents[0]
        data = data.replace("window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=", "")
        data = data.split(";window.TYPageName")[0]
    except:
        print("Rating Jason array")
    try:
        json_object = json.loads(data)
        rating = json_object["product"]["ratingScore"]["averageRating"]
    except Exception as e:
        rating = ""

    #     for category
    for btn in soup.find_all("button", {"class": "add-to-basket"}):
        category = btn.find_all_previous(['a', 'span'], {'class': 'product-detail-breadcrumb-item'})
        for li in category:
            # print(li.text)
            if li:
                categoryList.append(li.text)
    a = categoryList[::-1]
    try:
        cat1 = a[0]
    except:
        cat1 = ""
    try:
        cat2 = a[1]
    except:
        cat2 = cat1
    try:
        cat3 = a[2]
    except:
        cat3 = cat2
    try:
        cat4 = a[3]
    except:
        cat4 = cat3
    try:
        cat5 = a[4]
    except:
        cat5 = cat4
    try:
        cat6 = a[5]
    except:
        cat6 = cat5
    try:
        cay7 = a[6]
    except:
        cat7 = cat6

    category.clear()

    try:
        review = info.find_all_previous('a', {'class': "rvw-cnt-tx"})[0].text
    except:
        review =""
    #     Review.append("")

# subtructvalue = datetime.now() - now
# totaltime = int(subtructvalue.total_seconds() * 1000)

Date = str(datetime.now().date())

print(item)
print(xyz)
print(new_price)
print(old_price)
print(discount)
print(rating)
print(review)
print(datetime.now())
print(Date)
# print(totaltime)
# print(Category)
print(cat1)
print(cat2)
print(cat3)
print(cat4)
print(cat5)
print(cat6)
print(cat7)

