# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""

import tag_object as tag
import word_tokenize as wt
import spell_checking as sc
import rule
import class_object as obj
import pymongo
from pymongo import MongoClient

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    # while (True):
    # URL = input("Enter URL:")
    # news = wt.get_news(URL)
    # print(news)
    # print(news.split("\n"))

    # warning ! i found the problem with function get_news change to read file
    news_read = open("raw_data/input/news_2.txt", mode='r', encoding='utf-8')
    news = news_read.read()

    """
    before load data to function word tokenize we use tag date and time because we found problem with word tokenize.
    they split date and time  which we don't want it to be like that.
    """
    tag_date = tag.tag_date(news)
    tag_time = tag.tag_time(tag_date)
    tag_person = tag.tag_person(tag_time)
    """
    word token and tag action and location
    """
    word_tokenize = wt.word_segment_identify_tag(tag_person)
    tag_object = tag.tag_start(word_tokenize)
    print("this a tag result " + tag_object)
    print(" ")
    result = tag_object.replace("|", "")
    """
    edit wrong word from <fail>
    """
    result = sc.Autocorrection(result)
    print(" ")
    print("this true result " + result)

    """
    function test rule discover crime 
    """
    # list_p = []  # value read to keep on database
    # list_2d = rule.rule_strat(result)
    # for i in range(len(list_2d)):
    #      for j in range(len(list_2d[i])):
    #         list_p.append(list_2d[i][j].__dict__)
    #
    # print(list_p)
    """
    insert data to database 
    """
    #
    # client = MongoClient('localhost', 27017)
    # db = client.get_database("datanews")
    # news = db.news
    # news.insert_many(list_p)

