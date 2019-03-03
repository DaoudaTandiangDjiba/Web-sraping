from bs4 import BeautifulSoup 
import requests
import csv

source = requests.get('https://coreyms.com').text 

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.findAll('article'):

#print(article.prettify())

	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)


	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
		# print(vid_src)

		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
		# print(vid_id)

		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None

	print(yt_link)

	print()

	csv_writer.writerow([headline.encode("utf-8"), summary.encode("utf-8"), yt_link.encode("utf-8")])

csv_file.close()

