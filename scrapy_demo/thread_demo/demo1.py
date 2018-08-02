import threading
import time

def coding():
    for x in range(3):
        print("Coding....%s"%x)
        time.sleep(1)

def painting():
    for x in range(3):
        print("Painting....%s"%x)
        time.sleep(1)

def main():
    t1=threading.Thread(target=coding)
    t2=threading.Thread(target=painting)

    t1.start()
    t2.start()



if __name__ == "__main__":
    main()
