import requests
from bs4 import BeautifulSoup


def get_torrents():
    """
    Get all torrents link
    :return:
    """
    source_url = 'http://gen.lib.rus.ec/scimag/repository_torrent/'
    save_path = 'sci-hub-torrent/'
    try:
        req = requests.get(source_url)
        soups = BeautifulSoup(req.text, 'lxml').find_all('a')
        for soup in soups:
            if '.sci-hub-torrent' not in soup.text:
                continue
            print(source_url + soup.text)
            torrent_url = source_url + soup.text
            torrent = requests.get(torrent_url, allow_redirects=True)
            with open(save_path + soup.text, 'wb') as f:
                f.write(torrent.content)
    except Exception as error:
        print(error)


get_torrents()

