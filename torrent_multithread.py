import threading
from multiprocessing import Pool, cpu_count
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


def get_urls():
    """ get all sci-hub-torrent url
    """
    source_url = 'http://gen.lib.rus.ec/scimag/repository_torrent/'
    urls_list = []
    try:
        req = requests.get(source_url)
        soups = BeautifulSoup(req.text, 'lxml').find_all('a')
        for soup in soups:

            if '.torrent' not in soup.text:
                continue

            url = source_url + soup.text
            print(url)
            urls_list.append(url)
    except Exception as error:
        print(error)
    finally:
        return urls_list


lock = threading.Lock()     # global lock


def urls_crawler(url):
    """
    crawl sci-hub-torrent file
    :param url:
    :return:
    """
    save_path = 'torrent/'
    try:
        print('Crawling: ' + url)
        req = requests.get(url, allow_redirects=True)
        with open(save_path + url.split('/')[-1], 'wb') as fd:
            fd.write(req.content)

    except Exception as error:
        print(error)


if __name__ == '__main__':
    urls = get_urls()
    pool = Pool(processes=cpu_count())
    try:
        pool.map(urls_crawler, urls)
    except Exception as error:
        print(error)





