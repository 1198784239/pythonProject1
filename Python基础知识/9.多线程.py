import threading
import time
from concurrent.futures import thread


# function - 线程函数。
# args - 传递给线程函数的参数,他必须是个tuple类型。
# kwargs - 可选参数

#为线程定一个函数
# !/usr/bin/python
# -*- coding: UTF-8 -*-

from concurrent.futures import ThreadPoolExecutor
from thread import Thread

def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    #创建一个线程
    t1 = Thread(target =func,args=("李克聪",))
    # 启动线程
    t1.start()

    t2 = Thread(target =func,args=("周杰伦",))
    t2.start()

# #创建线程池
# with ThreadPoolExecutor(max_workers=5) as executor:
#     #把任务提交给线程池
#     for i in range(5000):
#         executor.submit(func, i)