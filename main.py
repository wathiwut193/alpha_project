import tag_object as tag
import word_tokenize as wt
import spell_checking as sc
import rule
# import rule_skiptag as rule_st
import class_object as obj
import write_file as wr
# import pymongo
# from pymongo import MongoClient
from bs4 import BeautifulSoup

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    # while (True):

    """
    read file html 
    """
    file_name = input("file_name: ")
    if (file_name[-7] == '1' or file_name[-7] == '2' or file_name[-7] == '3' or file_name[-7] == '4'
            or file_name[-7] == '5' or file_name[-7] == '6' or file_name[-7] == '7' or file_name[-7] == '8'
            or file_name[-7] == '9'):
        n = file_name[-7] + file_name[-6]
    else:
        n = file_name[-6]
    news = wt.read_file_get_news(file_name)
    # news = ('\n'
    # '\n'
    # '1. 1 ยิง นายทีน นายพล ที่โรงเรียน ยิง ฆาตกรรม 09.00น. ยิง \n'
    # '2. 1/2 ผู้เสียหาย ที่โรงเรียน ฆ่าตัวตาย นายพล ที่โรงเรียน ฆ่าตัวตาย \n'
    # '3. 2 นายพล ที่โรงเรียน ยิง ยิง นายแชมป์ นายสุชาย ที่โรงเรียน \n'
    # '4. 3 นายสุชาติ ที่โรงเรียน ถูก ที่โรงเรียน ยิง นายฟุก \n'
    # '5. 3/2 นายสุชาติ ที่โรงเรียน ถูก ที่โรงเรียน ยิง \n'
    # '6. 4 นายสุชาติ ที่โรงเรียน ถูก ที่โรงเรียน นายฟุก ที่โรงเรียน ยิง')
    """
    before load data to function word tokenize we use tag date and time because we found problem with word tokenize.
    they split date and time  which we don't want it to be like that.
    """
    tag_date = tag.tag_date(news)
    tag_time = tag.tag_time(tag_date)
    tag_person = tag.tag_person(tag_time)
    tag_adverb = tag.tag_adverb(tag_person)
    tag_location = tag.tag_location(tag_adverb)
    # print(tag_location)
    """
    word token and tag action and location
    """
    word_tokenize = wt.word_segment_identify_tag(tag_location)
    word_tokenize = wt.remove_stopword(word_tokenize)
    print(word_tokenize)
    tag_action = tag.tag_action(word_tokenize)
    # print(tag_action)
    # tag_object = tag.tag_secondary_action_1(tag_action)
    result = tag_action.replace("|", "")
    print(result)
    """
    edit wrong word from <fail>
    """
    result = sc.Autocorrection(result)
    # result = '<สถานที่>สภ.ปากชม </สถานที่>ส่วนร่าง<คน>ผู้เสียชีวิต</คน>นำไปชันสูตรพลิกศพที่<โรงพยาบาล>รพ.ปากชม</โรงพยาบาล>'
    # print(" ")
    # print("this true result " + result)
    # wr.export_text(result,n)

    """
    function test rule discover crime 
    """
    rule.results_from_rules(result, n)

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
    # db = client.get_database("datanews")
    # news = db.news
    # news.insert_many(list_p)
