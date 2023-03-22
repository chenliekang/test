import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['quanguo.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/']
    start_urls = ['http://quanguo.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/']

    def parse(self, response):
        # 获取的是响应的字符串
        # content = response.text
        # 获取的是二进制数据
        # content = response.body
        # 可以直接是xpath方法来解析response中的内容
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print('===========================')
        # 提取selector对象的data属性值
        print(span.extract())
