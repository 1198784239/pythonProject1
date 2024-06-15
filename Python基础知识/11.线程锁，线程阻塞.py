# 线程锁
import threading
L = []
# 上锁
S = threading.Lock()

def work01():
    global L
    # 上锁
    S.acquire()
    for i in range(1,5):
        L.append(i)
        print('work01执行')
     # 解锁
    S.release()


def work02():
    global L
    # 上锁
    S.acquire()
    for i in range(5,10):
        L.append(i)
        print('work02执行')
    # 解锁
    S.release()

t1 = threading.Thread(target=work01)
t2 = threading.Thread(target=work02)

t1.start()
t2.start()

# 线程阻塞
t1.join()
t2.join()
print(L)
print('主线结束')

