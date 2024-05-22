from pymongo import MongoClient
import numpy as np
import pandas as pd
import HepsiburadaPage
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
proxy  =   "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"

#options.add_argument("start-maximized")
#options.add_argument("disable-infobars")
#options.add_argument("--disable-extensions")
#options.add_argument('--proxy-server=%s' % proxy)
# proxy  =  "http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"
# driver = webdriver.Chrome(options=options,executable_path = r"D:\Users\Black Terminal\PyCharm Community Edition 2021.3.2\chromedriver.exe")
s=Service(r"C:\Users\admin\Downloads\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=s)
driver.maximize_window()
url = "https://www.hepsiburada.com/bilgisayarlar-c-2147483646?sayfa=2"
driver.get(url)
driver.implicitly_wait(30)
list = []
AppendLinks = []
productlink = []
itemDescription = []
i = 0
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
list.append(url)
while True:
    current_page_number = driver.find_element(By.XPATH,'/html/head/link[17]').text

    print(f"Processing page {current_page_number}..")

    try:
        next_page_link = driver.find_element(By.XPATH,'//*[@id="ProductList"]/div/div/link[2]').get_attribute('href')
        print(next_page_link)
        # next_page_link.click()
        driver.get(next_page_link)
        list.append(next_page_link)
        driver.implicitly_wait(10)
        links = driver.find_elements(By.XPATH, '//*[@class="productListContent-item"]/div/a')
        for link in links:
            AppendLinks.append(link.get_attribute('href'))
            print(AppendLinks)
            for i in AppendLinks:
                HepsiburadaPage.PageExtract(url=i)
    except :
        break

