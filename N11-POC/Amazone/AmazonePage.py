import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient

def PagExtract(url , session):


    links = []
    price = []
    Brand = []
    Category = []
    Review = []
    Rating = []
    pl = []
    ProductDescreption = []
    proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',}

    # url = 'https://www.amazon.com.tr/s?k=telefon+k%C4%B1l%C4%B1f%C4%B1&i=electronics&bbn=12466497031&rh=n%3A12466496031%2Cn%3A13709880031%2Cn%3A13709897031%2Cn%3A13710045031&dc&crid=1CDD0QS38YZGE&qid=1646648386&rnid=12466496031&sprefix=telefon+k%C4%B1l%C4%B1f%C4%B1%2Caps%2C190&ref=sr_nr_n_10'
    # url = "https://www.amazon.com.tr/s?bbn=13709907031&rh=n%3A13709907031%2Cp_n_feature_sixteen_browse-bin%3A13710916031&dc&qid=1651139321&rnid=13710915031&ref=lp_13709907031_nr_p_n_feature_sixteen_browse-bin_0"
    #data = requests.get(url,proxies=proxies, allow_redirects=False)
    data = session.get(url,headers=headers)
    print(data)
    soup = BeautifulSoup(data.text,"html.parser")

    print(soup.prettify())

    for link in soup.find_all('a',{'class':"a-link-normal s-no-outline"}):
        # print(link)
        links.append('https://www.amazon.com.tr'+link.get('href'))

    # for pD in soup.find_all('span',{'class':"a-size-base-plus a-color-base a-text-normal"}):
    #     ProductDescreption.append(pD.text)
    print(len(links))
    for ur in links:

        data = session.get(ur, headers=headers,  allow_redirects=False)
        # print(url)
        soup = BeautifulSoup(data.text, "html.parser")
        # print(soup.prettify())
        pD = soup.find_all('span',{'id':"productTitle"})
        if pD:
            for pD in soup.find_all('span', {'id': "productTitle"}):
                if pD:
                    ProductDescreption.append(pD.text)

                    print(pD.text)

        else:
            ProductDescreption.append("")
        pl.append(ur)
        # rew = soup.find_all('span', {"id": "acrCustomerReviewText"})
        # if rew:
        #     for i in soup.find_all('span', {"id": "acrCustomerReviewText"}):
        #         if i:
        #             # print(i)
        #             Review.append(i.text)
        #         else:
        #             Review.append("")

        rat = soup.find_all('span', {"class": "a-size-medium a-color-base"})
        if rat:
            for i in soup.find_all('span', {"class": "a-size-medium a-color-base"}):
                if i:
                    # print(i)
                    Rating.append(i.text.split("/")[0])
        else:
            Rating.append("")

        # b = soup.find_all('a', {"id": "bylineInfo"})
        # if b:
        #     for i in soup.find_all('a', {"id": "bylineInfo"}):
        #         if i:
        #             # print(i)
        #             Brand.append(i.text.split(": ")[1])
        # else:
        #     Brand.append("")

        prc = soup.find_all('span',{"class":"a-price aok-align-center"})
        if prc:
            for i in soup.find_all('span',{'class':'a-price aok-align-center'}):
                if i:
                    price.append(i.text.split("TL")[0]+"TL")
                    # print(i.text)
        else:
            price.append("")


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

        print(url)
        print(len(ProductDescreption))
        print(len(pl))
        print(len(price))
        print(len(Rating))
        print(len(Review))


    # df = pd.DataFrame({
    #
    #                               "ProductLink": url, "Descreption": ProductDescreption, "Brand " : Brand,
    #                               "Price": price, "Rating": Rating, "Review": Review,
    #                               })
    df = pd.DataFrame({

                                  "ProductLink": pl, "Descreption": ProductDescreption,
                                  "Price": price, "Rating": Rating,
                                  })
    x = pd.ExcelWriter("amazon-jacket.xlsx", engine="xlsxwriter")
    df.to_excel(x, sheet_name='Sheet1', index=False)
    x.save()

        # client = MongoClient('localhost', 27017)
        # db = client['N11']
        # collection = db['Amazon']
        # collection.insert_many(df.to_dict('records'))

        # print(df)
        # price.clear()
        # Rating.clear()
        # Review.clear()
        # ProductDescreption.clear()
        # print(Review)
    # # print(len(Review))
    # # print(len(price))
    # print(Rating)
    # print(links)
    # print(price)
    # print(ProductDescreption)
        # for btn in soup.find_all('input',{"id":"add-to-cart-button"}):
        #     if btn:
        #         # print(btn)
        #         for price in soup.find_all_previous(['div','h1','span'],{'class':'a-section a-spacing-none'}):
        #             price.append(price.text)
                 # print(price)
                    # if price:
                    #     print(price.text)
                    # else:
                    #     print("can't find")
        # for btn in soup.find_all('div',{"class":"a-button-stack"}):
        #     if btn:
        #         print(btn)
        #         category = btn.find_all_previous(['div','ul','li','span','a'],{'class':"a-subheader a-breadcrumb feature"})
        #         for i in category:
        #             print(i.text)
