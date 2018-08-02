import threading

VALUE=0

# def value_add():
#     global VALUE
#     for x in range(1000000):
#         VALUE+=1
#     print(VALUE)
# # result
# # 1000000
# # 1149096


gLock = threading.Lock()

def value_add():
    global VALUE
    gLock.acquire()
    for x in range(1000000):
        VALUE+=1
    gLock.release()
    print(VALUE)

def main():
    for i in range(2):
        t = threading.Thread(target=value_add)
        t.start()

if __name__ == '__main__':
    main()