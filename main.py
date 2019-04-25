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
    URL = input("Enter URL:")
    news = wt.get_news(URL)
    print(news)
    print(news.split("\n"))

    tag_date = tag.tag_date(news)
    tag_time = tag.tag_time(tag_date)
    tag_person = tag.tag_person(tag_time)

    word_tokenize = wt.word_segment_identify_tag(tag_person)
    tag_object = tag.tag_start(word_tokenize)
    print(tag_object)
    result = tag_object.replace("|", "")
    result = sc.Autocorrection(result)

    list_p = []  # value read to keep on database
    list_2d = rule.rule_strat(result)
    for i in range(len(list_2d)):
         for j in range(len(list_2d[i])):
            list_p.append(list_2d[i][j].__dict__)

    print(list_p)

    client = MongoClient('localhost', 27017)
    db = client.get_database("datanews")
    news = db.news
    news.insert_many(list_p)
