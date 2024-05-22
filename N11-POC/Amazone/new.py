import requests
from bs4 import BeautifulSoup

import AmazonePage
# from Amazone import PageExtractAmazone

site = 'https://www.amazon.com.tr/gp/sign-in.html'

session = requests.Session()


session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': site
}

'''get login page'''
resp = session.get(site)
html = resp.text

'''get BeautifulSoup object of the html of the login page'''
soup = BeautifulSoup(html, 'lxml')

#print(soup.prettify())

'''scrape login page to get all the needed inputs required for login'''
data = {}
form = soup.find('form', {'name': 'signIn'})
for field in form.find_all('input'):
    try:
        #print("Name",field['name'])
        #print("value",field['value'])
        data[field['name']] = field['value']

    except:
        pass

data[u'email'] = "pathiktrivedi5@gmail.com"
data[u'password'] = "Hybrid1234"

proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}

'''submit post request with username / password and other needed info'''
print("Before ",session)
post_resp = session.post('https://www.amazon.com.tr/ap/signin', data = data,proxies=proxies)
print(post_resp.status_code)
print("After ",session)
#print(post_resp.content)

post_soup = BeautifulSoup(post_resp.content, 'lxml')
#print(post_soup)
print(post_soup.find_all('title')[0].text)

if post_soup.find_all('title')[0].text == 'Your Account':
    print('Login Successfull')
else:
    print('Login Failed')

#working link
#singleproduct =  session.get("https://www.amazon.com.tr/Samsung-Galaxy-M52-128-Siyah/dp/B09K42QYM6/ref=nav_ya_signin/?_encoding=UTF8&ref_=nav_ya_signin&th=1",proxies=proxies)
singleproduct =  session.get("https://www.amazon.com.tr/Microsonic-Samsung-Galaxy-K%C4%B1l%C4%B1f-Transparent/dp/B09MQVJHGD/ref=pd_rhf_ee_s_pd_sbs_rvi_sccl_1_3/260-9359180-2649569?pd_rd_w=bmcuV&content-id=amzn1.sym.f16f922a-48f2-4c32-b8b1-bcc51d10173b&pf_rd_p=f16f922a-48f2-4c32-b8b1-bcc51d10173b&pf_rd_r=2H0SHSM8V3R7YDZXQB6C&pd_rd_wg=1XIRe&pd_rd_r=f7fe6968-6e7f-405b-b727-01f1c355ad6d&pd_rd_i=B09MQVJHGD&psc=1",proxies=proxies)
print("Later ",session)

productsoup = BeautifulSoup(singleproduct.text,'lxml')
#print(productsoup)
url = "https://www.amazon.com.tr/s?k=jacket&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=D59D8H1B0L6E&sprefix=jacket%2Caps%2C205&ref=nb_sb_noss_1"
AmazonePage.PagExtract(session=session,url= url)
# PageExtractAmazone.getdata(session=session)

#print(productsoup.prettify())