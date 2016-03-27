# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    status = scrapy.Field()
    desc = scrapy.Field(serializer=str)

