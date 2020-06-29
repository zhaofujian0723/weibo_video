# -*- coding: utf-8 -*-

import requests


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}


def start(url):
    content = requests.get(url, headers=headers).content
    print(content)


if __name__ == '__main__':
    url = "https://weibo.com/tv/v/IFF1X7aCZ?fid=1034:4499192328945687"
    start(url)

