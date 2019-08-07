import tag_object as tag
import word_tokenize as wt
import spell_checking as sc
import rule
# import rule_skiptag as rule_st
import class_object as obj
import write_file as wr
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import json
import datetime
import time

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    # while (True):

    """
    read file html 
    """
    start = time.time()
    file_name = input("file_name: ")
    if (file_name[-7] == '1' or file_name[-7] == '2' or file_name[-7] == '3' or file_name[-7] == '4'
            or file_name[-7] == '5' or file_name[-7] == '6' or file_name[-7] == '7' or file_name[-7] == '8'
            or file_name[-7] == '9'):
        n = file_name[-7] + file_name[-6]
    else:
        n = file_name[-6]
    news = wt.read_file_get_news(file_name)
    # get topic
    title = wt.get_topic_from_news(file_name)
    # print(title)
    # get date time
    date_time = wt.get_datetime_from_news(file_name)

    """
    before load data to function word tokenize we use tag date and time because we found problem with word tokenize.
    they split date and time  which we don't want it to be like that.
    """
    tag_date = tag.tag_date(news)
    tag_time = tag.tag_time(tag_date)
    tag_person = tag.tag_person(tag_time)
    tag_adverb = tag.tag_adverb(tag_person)
    tag_location = tag.tag_location(tag_adverb)
    """
    word token and tag action and location
    """
    word_tokenize = wt.word_segment_identify_tag(tag_location)
    rm_stopword = wt.remove_stopword(word_tokenize)
    print(rm_stopword)
    # tag_action = tag.tag_action(word_tokenize)
    # #print(tag_action)
    # tag_object = tag.tag_secondary_action(tag_action,1)
    # result = tag_action.replace("|", "")
    #print('----------------B--------------------')
    #print(result)
    """
    edit wrong word from <fail>
    """
    # result = sc.Autocorrection(result)
    # print('----------------A--------------------')
    # print(result)
    """
    function test rule discover crime 
    """
    # obj_r = rule.results_from_rules(result, n)
    # # print('=========================== result ===========================')
    # obj_r.Title = title
    # obj_r.Content = news
    # obj_r.DateTime = date_time
    # obj_r.Link = file_name

    """
    insert data to database 
    """
    # dbs = ''
    # client = MongoClient('localhost',27017)
    # db = client.get_database("news")
    # news = db.datanews
    # # print(y)
    # print(news.insert_one(obj_r.__dict__))
    #
    # end = time.time()
    # print(end-start)
    # pip install dnspython
