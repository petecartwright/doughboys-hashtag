import requests
from bs4 import BeautifulSoup




PODCAST_FEED_URL = 'http://feeds.feedburner.com/Doughboys'

resp = requests.get(PODCAST_FEED_URL)

soup = BeautifulSoup(resp.content, 'xml')

items = soup.findAll('item')

episodes = []

for i in items:
    title = i.title.text.strip()
    summary = i.summary.text.strip()
    guest = title.split('with')[-1].strip()
    pubdate = i.pubDate.text.strip()
    url = i.content['url']
    episodes.append({'title': title,
                     'summary': summary,
                     'pubdate': pubdate,
                     'guest': guest,
                     'url': url
                     })

