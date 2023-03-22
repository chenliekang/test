from multiprocessing import Process
import _thread
import threading
import time
import traceback
import queue

exitFlag = 0
# threadLock = threading.Lock()
# threads = []
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print('开始线程：' + self.name)
        process_data(self.name, self.q)
        # 获取锁，用于线程同步
        # threadLock.acquire()
        # print_time(self.name, self.counter, 3)
        print('退出线程：' + self.name)
        # 释放锁，开启下一个线程
        # threadLock.release()


def coding(language):
    """子进程要执行的代码"""
    for i in range(5):
        print("{} coding".format(language), end=' | ')
        time.sleep(1)


def print_time(threadName, delay, counter):
    # count = 0
    # while count < 5:
    #     time.sleep(delay)
    #     count += 1
    #     print('%s:%s' % (threadName, time.ctime(time.time())))
    while counter:
        # if exitFlag:
        #     threadName.exit()
        time.sleep(delay)
        print('%s:%s' % (threadName, time.ctime(time.time())))
        counter -= 1


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print('%s processing %s' % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


if __name__ == '__main__':
    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        pass

    # 通知线程是时候退出
    exitFlag = 1

    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主程序")

    # # 创建新线程
    # thread1 = myThread(1, "Thread-1", 1)
    # thread2 = myThread(2, "Thread-2", 2)
    #
    # # 开启新线程
    # thread1.start()
    # thread2.start()
    #
    # # 添加线程到线程列表
    # threads.append(thread1)
    # threads.append(thread2)
    #
    # # thread1.join()
    # # thread2.join()
    # # 等待所有线程完成
    # for t in threads:
    #     t.join()
    # print("退出主线程")

    # try:
    #     _thread.start_new_thread(print_time, ('Thread-1', 2, ))
    #     _thread.start_new_thread(print_time, ('Thread-2', 4, ))
    # except Exception as e:
    #     traceback.print_exc()
    #     print(e)
    #
    # while 1:
    #     pass

    # # 多进程
    # p = Process(target=coding, args=('python', ))
    # p.start()
    # for i in range(5):
    #     print("main program", end=' | ')
    #     time.sleep(1)