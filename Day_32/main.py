from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url)
html=response.text
soup=BeautifulSoup(html,'html.parser')
listings=[]
ul=soup.find_all('ul', class_="List-c11n-8-84-3-photo-cards")

links=[]
addresses=[]
prices=[]
# Data Scraping
link = soup.select('#zpid_2056905294 > div > div:nth-of-type(1) > a')
Address = soup.select('#zpid_2056905294 > div > div:nth-of-type(1) > a > address')
price = soup.select('#zpid_2056905294 > div > div:nth-of-type(1) > div:nth-of-type(2) > div > span')

# Data Cleaning
for i in range(0,len(link)):
    links.append(link[i]['href'])
    cleaned_address=" ".join(Address[i].text.split()).replace(',','').replace(' |','')
    cleaned_address=" ".join(list(dict.fromkeys(cleaned_address.split())))
    addresses.append(cleaned_address)
    cleaned_price=price[i].text.split()[0].replace('+','').replace('/mo','')
    prices.append(cleaned_price)
    
# Data parsing
df=pd.DataFrame({
    'Address': addresses,
    'Price': prices,
    'Link': links
})  

try:
    df.to_csv('Zillow Data.csv')
    print("Data Parsed Successfully")
except:
    print("Error while Parsing Data")
