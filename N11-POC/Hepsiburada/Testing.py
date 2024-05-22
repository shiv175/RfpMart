import time
from pymongo import MongoClient
import datetime
import pprint
from bson.objectid import ObjectId
from datetime import datetime
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
productlink = []
itemDescription = []
AppendLinks = []
Price = []
discount =[]
brand = []
Oldprice = []
Rating = []
Comment = []
Seller = []
Category1 = []
Category2 = []
Category3 = []
Category4 = []
Category5 = []
Category6 = []


driver = webdriver.Chrome(r"D:\Users\Black Terminal\PyCharm Community Edition 2021.3.2\chromedriver.exe")
driver.maximize_window()

url = "https://www.hepsiburada.com/erkek-sweatshirt-c-12102800?sayfa=2"

driver.get(url)
time.sleep(10)
now = datetime.now()


links = driver.find_elements(By.XPATH, '//*[@class="productListContent-item"]/div/a')
for link in links:
    AppendLinks.append(link.get_attribute('href'))
# //*[@id="DeliveryOptions_299e1d25-bc54-4687-bff9-d7da8ce18de9"]/div/div/div[2]/div/div/div[1]/div[2]

for i in AppendLinks:
    try:
        url = i
        driver.get(url)
        productlink.append(i)
        phonenames = driver.find_element(By.XPATH, '//*[@class="container"]/div/header/span')
        y = phonenames.get_attribute("innerHTML")
        itemDescription.append(y.strip())

        try:
            old = driver.find_element(By.XPATH, '//*[@id="originalPrice"]')
            Oldprice.append(old.text)
        except:
            Oldprice.append(" NaN")

        try:
            rating = driver.find_element(By.XPATH, '//*[@id="product-discount-rate"]/span[1]')
            discount.append(rating.text)
        except:
            discount.append("NaN")
        try:
            price = driver.find_element(By.XPATH, '//*[@id="offering-price"]')
            Price.append(price.text)
        except:
            Price.append(" NaN")
        try:
            rating = driver.find_element(By.XPATH, '//*[@id="detail-container"]/div/header/span')
            brand.append(rating.get_attribute('text'))
        except:
            brand.append(np.nan)

        try:
            rating = driver.find_element(By.XPATH, '//*[@id="productReviews"]/span[1]')
            Rating.append(rating.text)
        except:
            Rating.append("--")

        try:
            comment = driver.find_element(By.XPATH, '//*[@id="comments-container"]')
            Comment.append(comment.text)
        except:
            Comment.append("--")

        try:
            seller = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/main/div[3]/section[1]/div[6]/div/div[4]/div[1]/div[2]/div/div[1]/div[4]/div[1]/span/span[2]/a')
            Seller.append(seller.text)
        except:
            Seller.append("--")

        try:
            category1 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[1]/a")
            Category1.append(category1.text)
        except:
            Category1.append("-")

        try:
            category2 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[2]/a")
            Category2.append(category2.text)
        except:
            Category2.append("-")

        try:
            category3 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[3]/a")
            Category3.append(category3.text)
        except:
            Category3.append("-")

        try:
            category4 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[4]/a")
            Category4.append(category4.text)
        except:
            Category4.append("-")

        try:
            category5 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[5]/a")
            Category5.append(category5.text)
        except:
            Category5.append("-")

        try:
            category6 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/ul/li[6]/a")
            Category6.append(category6.text)

        except:
            Category6.append(" ")


        # // *[ @ id = "DeliveryOptions_299e1d25-bc54-4687-bff9-d7da8ce18de9"] / div / div / div[2] / div / div / div[1] / \
        #                                                                        div[2] / b
        delivery = driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/section[3]/div/div/div[7]/div/div/div/div/div[1]/div/div/div[2]")
        print(delivery.text)
        print(delivery)
        subtructvalue = datetime.now() - now
        x = int(subtructvalue.total_seconds() * 1000)
        print(x)

        print(len(itemDescription))
        print(len(productlink))
        print(len(Price))
        print(len(discount))
        print(len(brand))
        print(len(Oldprice))
        print(len(Rating))
        print(len(Comment))
        print(len(Seller))
        print(len(Category1))
        print(len(Category2))
        print(len(Category3))
        print(len(Category4))
        print(len(Category5))
        print(len(Category6))

        data = (
            {"Company_Name": "hepsiburada", "Category": "Electronik", "Extract date": now,"Time" : x,
             "product": itemDescription, "link": productlink,
             "price": Oldprice, "Discount": discount, " Discount price": Price,
             "Brand ": brand, "Rating": Rating, "Review": Comment, "Seller": Seller, "Category1": Category1,
             "Category2": Category2
                , "Category3": Category3, "Category4": Category4, "Category5": Category5, "Category6": Category6})

        df = pd.DataFrame(data)
        print(df)
        df.to_excel("hepsi.xlsx")

        # client = MongoClient('localhost', 27017)
        # db = client['N11']
        # collection = db['Hepsiburada']
        # collection.insert_many(df.to_dict('records'))

        Price.clear()
        discount.clear()
        brand.clear()
        Oldprice.clear()
        Rating.clear()
        Comment.clear()
        Seller.clear()
        itemDescription.clear()
        productlink.clear()
        Category1.clear()
        Category2.clear()
        Category3.clear()
        Category4.clear()
        Category5.clear()
        Category6.clear()
    except:
        pass
