from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('Process id is {}'.format(getpid()))
    print('{} download starting.....'.format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('{} is downloaded, use {}s'.format(filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python.py',))
    p1.start()
    p2 = Process(target=download_task, args=('Matlab',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total time is {}s'.format(end - start))

if __name__ == '__main__':
    main()
