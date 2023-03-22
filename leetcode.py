def test():
	ide_list = [
		{
			"shutcut": 'i',
			"name": "IDEL",
			"link": "https://docs.python.org/3/library/idle.html",
			"desc": "Python 内置的IDE，功能比较一般"
		},
		{
			"shutcut": 'v',
			"name": "VIM",
			"link": "http://www.vim.org/",
			"desc": "如果你是个VIM爱好者，可以用VIM编写Python，但是Python的缩进处理会比较麻烦。当然，你在 Linux 服务器上的时候有时候就只能用VI/VIM了。"
		},
		{
			"shutcut": 'c',
			"name": "VSCode",
			"link": "https://code.visualstudio.com/",
			"desc": "VSCode 对Python的支持非常友好，配合几个插件后几乎是对 Python 开发最友好的IDE了"
		},
		{
			"shutcut": 'p',
			"name": "PyCharm",
			"link": "https://www.jetbrains.com/pycharm/",
			"desc": "jetbrains 出品的 PyCharm 也是 Python 开发者常用的IDE"
		}
	]

	ide_dict = {}
	short_cuts = []
	for ide in ide_list:
		s = ide['shutcut']
		ide_dict[s] = ide
		short_cuts.append(s)

	print("常见的 Python IDE 列表：")
	for s in ide_dict:
		print('* {}: {}'.format(s, ide_dict[s]['name']))

	while True:
		print('')
		ret = input("请选择你喜欢的IDE({}, q退出)：".format('/'.join(short_cuts)))
		if ret == 'q':
			break

		ide = ide_dict.get(ret)
		if ide is None:
			print("[错误] 不支持的选项")
		else:
			print("* IDE: {}".format(ide['name']))
			print("* 链接: {}".format(ide['link']))
			print("* 描述: {}".format(ide['desc']))

if __name__ == '__main__':
	test()