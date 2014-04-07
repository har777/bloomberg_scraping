from scrapy.item import Item, Field

class Bloomberg2Item(Item):
    title = Field()
    text = Field()

