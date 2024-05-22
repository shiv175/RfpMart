import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import json
from datetime import datetime
session = requests.session()
#session.trust_env = False
#headers = {'User-Agent': 'Mozilla/5.0'}
#headers = {
#    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
#}
def pageExtraction(url):

    proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}

    #url = 'https://www.trendyol.com/kapak-ve-kilif-x-c104026'
    #url = 'https://www.trendyol.com/tencere-x-c1191'

    #source_code = session.get(url,proxies=proxies, timeout=3, )
    x = datetime.now()
    source_code = session.get(url,proxies=proxies, allow_redirects=False)
    y = datetime.now() - x
    totaltime = int(y.total_seconds() * 1000)
    print(totaltime)
    #print(source_code.content)
    showContent = BeautifulSoup(source_code.text, "html.parser")
    # print(showContent.prettify())

    itemDescription = []
    links = []
    for productdescribtion in showContent.find_all('div',{'class':'p-card-chldrn-cntnr'}):
        #print(productdescribtion.text)

        # print(productdescribtion.find('a').get('href'))
        links.append(productdescribtion.find('a').get('href'))


    Rating = []
    originalAmount = []
    DP = []
    merchantlink = []

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

    for l in links:
        sourcecode = session.get('https://www.trendyol.com'+l,proxies=proxies, allow_redirects=False)
        link = 'https://www.trendyol.com'+l
        ProductLink = link
        plain_text = sourcecode.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup.prettify())
        discountprice = ''
        orginialprice = ''
        findmerchentInformation = ''

        for newprice in soup.find_all('div', {'class': 'product-button-container'}):
            discountprice = newprice.find_all_previous('span', {'class': 'prc-org'})
            orginialprice = newprice.find_all_previous('span', {'class': 'prc-slg'})
            AmountDescription = newprice.find_all_previous('span', {'class': 'prc-dsc'})
            findmerchentInformation = newprice.find_all_previous('a', {'class': 'merchant-text'})
            review  = newprice.find_all_previous('a',{'class' : "rvw-cnt-tx"})
            item = newprice.find_all_previous('h1',{'class' : 'pr-new-br'})
            # print(type(soup.find_all_previous()))
            #print('orginialprice',orginialprice)
            #print('discountprice',discountprice)
            if item:
                for i in item:
                    itemDescription.append(i.text)
                    print(i.text)

            if discountprice:
                for price in discountprice:
                    originalAmount.append(price.text)
                    # print("https://www.trendyol.com" + links)
            else:
                if AmountDescription:
                    for pDes in AmountDescription:
                        originalAmount.append(pDes.text)
                else:
                    originalAmount.append("")
                #originalAmount.append("")
                #print('original price', price)
                #print('original price', price.text)

            if orginialprice:
                for originalP in orginialprice:
                    DP.append(originalP.text)
            else:
                DP.append("")
                #print("https://www.trendyol.com" + links)
                #print('Discounted price', originalP)
                #print('Discounted price',originalP.text)
               # print(soup.prettify())
            if merchantlink:
                for merchanat in findmerchentInformation:
                    # print(merchanat.text)
                    # print(merchanat.get('href'))
                    merchantlink.append(merchanat.text)
            else:
                merchantlink.append("")

            if merchantlink :
                for merchanat in findmerchentInformation:
                    Merchantname.append(merchanat.text)
            else:
                Merchantname.append("")


            script = soup.findAll('script', {"type": "application/javascript"})
            data = script[1].contents[0]
            data = data.replace("window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=", "")
            data = data.split(";window.TYPageName")[0]
            try:
                json_object = json.loads(data)
                rating = json_object["product"]["ratingScore"]["averageRating"]
                if rating:
                    Rating.append(rating)
                else:
                    Rating.append(0)
            except:
                pass

            for btn in soup.find_all("button", {"class": "add-to-basket"}):
                category = btn.find_all_previous(['a', 'span'], {'class': 'product-detail-breadcrumb-item'})
                # print(soup.find_all(['ul','li','span','a'], {'class': 'clearfix hidden-breadcrumb robot-productPage-breadcrumb-hiddenBreadCrumb hidden-m'}))
                for li in category:
                    # print(li.text)
                    if li:
                        categoryList.append(li.text)
            #print(categoryList)
            a = categoryList[::-1]
            #print(a)
            if a[0]:
                category1.append(a[0])
            else:
                category1.append("")
            if a[1]:
                category2.append(a[1])
            else:
                category2.append("")
            if a[2]:
                category3.append(a[2])
            else:
                category3.append("")
            if a[3]:
                category4.append(a[3])
            else:
                category4.append("")
            if a[4]:
                category5.append(a[4])
            else:
                category5.append("")
            if a[5]:
                category6.append(a[5])
            else:
                category6.append("")
            try :
                if a[6]:
                    category7.append(a[6])
            except:
                category7.append("")
            # print(category1, category2, category3, category4, category5, category6, category7)

            category.clear()

            if review :
                for stars in review:
                    Review.append(stars.text)
            else:
                Review.append("")
        for btn in soup.find_all("button", {"class": 'add-to-basket'}):
            # print(btn)
            try:
                fav = btn.find_all_next('div', {'class': 'fv-dt'})
                if fav:
                    for f in fav:
                        # print(f.text)
                        if f:
                            favourite.append(f.text)
                else:
                    favourite.append(" ")
            except:
                pass

        df = pd.DataFrame(
            {"Company": "Trendyol" , "Category" : "Non Catlog","item description": itemDescription, "Original Amount": originalAmount, "DisCountPrice": DP,
             "Product Link": ProductLink,
             "Merchent Link": merchantlink, "Review": Review, "Seller": Merchantname, "Rating": Rating,
             "favourite": favourite, "Category 1 ": category1, "Category 2 ": category2, "Category 3 ": category3,
             "Category 4": category4,
             "Category 5 ": category5, "Category 6 ": category6, "Category 7 ": category7})

        # client = MongoClient('localhost', 27017)
        # db = client['N11']
        # collection = db['Trendyol']
        # collection.insert_many(df.to_dict('records'))
        print(df)

        category1.clear()
        category2.clear()
        category3.clear()
        category4.clear()
        category5.clear()
        category6.clear()
        category7.clear()
        originalAmount.clear()
        DP.clear()
        merchantlink.clear()

        Review.clear()
        Merchantname.clear()
        itemDescription.clear()
        favourite.clear()
        Rating.clear()
        # print(len(Rating))


    print(len(category1))
    print(len(category2))
    print(len(category3))
    print(len(category4))
    print(len(category5))
    print(len(category6))
    print(len(category7))
    print(len(originalAmount))
    print(len(DP))
    print(len(merchantlink))
    print(len(ProductLink))
    print(len(Review))
    print(len(Merchantname))
    print(len(itemDescription))
    print(len(favourite))
    print(len(Rating))
    print(len(Rating))

    print(itemDescription)



# print("Original Amount",len(originalAmount))
# print(originalAmount)
# print("Discount Amount", len(DP))
# print(DP)
# print("Merchent Link",len(merchantlink))
# print(merchantlink)
# # df.insert(3,'Original Amount',originalAmount)
# df.insert(4,"DiscountAmount",DP)
# df.insert(5,"Merchent Link",merchantlink)

    WriteDataFrame = pd.DataFrame({ "item description" : itemDescription,"Original Amount":originalAmount,"DisCountPrice":DP,"Product Link": ProductLink ,
                                "Merchent Link":merchantlink,"Review" : Review,"Seller" : Merchantname,"Rating" : Rating,
                               "favourite" : favourite,"Category 1 ": category1,"Category 2 ": category2,"Category 3 ": category3,"Category 4": category4,
                                "Category 5 ": category5,"Category 6 ": category6,"Category 7 ": category7})

# "Item description": df['Description'],