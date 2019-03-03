from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
 
my_url = "https://www.cdiscount.com/jeux-pc-video-console/v-103-0.html"

# opening up connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("li", {"class":"cPdtItem jsPdtItem"})
# lenght = len(containers)
# print(lenght)

csv_file = open('topventes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['game', 'price'])


container = containers[0]
# container.a
for container in containers:
	title = container.find("div",{"class":"cPdtItTit"})
	game = title.text
# print(Title.text)
	price = container.find("span",{"class":"price jsPrice"})
	price = price.text.strip()
# print(price.text)
	print("game: " + game)
	print("price: " + price)
	game = game.encode("utf-8")
	price = price.encode("utf-8")

	csv_writer.writerow([game, price])

csv_file.close()



