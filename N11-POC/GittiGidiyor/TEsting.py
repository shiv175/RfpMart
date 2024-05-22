# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import GittiPage
#
# df = pd.read_excel(r"C:\Users\admin\Downloads\n11.xls")
#
# for i in df["URL"]:
#     print(i)
# # print(df)
# #
# # # data = pd.Series(df)
# # data = pd.DataFrame(df)
# # print(data)
# # # print(data)
# # for i in data.iteritems():
# #     print(i)
#     session = requests.session()
#     proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
#
#     root_url = i
#
#     html = requests.get(root_url, proxies=proxies, allow_redirects=False)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     # print(soup.prettify())
#     pages = []
#     paging = soup.find("div", {"class": "d8kjk0-0 gEPcey"}).find("ul", {"class": "sc-12aj18f-3 kLmKCh"}).find_all("li")
#     start_page = paging[1].text
#     last_page = paging[len(paging) - 2].text
#     print(last_page)
#     url = root_url.rstrip(root_url[-1])
#     for i in range(int(start_page), int(last_page) + 1):
#         pages.append(url + format(i))
#         print(url +format(i))
#
#     for page in pages:
#         try:
#             GittiPage.pageExtract(url=page)
#             print(page)
#
#         except:
#             pass


import requests
from bs4 import BeautifulSoup
session = requests.session()
proxies = {"http": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
url = 'https://www.gittigidiyor.com/cep-telefonu-ve-aksesuar/iphone-13-pro-max-kilif-silikon-magsafe-ozellikli-seffaf-darbe-korumali-hdfyb_pdp_733086916'
source_code = session.get(url, proxies=proxies, allow_redirects=False)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
print(soup.prettify())

