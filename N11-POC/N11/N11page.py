import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import openpyxl
import pandas as pd
import numpy as np
import json


def pageExtraction(url):
    from datetime import datetime


    session = requests.session()
    proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    # url = "https://www.n11.com/arama?q=telefonu"
    # source_code = requests.get(url)
    source_code = session.get(url,proxies=proxies, allow_redirects=False)
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
    #print(plain_text)
    #source_code.headers['content-type']
    soup = BeautifulSoup(plain_text,'html.parser')
    # print(soup)
    # print(soup.prettify())



    for link in soup.find_all('a',{'class':'plink'}):
        links.append(link.get('href'))
        # print(links)

    for i in links:
        now = datetime.now()
        source_code = requests.get(i , proxies=proxies,allow_redirects=False)
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
        try:
            rating = json_object1["itemListElement"][0]["name"]
            # print(rating)
            if rating:
                category1.append(rating)
                # print(rating)
        except:
            category1.append("-")

        try:
            rating = json_object1["itemListElement"][1]["name"]
            # print(rating)
            if rating:
                category2.append(rating)
                # print(rating)
        except:
            category2.append("-")

        try:
            rating = json_object1["itemListElement"][2]["name"]
            # print(rating)
            if rating:
                category3.append(rating)
                # print(rating)
        except:
            category3.append("-")

        try:
            rating = json_object1["itemListElement"][3]["name"]
            # print(rating)
            if rating:
                category4.append(rating)
                # print(rating)
        except:
            category4.append("-")

        try:
            rating = json_object1["itemListElement"][4]["name"]
            # print(rating)
            if rating:
                category5.append(rating)
                # print(rating)
        except:
            category5.append("-")

        try:
            rating = json_object1["itemListElement"][5]["name"]
            # print(rating)
            if rating:
                category6.append(rating)
                # print(rating)
        except:
            category6.append("")

        try:
            rating = json_object1["itemListElement"][6]["name"]

            if rating:
                category7.append(rating)
                # print(rating)
        except:
            category7.append("-")
        subtructvalue = datetime.now() - now
        x = int(subtructvalue.total_seconds() * 1000)
        print(now)
        print(datetime.now())
        print(x)
        df = pd.DataFrame(
            {"Company": "N11" , "Category" : "Elektronik","Extract date" : now,"Time" : x,"Links": Productlinks,
             "Descreption": Itemdescreption, "Price": Price, "Rating": Rating, "Review": Review,
             "Delivery" : y ,
             "category 1 ": category1, "category 2 ": category2, "category 3 ": category3, "category 4 ": category4,
             "category 5 ": category5,
             "category 6 ": category6, "category 7 ": category7})

        # data = pd.DataFrame(df)
        # data.to_excel("N11.xlsx")

        client = MongoClient('localhost', 27017)
        db = client['N11']
        collection = db['N11']
        collection.insert_many(df.to_dict('records'))

        # data = pd.DataFrame(df)
        # data.to_excel("N11.xlsx" , index= False)

        Review.clear()
        Itemdescreption.clear()
        Price.clear()
        Rating.clear()
        oldprice.clear()
        category1.clear()
        category2.clear()
        category3.clear()
        category4.clear()
        category5.clear()
        category6.clear()
        category7.clear()
        Productlinks.clear()

        print(df)







