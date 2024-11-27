import re
from scrapy_redis.spiders import RedisSpider
import scrapy
import json

from bilibili.items import BilibiliItem


class TagsSpider(RedisSpider):
    name = "tags"
    redis_key ="tags:start_urls"
    tids=[17,171,172,65,173,121,136,19]
    #171=3000，172=10000，17=3000，65=6000
    def parse(self, response):
        for tid in self.tids:
            temp=1
            while True:
                yield scrapy.Request(url='https://api.bilibili.com/x/web-interface/newlist?rid='+str(tid)+'&type=0&ps=30&pn='+str(temp),callback=self.bvid_parse)
                temp=temp+1
                if temp>=2000:
                    break



    def bvid_parse(self,response):
        js=json.loads(response.text)
        if not js.get('data', {}).get('archives'):
            return None
        else:
            for data in js['data']['archives']:
                str1=data['bvid']
                yield scrapy.Request(url='https://www.bilibili.com/video/'+str(str1),callback=self.info_parse)

    def info_parse(self,response):
        pattern_tags = re.findall(r'"tag_name"\s*:\s*"([^"]+)"', response.text)
        match = re.search(r'"view"\s*:\s*(\d+).*?"reply"\s*:\s*(\d+).*?"favorite"\s*:\s*(\d+).*?"coin"\s*:\s*(\d+).*?"share"\s*:\s*(\d+).*?"like"\s*:\s*(\d+).*?', response.text)
        match1 = re.search(r'"duration"\s*:\s*(\d+)', response.text)
        match2 = re.search(r'"pubdate"\s*:\s*(\d+)', response.text)
        item=BilibiliItem()
        item['hits']=match.group(1)
        item['likes']=match.group(6)
        item['coin'] = match.group(4)
        item['star'] = match.group(3)
        item['turn'] = match.group(5)
        item['reply'] = match.group(2)
        item['time']=match1.group(1)
        item['release']=match2.group(1)
        item['tags']=pattern_tags
        yield item