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
    # tag_location = tag_location.replace('<จังหวัด_ผิด>จังหวัด','<จังหวัด_ผิด>')
    # tag_location = tag_location.replace('<ตำบล_ผิด>ต.','<ตำบล_ผิด>')
    # print(tag_location)
    """
    word token and tag action and location
    """
    word_tokenize = wt.word_segment_identify_tag(tag_location)
    word_tokenize = wt.remove_stopword(word_tokenize)
    # print(word_tokenize)
    tag_action = tag.tag_action(word_tokenize)
    # print(tag_action)
    # tag_object = tag.tag_secondary_action_1(tag_action)
    result = tag_action.replace("|", "")
    # print('----------------B--------------------')
    print(result)
    """
    edit wrong word from <fail>
    """
    result = sc.Autocorrection(result)
    print('----------------A--------------------')
    print(result)
    # result = '<สถานที่>สภ.ปากชม </สถานที่>ส่วนร่าง<คน>ผู้เสียชีวิต</คน>นำไปชันสูตรพลิกศพที่<โรงพยาบาล>รพ.ปากชม</โรงพยาบาล>'
    # print(" ")
    # print("this true result " + result)
    # wr.export_text(result,n)

    """
    function test rule discover crime 
    """
    obj_r = rule.results_from_rules(result, n)
    # print('=========================== result ===========================')
    obj_r.Title = title
    obj_r.Content = news
    obj_r.DateTime = date_time
    obj_r.Link = file_name
    
    # da = date_time[0]
    # print(type(da))
    # d = datetime.datetime.strptime(str(da), "%Y-%m-%d")
    # dd = datetime.datetime(2009, 11, 12)
    # obj_r.Date = dd
    # print(type(dd))
    # print(obj_r.__dict__)

    # rule_st.cause_rule_results(result,n)
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
    # db = client.get_database("mydatabase")
    # news = db.mynews
    # news.insert_many(obj_r.__dict__)

    dbs = 'mongodb+srv://wathiwut193:Cc2191996@cluster0-pjudc.mongodb.net/test?retryWrites=true'
    client = MongoClient(dbs,27017)
    db = client.get_database("news")
    news = db.datanews
    # print(y)
    print(news.insert_one(obj_r.__dict__))

    end = time.time()
    print(end-start)
    # pip install dnspython
