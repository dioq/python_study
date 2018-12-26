# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup


# 获取html文档
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


# 获取html中所有的链接
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    list = []  # 申明空数组
    for link in soup.find_all(attrs={"class":" j-video"}):
        list.append(link.get('data-mp4'))
    return list


if __name__ == "__main__":
    url_joke = "http://www.budejie.com/video"

    html = get_html(url_joke)
    joke_content = get_certain_joke(html)
    print("=============== over ================")
    print(joke_content.count)
    print(json.dumps(joke_content))
