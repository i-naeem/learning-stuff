# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PcpartsItem(Item):
    title = Field()
    brand = Field()
    price = Field()
    media = Field()
    rating = Field()
    in_stock = Field()
    description = Field()
