from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from bloomberg2.items import Bloomberg2Item

class MySpider(CrawlSpider):
    name = "bloomberg_spider"
    allowed_domains = ["bloomberg.com"]
    start_urls = ["http://www.bloomberg.com/"]

    rules = (Rule (SgmlLinkExtractor(allow=("/news/*",))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        res = Selector(response)
        items = []
        item = Bloomberg2Item()
        item["title"] = res.xpath('//title/text()').extract()
        item["text"] = res.xpath('//div[@itemprop="articleBody"]/p/text()').extract()
        items.append(item)
        print " "
        print " "
        print " "
        print item
        print " "
        print " "
        print " "
        return item