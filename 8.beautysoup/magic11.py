import requests
from bs4 import BeautifulSoup
import sys,os,os.path
os.environ['HTTP_PROXY']="http://10.32.100.241:8080"
os.environ['HTTPS_PROXY']="https://10.32.100.241:8080"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

url="https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality=Hadapsar&cityName=Pune"
r=requests.get(url,headers=headers,timeout=5)
c=r.content
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
#all=soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})
#print(all[0].find("div",{"class":"m-srp-card__price"}).text)