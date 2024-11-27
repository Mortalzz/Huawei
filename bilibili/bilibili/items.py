# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 播放量
    hits = scrapy.Field()
    #点赞量
    likes=scrapy.Field()
    #tags
    tags=scrapy.Field()
    #投币
    coin=scrapy.Field()
    #收藏
    star=scrapy.Field()
    #转发
    turn=scrapy.Field()
    #评论
    reply=scrapy.Field()
    #视频时长
    time=scrapy.Field()
    #发布日期
    release=scrapy.Field()
    pass
