import time
import re
import requests
import lxml.html
from pymongo import MongoClient


def main():
    '''
    main process
    '''
    client = MongoClient('127.0.0.1', 27017)
    collection = client.scraping.ebooks
    collection.create_index('key', unique=True)

    session = requests.Session()
    response = session.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        key = extract_key(url)
        ebook = collection.find_one({'key': key})
        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
            collection.insert_one(ebook)


def scrape_list_page(response):
    '''
    retrieve urls from web page
    '''
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(response):
    """
    get detail page info as dict type
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text,
        'content': [normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')],
    }
    return ebook


def extract_key(url):
    """
    get key from url
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)


def normalize_spaces(s):
    '''
    replace blanks to one blank, and trim
    '''
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
