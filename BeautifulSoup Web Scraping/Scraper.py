from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

with open('scraped-data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'Video URL'])

    for article in soup.find_all('article'):
        try:
            print('-'*20)
            headline = article.h2.a.text
            print('*', headline)

            summary = article.find('div', class_='entry-content').p.text
            print('*', summary)

            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f'http://youtube.com/watch?v={vid_id}'
            print('*', yt_link)
            print('-'*20)

            csv_writer.writerow([headline, summary, yt_link])

        except TypeError:
            continue
