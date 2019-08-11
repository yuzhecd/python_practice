from random import randint
from time import time, sleep

def download_task(filename):
    print('{} download starting.....'.format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('{} is downloaded, use {}s'.format(filename, time_to_download))

def main():
    start = time()
    download_task('Python.py')
    download_task('Matlab')
    end = time()
    print('Total time is {}s'.format(end - start))

if __name__ == '__main__':
    main()
