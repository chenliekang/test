from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class ftp_server:
    def __init__(self):
        # 实例化DummyAuthorizer来创建ftp用户
        self.authorizer = DummyAuthorizer()
        # 参数：用户名，密码，目录，权限
        self.authorizer.add_user('admin', '123456', r'C:\Users\95111\Desktop\test', perm='elradfmwMT')
        # 匿名登录
        # authorizer.add_anonymous('/home/nobody')
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer
        # 参数：IP，端口，handler
        self.server = FTPServer(('0.0.0.0', 2121), self.handler)  # 设置为0.0.0.0为本机的IP地址
        self.server.serve_forever()


def cut_screen(title, savepath):
    ftp = ftp_server()
    pass

    # 截图 title:窗口名称 savepath:所截图片存储路径
    # hwnd = win32gui.FindWindow(None, title)
    # app = QApplication(sys.argv)
    # screen = QApplication.primaryScreen()
    # pix = screen.grabWindow(hwnd)
    # pix.save(savepath)


if __name__ == "__main__":
    # time.sleep(5)
    title = u'开具增值税专用发票'
    savepath = "123.jpg"
    cut_screen(title, savepath)