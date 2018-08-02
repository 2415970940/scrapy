"""
队列先进先出
Queue(size)初始化队列
get()返回队列的最先进去的元素
put()将数据放入队列中
qsize()队列大小
full()队列是否为满
empty()队列是否为空
"""
from queue import Queue
from threading import Thread
import  time

def set_value(q):
    index = 0
    while True:
        q.put(index)
        index +=1
        time.sleep(3)

def get_value(q):
    while True:
        result = q.get()
        print(result)

def main():
    q = Queue(4)
    t1 = Thread(target=get_value,args=[q])
    t2 = Thread(target=set_value,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
