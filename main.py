# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""


import tag_object as tag
import word_tokenize as wt
import spell_checking as sc

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    #while (True):
        URL = input("Enter URL:")
        news = wt.get_news(URL)
        tag_date = tag.tag_date(news)
        tag_time = tag.tag_time(tag_date)
        tag_person = tag.tag_person(tag_time)

        word_tokenize = wt.word_segment_identify_tag(tag_person)
        tag_object = tag.tag_start(word_tokenize)

        result = tag_object.replace("|","")
        result = sc.spell_checker(result)

        print(result)
