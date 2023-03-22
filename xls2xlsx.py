import os
import win32com
from win32com.client import Dispatch


def xls_xlsx(path):
    # 调用excel程序
    w = win32com.client.Dispatch('Excel.Application')
    # 后台运行，不显示，不警告
    w.Visible = 0
    w.DisplayAlerts = 0
    # 打开excel工作簿
    wb = w.Workbooks.Open(path)
    # 这里必须要绝对地址，保持和xls路径一致
    newpath = allpath + '\\转换后的文档.xlsx'
    '''
    FileFormat = 51，表示xlsx扩展文件；
    FileFormat = 56，表示xls扩展文件；
    FileFormat = 52，表示xlsm扩展文件；
    FileFormat = 23，表示csv扩展文件；
    '''
    wb.SaveAs(newpath, FileFormat=51)
    w.Quit()    # 退出
    return newpath


allpath = os.getcwd()
print(allpath)
xls_xlsx(allpath + '\\转换前的文档.xls')