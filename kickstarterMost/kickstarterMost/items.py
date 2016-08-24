# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KickstarterMostItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    cat = scrapy.Field()
    title = scrapy.Field()
    blurb = scrapy.Field()
    desc = scrapy.Field()
    rewards = scrapy.Field()
