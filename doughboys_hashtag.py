import os
import datetime

import requests
from bs4 import BeautifulSoup

PODCAST_FEED_URL = 'http://feeds.feedburner.com/Doughboys'


def create_download_directory():
    if not os.path.exists('downloads/'):
        os.makedirs('downloads/')


def download_file(url):
    local_filename = 'downloads/' + url.split('/')[-1]
    
    r = requests.get(url, stream=True)    

    if r.status_code == 200:
        total_length = r.headers.get('content-length')
        if total_length is None:
            return 'Error downloading {0}'.format(url)    
        else:
            data_length = 0
            total_length = int(total_length)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=total_length/50): 
                    data_length += len(chunk)
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                    amount_done = int(100 * data_length / total_length)
                    print '{0} percent done'.format(amount_done)
            return local_filename
    else:
        return 'Error downloading {0}'.format(url)


def get_episode_info_from_items(items):
    # parse out the episode information
    episodes = []
    for i in items:
        title = i.title.text.strip()
        summary = i.summary.text.strip()
        guest = title.split('with')[-1].strip()
        pubdate = i.pubDate.text.strip()
        url = i.content['url']
        filename = url.split('/')[-1]

        episodes.append({'title': title,
                         'summary': summary,
                         'pubdate': pubdate,
                         'guest': guest,
                         'url': url,
                         'filename': filename,
                         'local_path': ''
                         })

    return episodes


def main():

    # get the XML from the RSS feed, break it down by each item
    resp = requests.get(PODCAST_FEED_URL)
    soup = BeautifulSoup(resp.content, 'xml')
    items = soup.findAll('item')
    
    episodes = get_episode_info_from_items(items)
    
    create_download_directory()

    # download all of the episodes to a local folder
    for e in episodes:
        if os.path.isfile('downloads/'+e['filename']):
            print u'File exists for {0}'.format(e['title'])
        else:
            print u'about to download {0}'.format(e['title'])
            start_time = datetime.datetime.now()
            local_filename = download_file(e['url'])
            e['local_path'] = local_filename
            end_time = datetime.datetime.now()
            print u'done downloading {0}'.format(e['title'])    
            print 'Elapsed time {0}'.format(str(end_time - start_time))
        print '------------------------------------------'
        print '------------------------------------------'



if __name__ == '__main__':
    main()

