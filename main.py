import requests
from bs4 import BeautifulSoup

url = 'https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E596&insId=1&radius=0.0&minPrice=&maxPrice=900&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare='

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='l-searchResult')

for result in results:
    price = result.find('span', class_='propertyCard-priceValue').text.strip()
    address = result.find('address', class_='propertyCard-address').text.strip()
    print(price, address)