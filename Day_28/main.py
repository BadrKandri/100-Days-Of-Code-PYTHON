from bs4 import BeautifulSoup
import requests
import smtplib
from config import get_mail_info

# scraping the price
url = "https://www.amazon.com/Dell-OptiPlex-Computer-Quad-Core-Processor/dp/B0BLQNXY8B/ref=sr_1_3?crid=2GR02YBML1BQB&dib=eyJ2IjoiMSJ9.HdxYNBCKSxl0qddLonbpDj05RPiWKzOpngSSvd0KA3_hChXikRsVGwLFWntBfiKJ2LWKRuC1vl0kcYpJiyB8_9XLSBORZe1SkPV3Ng6oQqNe2MCkt1dRVm5QIlUAN25lzzyLUu09K7FR_Zc5MBe0UHOOrLW-2goxCyw-g-eIRY3y8dHrUa4K3_-qzISnOA-JGhCVQ4k-5NzB76pOn1kqAedX3wvtJkShasSCJfSK87Q.xYtHHIzBaV3ULkBFcl80g96mt4LtddrFpqIOIx6qiD8&dib_tag=se&keywords=full%2Bgamer%2Bpc%2Bsetup&qid=1740868069&sprefix=full%2Bgamer%2Bpc%2Bsetup%2Caps%2C186&sr=8-3&th=1"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0 (Edition Campaign 34)",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org"
}
html=requests.get(url,headers).text
soup=BeautifulSoup(html,'html.parser')
price=soup.find(class_="a-offscreen")
price=float(price.get_text().split('$')[1])
title = soup.find(id="productTitle").get_text().strip()
#print(f'{title}\n{price}')

# mail alert
my_mail,password,receiver = get_mail_info()
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()#secure my mail
connection.login(user=my_mail,password=password)
message=f"{title}'s price has finally dropped to ${price}! Don't miss out\n\n{url}"

if price<=300:
    connection.sendmail(from_addr=my_mail,to_addrs=receiver,msg=f"Subject: AMAZON PRICE ALERT!!\n\n{message}")
    connection.close()
    print(f"Email is sent to: {receiver}")
    
