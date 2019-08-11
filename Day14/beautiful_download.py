from time import time
from threading import Thread

import requests

class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('./' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=1655e784f62741f0c0059891361d17fe&num=10')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()
