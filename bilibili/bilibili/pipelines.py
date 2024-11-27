# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilibiliPipeline:
    def __init__(self):
        # 在管道初始化时，打开 CSV 文件进行写入
        self.file = open('output.csv', mode='a', newline='', encoding='utf-8')
        # 定义 CSV 文件的列头
        self.writer = csv.DictWriter(self.file, fieldnames=['hits', 'likes','coin','star','turn','reply','time','release','tags'])
        # 写入列头
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 处理每个爬取到的 item，写入 CSV 文件
        self.writer.writerow({
            'hits': item.get('hits'),
            'likes': item.get('likes'),
            'coin': item.get('coin'),
            'star': item.get('star'),
            'turn': item.get('turn'),
            'reply': item.get('reply'),
            'time': item.get('time'),
            'release': item.get('release'),
            'tags': ', '.join(item.get('tags', []))  # 如果有多个标签，合并成一个字符串
        })
        return item  # 返回 item，表示处理完成

    def close_spider(self, spider):
        # 爬虫结束时，关闭 CSV 文件
        self.file.close()