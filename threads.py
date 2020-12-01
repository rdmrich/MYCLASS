from time import sleep
from threading import *

'''
main thread
t1
t2
'''


class hello(Thread):

    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)


class hi(Thread):

    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)


t1 = hello()
t2 = hi()

t1.start()
sleep(0.3)
t2.start()
t1.join()
t2.join()
print('bye')
