import threading
import random
import time

gMoney = 1000
gCondition = threading.Condition()
gTime = 0
gTotalTimes = 100


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        global gTotalTimes
        while True:
            money = random.randint(100,1000)
            gTime += 1
            if gTime<=gTotalTimes:
                gCondition.acquire()
                gMoney += money
                print("%s生产%d元，剩余%d"%(threading.current_thread(),money,gMoney))
                gCondition.notify_all()
                gCondition.release()
                time.sleep(1)
            else:
                break


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gMoney >= money:
                gMoney -=money
                print("%s消费%d元，剩余%d"%(threading.current_thread(),money,gMoney))
                gCondition.release()
            else:
                while gMoney < money:
                    print("%s消费%d元，金钱不足，剩余%d"%(threading.current_thread(),money,gMoney))
                    gCondition.wait()
                gMoney -=money
                gCondition.release()
            time.sleep(1)

def main():
    for x in range(3):
        t = Producer(name="生产者%d"%x)
        t.start()

    for x in range(5):
        t = Consumer(name="消费者%d"%x)
        t.start()

if __name__ == '__main__':
    main()