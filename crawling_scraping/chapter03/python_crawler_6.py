import time
import re
import requests
import lxml.html


def main():
    '''
    main process
    '''
    session = requests.Session()
    response = session.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        time.sleep(1)
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)


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
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text,
        'content': [normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')],
    }
    return ebook


def normalize_spaces(s):
    '''
    replace blanks to one blank, and trim
    '''
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
