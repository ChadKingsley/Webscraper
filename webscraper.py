#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/linux-unix-oreilly-books"
tierDict = {}

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

#Bundle Tiers
tiers = soup.select(".dd-game-row")

for tier in tiers:
    #only for headline
    if tier.select(".dd-header-headline"):
        #grab tier name and price
        tiername = tier.select(".dd-header-headline")[0].text.strip()
        #grab tier product names
        productNames = tier.select(".dd-image-box-caption")
        productNames = [prodName.text.strip() for prodName in productNames]
        #add one product tier to our datastructure
        tierDict[tiername] = {"products": productNames}

#old tiers
tierHeadlines = soup.select(".dd-header-headline")
strippedTiernames = [tier.text.strip() for tier in tierHeadlines]

#product Names
productNames = soup.select(".dd-image-box-caption")
strippedProductnames = [prodName.text.strip() for prodName in productNames]


##common access pattern
for tiername,tierinfo in tierDict.items():    #ouput datastructure info
    print(tiername)
    print("products:")
    print(", ".join(tierinfo['products']))
    print("\n\n")

