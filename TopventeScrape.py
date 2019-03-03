from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
 
my_url = "https://www.cdiscount.com/jeux-pc-video-console/v-103-0.html"

# opening up connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("li", {"class":"cPdtItem jsPdtItem"})
lenght = len(containers)
# print(lenght)
container = containers[0]
# container.a
Title = container.find("div",{"class":"cPdtItTit"})
Title.text
# print(Title.text)
price = container.find("span",{"class":"price jsPrice"})
price.text
print(price.text)