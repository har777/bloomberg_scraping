import pymongo
from pymongo import MongoClient

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client.scrapy
        collection = db.my_items



    def process_item(self, item, spider):

        self.collection.insert(dict(item))
        return item