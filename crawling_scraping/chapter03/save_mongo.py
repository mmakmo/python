import lxml.html
from pymongo import MongoClient


tree = lxml.html.parse('index.html')
html = tree.getroot()

client = MongoClient('127.0.0.1', 27017)
# get 'scraping' database
db = client.scaping
# get links collection
collection = db.links
# delete all collection documents
collection.delete_many({})

for a in html.cssselect('a'):
    collection.insert_one({
        'url': a.get('href'),
        'title': a.text,
    })

for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])
