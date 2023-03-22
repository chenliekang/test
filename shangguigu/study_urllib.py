import json
import urllib.request
import urllib.parse
import urllib.error


# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
# print(type(response))

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 读取多行
# content = response.readlines()
# print(content)

# 返回状态码
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取状态信息
# print(response.getheaders())

# 下载网页
# urllib.request.urlretrieve(url, 'baidu.html')

# 下载图片
# url_img = 'https://img1.baidu.com/it/u=1722277522,2436167607&fm=253&fmt=auto&app=138&f=JPEG?w=499&h=500'
# urllib.request.urlretrieve(url=url_img, filename='lisa.jpg')

# 下载视频
# url_video='https://vd2.bdstatic.com/mda-md5n98c7ksyk46dk/sc/cae_h264/1617695285/mda-md5n98c7ksyk46dk.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1676853632-0-0-21755acf885e2a67540bc71d5676be47&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0631923122&vid=6240707458453892396&abtest=&klogid=0631923122'
# urllib.request.urlretrieve(url_video, 'gk.mp4')

# 使用代理
# url = 'https://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# print(content)

# 编码
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&fenlei=256&rsv_pq=0xfb749c750023809f&rsv_t=710aRFJeJWj91gxs1IyNb7QTgg8RGXu1neRQLjrJhfcWueTgsHmJSQAJY7VA&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=12&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6&rsp=5&inputT=5223&rsv_sug4=5223
# 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码
# 单个编码
# url = 'https://www.baidu.com/s?wd='
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# name = urllib.parse.quote('周杰伦')
# url = url + name
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# print(content)
# 多个编码
# data = {
#     'wd': '周杰伦',
#     'sex': '男'
# }
# a = urllib.parse.urlencode(data)
# print(a)

# post请求
# url = 'https://fanyi.baidu.com/sug'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# data = {
#     'kw': 'spider'
# }
# # post请求方式的参数必须编码
# data = urllib.parse.urlencode(data).encode('utf-8')
# request = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# obj = json.loads(content)
# print(obj)
# url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# headers = {
#     'Accept': '*/*',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Acs-Token': '1676883606819_1676973052980_PrWY6o4l7e5bIX48MUwcDankRiDDFXJEJp8LF0ntCvvRvHDhb/wo0PwBN5GnW5K61SOepapmef3H6ecmNYYcJn4f6jfv3fHlgazLyTPaXSLZmzEwyd1xVL/JIcn9jpofEUvS2j9Prr1Gbmw+mtYaLjwiBVhNPYWc7+hyo6VNmNL62ao6whEMGBD+epn3dW3H/0JkOiLK/uliKiO2o+weQU39xsNbeReMEOAIwhDwd3bZ4DYhoAyf39EEcaMV0b8GphJbRfBPOhJN1acgTKFpe9ywXvM8X4uehBMK0AT4YsAN0gFQHp6uqQnN/hYyty06pWN8DpUq2U9+Tw1M+hM/kg==',
#     'Connection': 'keep-alive',
#     'Content-Length': '135',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': 'BIDUPSID=165C11E9570781A0EB04DC3E0856F166; PSTM=1659540076; BAIDUID=165C11E9570781A0B5DBDCC52D74336A:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-315%3A346%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36554_38112_38092_38124_37906_38176_38171_38244_37937_38089_26350_37284_38008_37881; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1675825854,1675923990,1676939261,1676949526; BAIDUID_BFESS=165C11E9570781A0B5DBDCC52D74336A:FG=1; PSINO=5; delPer=0; BA_HECTOR=8l0581a52gag80a18k858hpl1hv931b1l; ZFY=XIRi8vxRzpqfMn6Dhrd:ANjK:A20lziBGybn71hYZznDA:C; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1676971657; ab_sr=1.0.1_M2Q3NTBlMGVkMDY2YmI2NzMyNTU1NDgxNmEyNWEyNThlMDdhNWQ0ODJlZjFlMjY3ZDA3Y2QzMjA1MDliMGIzMzA5YjE1YzVmMzQ0MzQ2YWQ0YWRiYjI4ZWZmYmEwNjExZDIyMjc4YTdkMjgzNTM3ZWIyZTlhOWE0YjVhYjk5ZTI4NjY4NzE5ZjBkYWM2MjIxMjk3OTdmNWQ1NGE3ZWIzZg==',
#     'Host': 'fanyi.baidu.com',
#     'Origin': 'https://fanyi.baidu.com',
#     'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
#     'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest'
# }
# data = {
#     'from': 'en',
#     'to': 'zh',
#     'query': 'love',
#     'transtype': 'realtime',
#     'simple_means_flag': '3',
#     'sign': '198772.518981',
#     'token': '828af2db11a84df24c055acf28e63740',
#     'domain': 'common'
# }
# data = urllib.parse.urlencode(data).encode('utf-8')
# request = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# obj = json.loads(content)
# print(obj)

# # ajax-post
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# data = {
#     'cname': '北京',
#     'pid': '',
#     'pageIndex': 1,
#     'pageSize': '10'
# }
# data = urllib.parse.urlencode(data).encode('utf-8')
# request = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('kfc_1.json', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# 异常
# url = 'https://blog.csdn.net/m0_64336780/article/details/1274545111'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# try:
#     request = urllib.request.Request(url=url, headers=headers)
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     print(content)
# except urllib.error.HTTPError:
#     print('系统正在升级。。。')

# 微博的cookie登陆
# 个人信息页面是utf-8，但还是报编码错误，因为并没有进入到个人信息页面，而是跳转到了登陆页面，登陆页面不是utf-8，所以会报错
# url = 'https://weibo.cn/7752966978/info'
# headers = {
#     'cookie': '_T_WM=2cb11749391c23edff653dd09e97e6b5; SCF=AjWGjFzsZTCq87ENyA3FRO0Nysyy5vUy208gqIvJPU86Ax0Rlwph-xcDAm5T5tWeTTQ_s7P6jz3NXxU7rnjPBbM.; SUB=_2A25O8dnpDeRhGeFJ7lAY9ijFzDSIHXVqHeehrDV6PUNbktAGLRj4kW1Nf75XtjZpzALTR1zeTSVpa6LIh4Sl2snl; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhH5n5VqjYIRkIFqmyN8S9Z5JpX5KMhUgL.FoMNSKz4Soq4S0n2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0-E1Kqc1KMR; SSOLoginState=1677044153; ALF=1679636153',
#     'referer': 'https://weibo.cn/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('weibo.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# handler处理器
url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
# (1)获取handler对象
handler = urllib.request.HTTPHandler()
# (2)获取opener对象
opener = urllib.request.build_opener(handler)
# (3)调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
