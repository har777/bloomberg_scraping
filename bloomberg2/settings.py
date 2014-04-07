# Scrapy settings for bloomberg2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bloomberg2'

SPIDER_MODULES = ['bloomberg2.spiders']
NEWSPIDER_MODULE = 'bloomberg2.spiders'


ITEM_PIPELINES = [
  'scrapy_mongodb.MongoDBPipeline',
]

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'my_items'
#MONGODB_UNIQUE_KEY = 'url'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bloomberg2 (+http://www.yourdomain.com)'
