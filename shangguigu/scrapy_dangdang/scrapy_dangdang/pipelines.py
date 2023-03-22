# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道的话，那么必须在settings中开启管道
class ScrapyDangdangPipeline:
    def open_spider(self, spider):
        # 在爬虫文件开始之前就执行的一个方法
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # （1）write方法必须要写一个字符串，而不能是其他的对象
        # （2）w模式会每一个对象都打开一次文件，覆盖之前的内容
        self.fp.write(str(item))

        return item

    def close_spider(self, spider):
        # 在爬虫文件执行完之后执行的方法
        self.fp.close()


import urllib.request


# 多条管道开启
# （1）定义管道类
# （2）在settings中开启管道，'scrapy_dangdang.pipelines.DangDangDownloadPipeline': 301
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
