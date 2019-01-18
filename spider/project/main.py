# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup

def getHtml(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

# 解析html
def paramserHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    list = []  # 申明空数组
    for link in soup.find_all(attrs={"class":"g-list"}):
        list.append(link.get('data-mp4'))
    return list


if __name__ == "__main__":
    url_target = "http://news.duowan.com/tag/377717538395.html"

    html = getHtml(url_target)
    joke_content = paramserHtml(html)
    print("=============== over ================")
    print(joke_content.count)
    print(json.dumps(joke_content))
