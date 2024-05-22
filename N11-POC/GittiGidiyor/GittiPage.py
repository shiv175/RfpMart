import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from pymongo import MongoClient
from datetime import datetime
# url = "https://www.gittigidiyor.com/saat"
def pageExtract(url):


    itemDescription = []
    now   = datetime.now()
    links = []
    session = requests.session()
    proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
    # url = 'https://www.gittigidiyor.com/cep-telefonu-aksesuar/kilif'
    # url = "https://www.gittigidiyor.com/saat"
    # source_code = requests.get(url)
    source_code = session.get(url,proxies=proxies, allow_redirects=False)

    plain_text = source_code.text

    soup = BeautifulSoup(plain_text,'html.parser')

    #print(soup.prettify())

    for productdescription in soup.findAll('h3',{'class':'medium'}):
        #print(productdescription.text)
        itemDescription.append(productdescription)
    print(len(itemDescription))
    for link in soup.findAll('a',{'rel':'bookmark'}):
        print(link.get('href'))
        links.append(link.get('href'))
    print(len(links))

    OriginalPrice = []
    DiscountPrice = []
    disCount = []
    ProductDescription = []
    subDescription = []
    productLinks = []
    Rating = []
    Review = []
    Seller = []
    category1 = []
    category2 = []
    category3 = []
    category4 = []
    category5 = []
    category6 = []
    a = []



    for ProductLinks in links:
        productLinks.append(ProductLinks)
        source_code = session.get(ProductLinks,proxies=proxies, allow_redirects=False)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for p in soup.findAll('button', {'id': 'buy-now'}):
            previous_price = p.findAllPrevious()
            # print(previous_price)
            original_price = p.findAllPrevious('span', {'id': 'sp-price-highPrice'})
            discount_price = p.findAllPrevious('div', {'class': 'lowPrice lastPrice'})
            disCountPercentage = p.findAllPrevious('span', {'id': 'sp-price-discountPercentage'})
            prodD = p.findAllPrevious('h1', {'class': 'title r-onepp-title'})
            subD = p.findAllPrevious('span', {'id': 'sp-subTitle'})
            Comment = p.find('span', {'id' : 'sp-reviewCommentCount'})
            seller = p.find_all_previous(['span'], {'class': 'member-nick'})

            if original_price:
                for o in original_price:
                    # print(o.text)
                    OriginalPrice.append(o.text.strip())
                    # print(o.text.strip())
            else:
                OriginalPrice.append("")
            if discount_price:
                for d in discount_price:
                    DiscountPrice.append(d.text.strip())
                    # print(d.text.strip())
            else:
                DiscountPrice.append("")
            if disCountPercentage:
                for dis in disCountPercentage:
                    disCount.append(dis.text.strip())
                    # print(dis.text.strip())
            else:
                disCount.append("")
            if prodD:
                for pD in prodD:
                    ProductDescription.append(pD.text.strip())
                    # print(pD.text.strip())
            else:
                ProductDescription.append("")
            if subD:
                for sD in subD:
                    subDescription.append(sD.text.strip())
                    # print(sD.text.strip())
            else:
                subDescription.append("")
            # if Comment:
            #     for ct in Comment:
            #         comment.append(ct.text)

        for li in seller:
            if li:
                Seller.append(li.text)
            else:
                Seller.append("")

        blank = soup.find_all(['strong'], {'class': 'catalog-review-point'})
        if blank:
            for li in soup.find_all(['strong'], {'class': 'catalog-review-point'}):
                for r in blank:
                    if r:
                        Rating.append(r.text)
        else:
            Rating.append(" ")
        blank = soup.find_all(['span'], {'class': 'catalog-review-count'})
        if blank:
            for li in soup.find_all(['span'], {'class': 'catalog-review-count'}):
                # print(li)
                if li:
                    Review.append(li.text)
        else:
            Review.append(" ")
        for btn in soup.find_all("button", {"class": "control-button gg-ui-button plr10 gg-ui-btn-primary showModal"}):
            if btn:
                category = btn.find_all_previous(['ul', 'li', 'span', 'a'],
                                                 {
                                                     'class': 'clearfix hidden-breadcrumb robot-productPage-breadcrumb-hiddenBreadCrumb hidden-m'})
                # print(soup.find_all(['ul','li','span','a'], {'class': 'clearfix hidden-breadcrumb robot-productPage-breadcrumb-hiddenBreadCrumb hidden-m'}))
                for li in category:
                    if li:
                        li.replace_with("\n\n\n\n\n\n")
                        a.append((li.text).strip())
                new = []
                # print(new)
                # print(a)
                for str in a:
                    for w in str:
                        if w == " ":
                            pass
                        else:
                            new.append(w)
                a.clear()
                list = []
                last = ""
                for i in new:
                    if i == "\n":
                        i = i.replace("\n", " ")
                        list.append(i)

                    else:
                        list.append(i)
                new.clear()
                last = last.join(list)
                final = []
                list.clear()
                list.append(last)

                for sp in list:
                    while "  " in sp:
                        sp = sp.replace("  ", " ")
                final = sp.replace(" ", ",")
                wordList = final.split(",")
                try:
                    if wordList[0]:
                        category1.append(wordList[0])
                except:
                    category1.append("")
                try:
                    if wordList[1]:
                        category2.append(wordList[1])
                except:
                    category2.append("")
                try:
                    if wordList[2]:
                        category3.append(wordList[2])
                except:
                    category3.append("")
                try:
                    if wordList[3]:
                        category4.append(wordList[3])
                except:
                    category4.append("")
                try:
                    if wordList[4]:
                        category5.append(wordList[4])
                except:
                    category5.append("")
                try:
                    if wordList[5]:
                        category6.append(wordList[5])
                except:
                    category6.append("")
            else:
                for i in range(1, 7):
                    category(i).append("-")
            # print(category1, category2, category3, category4, category5, category6)
            wordList.clear()
        try:
            for i in soup.find_all("span", {"class": "shippingTimeDetail"}):
                delivery = i.text.strip()
        except:
            delivery = ""


        subtructvalue = datetime.now() - now
        totaltime = int(subtructvalue.total_seconds() * 1000)
        print(now)
        print(datetime.now())
        print(totaltime)

        # print(len(Rating))
        # print(Rating)
        # print(len(Seller))
        # print(len(ProductDescription))
        # print(len(category6))
        # print(len(category1))
        # print(len(category2))
        # print(len(category3))
        # print(len(category4))
        # print(len(category5))
        # print(len(OriginalPrice))
        # print(len(subDescription))
        # print(len(DiscountPrice))
        # print(len(disCount))
        # print(len(Review))

        df = pd.DataFrame(
            {"Company_Name": "gittigidiyor", "Category": "Non  Catlog", "ProductDescription": ProductDescription,
             "Sub Description": subDescription,"Extract date" : now,"Time" : totaltime,
             "Original Price": OriginalPrice, "Discount Price": DiscountPrice,
             "Campaigns": disCount, "Seller": Seller,
             "Rating": Rating, "Review": Review, "ProductLinks": ProductLinks,"Delivery" : delivery,
             "category 1": category1, "category 2": category2,
             "category 3": category3, "category 4": category4, "category 5": category5,
             "category 6": category6})
        print(df)



        data = pd.DataFrame(df)
        data.to_excel("file.xlsx")

        # client = MongoClient('localhost', 27017)
        # db = client['N11']
        # collection = db['GittiGidiyor']
        # collection.insert_many(df.to_dict('records'))

        OriginalPrice.clear()
        DiscountPrice.clear()
        disCount.clear()
        ProductDescription.clear()
        subDescription.clear()
        productLinks = []
        Rating.clear()
        Review.clear()
        Seller.clear()
        category1.clear()
        category2.clear()
        category3.clear()
        category4.clear()
        category5.clear()
        category6.clear()
        a.clear()






# obj = pageExtract(url="https://www.gittigidiyor.com/saat" )



