# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""

import requests
from bs4 import BeautifulSoup

import time
from pymongo import MongoClient
import os
import glop
import tag_object as tag


# - *- coding: utf- 8 - *-

# function get news from website thairath only
def get_news(URL):
    data = requests.get(URL)
    soup = BeautifulSoup(data.text, 'html.parser')
    header = soup.find_all("h1")
    date_news = soup.find_all("div", {"class": "css-1cxbv8p evs3ejl7"})
    content = soup.find_all("p")

    text = ''
    # for i in header:
    #   text += i.text
    # for z in date_news:
    #    text += z.text
    for j in content:
        text += j.text

    return text


if __name__ == '__main__':
    URL = input("Enter URL:")
    news = get_news(URL)
    print(tag.tag_start(news))
