import pymongo
from pymongo import MongoClient

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client.data
        collection = db.items



    def process_item(self, item, spider):

        self.db["items"].insert(dict(item))
        return item