import psutil
import os, datetime, time


def getMemCpu():
    data = psutil.virtual_memory()
    total = data.total
    free = data.available
    memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + " "
    cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
    return memory + cpu


if __name__ == '__main__':
    while True:
        print(psutil.cpu_percent())
        print(psutil.virtual_memory().percent)
        print('-----------')
        time.sleep(1)