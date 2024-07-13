import requests
import bs4
p=requests.get("https://tv.filmnet.ir/")
soup= bs4.BeautifulSoup(p.text,"html.parser")
name=soup.find_all("p")

for i in name:
    print(i.text)
