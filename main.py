# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""


import tag_object as tag
import word_tokenize as wt

# - *- coding: utf- 8 - *-
if __name__ == '__main__':
    while (True):
        URL = input("Enter URL:")
        news = wt.get_news(URL)
        tag_object = tag.tag_start(news)
        print(tag_object)
