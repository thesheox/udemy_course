import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {



"Request Line" : "GET / HTTP/1.1",
"Host":"myhttpheader.com",
"upgrade-insecure-requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,images/avif,images/webp,images/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

"sec-ch-ua-platform":"Windows",
"sec-fetch-site":"cross-site",
"sec-fetch-mode":"navigate",

"sec-fetch-dest":"document",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"en-US,en;q=0.9,fa;q=0.8",
"priority":"u=0, i",
"x-forwarded-proto":"https",
"x-https":"on",
"X-Forwarded-For":"5.119.169.172",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
titles=soup.find(class_="a-offscreen")
#
# song_names=[title.getText().strip() for title in titles if ":" not in title.getText().strip()]
print(soup)