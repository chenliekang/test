# cython: language_level=3

import time
import calendar

# ticks = time.time()
# print('当前时间戳为：', ticks)

# localtime = time.localtime(time.time())
# localtime = time.asctime(time.localtime(time.time()))
# print('本地时间为：', localtime)

# # 格式化成 年-月-日 时:分:秒 形式
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#
# # 格式化成 星期 月 日 时：分：秒 年 形式
# print(time.strftime('%a %b %d %H:%M:%S %Y'), time.localtime())
#
# # 将格式字符串转换为时间戳
# a = 'Sat Mar 28 22:24:24 2016'
# print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))


def func():
    cal = calendar.month(2016, 1)
    print('以下输出2016年1月份的日历：')
    print(cal)
