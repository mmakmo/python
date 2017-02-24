import requests
import lxml.html


def main():
    '''
    main process
    '''
    response = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        print(url)


def scrape_list_page(response):
    '''
    retrieve urls from web page
    '''
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url


if __name__ == '__main__':
    main()
