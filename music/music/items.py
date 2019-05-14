# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()   # 序号
    title = scrapy.Field()   # 歌曲名
    artist = scrapy.Field()  # 艺术家
    link = scrapy.Field()  # 歌曲链接