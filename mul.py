#-*- coding=utf8 -*-
import multiprocessing
import time
def fuc(msg):
    for i in range(3):
        print(msg)
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=fuc, args=("hello",))
    p.start()
    p.join()
    print("sub-process done")