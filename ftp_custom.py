from ftplib import FTP
import os
import traceback


# 连接ftp
def ftpconnect(host, port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


# 从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置的缓冲区大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)   # 参数为0，关闭调试模式
    fp.close()


# 从ftp下载整个目录下文件
def DownLoadFileTree(ftp, LocalDir, RemoteDir):  # 下载整个目录下的文件
    print("remoteDir:", RemoteDir)
    if not os.path.exists(LocalDir):
        os.makedirs(LocalDir)
    ftp.cwd(RemoteDir)
    RemoteNames = ftp.nlst()
    print("RemoteNames", RemoteNames)
    for file in RemoteNames:
        Local = os.path.join(LocalDir, file)
        print(ftp.nlst(file))
        if file.find(".") == -1:
            if not os.path.exists(Local):
                os.makedirs(Local)
            DownLoadFileTree(ftp, Local, file)
        else:
            downloadfile(ftp, file, Local)
    ftp.cwd("..")
    return


# 从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    # host, port, username, password
    ftp = ftpconnect("192.168.101.5", 2121, "admin", "123456")
    try:
        # 从ftp下载整个目录下文件
        DownLoadFileTree(ftp, "C:/Users/95111/Desktop/test", '/')
    except Exception as e:
        traceback.print_exc()
        print(e)
    # 下载文件，第一个是ftp服务器路径下的文件，第二个是要下载到本地的路径文件
    downloadfile(ftp, "/home/ftpuser/files/", "C:/Users/95111/Desktop/test/")
    # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
    uploadfile(ftp, '/upload/1.txt', "C:/Users/Administrator/Desktop/1.txt")
    # ftp.close() #关闭ftp
    # #调用本地播放器播放下载的视频
    # os.system('start D:\soft\kugou\KGMusic\KuGou.exe C:\Users\Administrator\Desktop\ftp\test.mp3')

    print(ftp.getwelcome())     # 打印出欢迎信息
    # 获取当前路径
    pwd_path = ftp.pwd()
    print("FTP当前路径:", pwd_path)
    # 显示目录下所有目录信息
    # ftp.dir()
    # 设置FTP当前操作的路径
    ftp.cwd('/upload/')
    # 返回一个文件名列表
    filename_list = ftp.nlst()
    print(filename_list)

    ftp.mkd('目录名')  # 新建远程目录
    ftp.rmd('目录名')  # 删除远程目录
    ftp.delete('文件名')  # 删除远程文件
    ftp.rename('fromname', 'toname')  # 将fromname修改名称为toname

    # 逐行读取ftp文本文件
    file = '/upload/1.txt'
    # ftp.retrlines('RETR %s' % file)
    # 与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8KB）下载的数据
    # ftp.retrbinary('RETR %s' % file)