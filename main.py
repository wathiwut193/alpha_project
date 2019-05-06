# -*- coding: utf-8 -*-

import tag_object as tag
import word_tokenize as wt
import spell_checking as sc
import rule
import class_object as obj
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    # while (True):

    """
    read file html 
    """
    file_name = input("file_name: ")
    news = wt.read_file_get_news(file_name)
    """
    before load data to function word tokenize we use tag date and time because we found problem with word tokenize.
    they split date and time  which we don't want it to be like that.
    """
    tag_date = tag.tag_date(news)
    tag_time = tag.tag_time(tag_date)
    tag_person = tag.tag_person(tag_time)
    tag_location = tag.tag_location(tag_person)

    """
    word token and tag action and location
    """
    word_tokenize = wt.word_segment_identify_tag(tag_location)
    tag_action = tag.tag_action(word_tokenize)
    #tag_object = tag.tag_secondary_action_1(tag_action)
    result = tag_action.replace("|", "")
    """
    edit wrong word from <fail>
    """
    result = sc.Autocorrection(result)
    print(" ")
    print("this true result " + result)

    """
    function test rule discover crime 
    """
    # rule_result = rule.cause_rule_results(result)
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
