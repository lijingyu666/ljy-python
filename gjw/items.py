# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GjwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    stu = scrapy.Field()
    work = scrapy.Field()
    age = scrapy.Field()

    address = scrapy.Field()
    towork = scrapy.Field()

    salary = scrapy.Field()
    pass
