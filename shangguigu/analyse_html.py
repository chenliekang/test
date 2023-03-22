from lxml import etree
import urllib.request

# xpath解析本地文件
# tree = etree.parse('xpath_use.html')
# print(tree)
# li_list = tree.xpath('//ul/li[@id]/text()')
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')
# print(li_list)
# li = tree.xpath('//ul/li[@id="l1"]/@class')
# print(li)
# li_list = tree.xpath('//ul/li[contains(@id, "l")]/text()')
# li_list = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# li_list = tree.xpath('//ul/li[@id="l1" or @id="l2"]/text()')
# li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
# print(li_list)

# xpath解析服务器响应文件
# url = 'http://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# tree = etree.HTML(content)
# result = tree.xpath('//input[@id="su"]/@value')
# print(result)


# 下载前十页图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
