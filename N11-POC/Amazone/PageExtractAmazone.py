import requests
from bs4 import BeautifulSoup
import AmazonePage

proxies = {"https": "http://HWF:Hybrid2022_country-tr@proxy.iproyal.com:12323"}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
Range = []
# url = 'https://www.amazon.com.tr/s?k=telefon+k%C4%B1l%C4%B1f%C4%B1&i=electronics&bbn=12466497031&rh=n%3A12466496031%2Cn%3A13709880031%2Cn%3A13709897031%2Cn%3A13710045031&dc&crid=1CDD0QS38YZGE&qid=1646648386&rnid=12466496031&sprefix=telefon+k%C4%B1l%C4%B1f%C4%B1%2Caps%2C190&ref=sr_nr_n_10'
url ="https://www.amazon.com.tr/s?rh=n%3A13710329031&fs=true&ref=lp_13710329031_sar"
# data = requests.get(url,proxies=proxies, allow_redirects=False)
root_url = "https://www.amazon.com.tr/s?i=electronics&rh=n%3A13710329031&fs=true&page={}&qid=1651231931&ref=sr_pg_{}"
data = requests.get(url, headers=headers, proxies=proxies)
print(data)
soup = BeautifulSoup(data.text, "html.parser")
page =  soup.find_all('span',{'class':"s-pagination-item s-pagination-disabled"})
for i in page:
    print(i)
    Range.append(i.text)
print(int(Range[0]))
start = 1
end = int(Range[0])

for i in range(start,end):
    try:
        AmazonePage.PagExtract(url = root_url.format(i,i))
    except:
        pass
