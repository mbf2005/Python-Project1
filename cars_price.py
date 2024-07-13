import requests
import bs4

site = requests.get("https://karnameh.com/car-price")
soup = bs4.BeautifulSoup(site.text, "html.parser")
cars_name = soup.find_all(class_="MuiTypography-root MuiTypography-body1 muirtl-iy5bpq")
cars_price = soup.find_all(class_="MuiTypography-root MuiTypography-body1 muirtl-22intj")

name1=[] ; price1=[]
for i in cars_name:
    name1.append(i.text)
for i in cars_price:
    price1.append(i.text)
i=0
while(i<len(cars_name)):
    print(name1[i],"=",(price1[i]))
    i+=1



    