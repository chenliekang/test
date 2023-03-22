import os
import time
import subprocess
from win32com.client import GetObject

sap_path = "C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe"
ip_path = '10.141.146.24'
computer = '200_05'


if __name__ == '__main__':
    try:
        os.system('TASKKILL /F /FI "USERNAME eq ' + computer + '" /IM "saplogon.exe"')
    except:
        pass
    subprocess.Popen(sap_path)
    time.sleep(10)
    con = GetObject("SAPGUI").GetScriptingEngine
    con.OpenConnectionByConnectionString(ip_path)