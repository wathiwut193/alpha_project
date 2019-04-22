# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""

import deepcut
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


def word_tokenize(text):
    data = deepcut.tokenize(text, custom_dict='/dictionary/custom_dict.txt')
    return data


if __name__ == '__main__':
    # connect to database on mongodb atlas cloud
    # database = "mongodb+srv://student:m789789123@cluster0-ds9da.mongodb.net/test?retryWrites=true"
    # client = MongoClient(database, connectTimeout=200)
    # check status to connect
    # print(client.status)
    # show list data base
    # print(client.list_database_names())
    # use database client
    # datanews = client.datanews
    # print(datanews.list_collection_names())

    URL = input("Enter URL:")
    news = get_news(URL)

    print(tag.tag_start(news))
    #print(tag.tag_object(news))
