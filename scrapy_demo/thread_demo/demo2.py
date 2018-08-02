import threading
import time

class CodingTread(threading.Thread):
    def run(self):
        for x in range(3):
            print("Coding....%s"%x)
            time.sleep(1)

class PaintingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("Painting....%s"%x)
            time.sleep(1)

def main():
    t1 = CodingTread()
    t2 = PaintingThread()
    t1.start()
    t2.start()



if __name__ == "__main__":
    main()