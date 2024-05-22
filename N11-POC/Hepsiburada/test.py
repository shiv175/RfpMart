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

now = datetime.now()
productlink = []
itemDescription = []
AppendLinks = []
Price = []
discount = []
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

url = "https://www.hepsiburada.com/lenovo-v15-g2-intel-core-i5-1135g7-8gb-ram-256gb-ssd-windows-10-home-15-6-fhd-tasinabilir-bilgisayar-82kb000rtx-p-HBCV00000YOLKK"
driver.get(url)
# productlink.append(i)
delivery = driver.find_element(By.CLASS_NAME,
                               'merchant-name small')
print(delivery.text)

driver.close()
