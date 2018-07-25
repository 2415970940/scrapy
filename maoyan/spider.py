import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool
from bs4 import BeautifulSoup

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        # proxies = {'http':'http://125.120.204.138:6666','https':'https://125.120.205.253:6665'}
        # response = requests.get(url,headers = headers,proxies = proxies)
        response = requests.get(url,headers = headers)
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')


def main():
    url = "http://maoyan.com/board/4"
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(1, 4)])
    pool.map(main, groups)
    pool.close()
    pool.join()