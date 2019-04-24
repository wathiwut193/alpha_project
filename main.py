# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:15:00 2019

@author: wathi
"""

import requests
from bs4 import BeautifulSoup
import deepcut
import time
from pymongo import MongoClient
import os
import glop
import re
import tag_object as tag


# - *- coding: utf- 8 - *-

# function get news from website thairath only
def get_news(URL):
    data = requests.get(URL)
    soup = BeautifulSoup(data.text, 'html.parser')
    # header = soup.find_all("h1")
    # date_news = soup.find_all("div", {"class": "css-1cxbv8p evs3ejl7"})
    paragraphs = soup.find_all("p")

    # text = ''
    # # for i in header:
    # #   text += i.text
    # # for z in date_news:
    # #    text += z.text
    # for j in paragraphs:
    #     text += j.get_text()

    content = []
    for p in paragraphs:
        content.append(p.getText())
        all_content = "\n".join(content)
    return all_content


def word_tokenize(text):
    text = deepcut.tokenize(text, custom_dict="custom_dict/custom_dict.txt")
    word_cut = "|".join(text)

    regex = r"(<[^<]เวลา>[^<]*</[^<]เวลา>)"
    read_str = ("คดีฆ่าพระ ยังอึมครึม วอนช่วยแก้ปัญหาดับไฟใต้!\n"
                "โดย ไทยรัฐฉบับพิมพ์<date>24 ม.ค. 2562</date> <time>04:30 น.</time>\n"
                "สมภารวัดดัง จ.นราธิวาส ระบุสถานการณ์ในพื้นที่ยังอึมครึม ออกจากวัดไปกิจนิมนต์แต่ละครั้งไม่รู้จะมีชีวิตกลับมาหรือไม่ ผวาหนักถึงขั้นลูกศิษย์ต้องพกปืนป้องกันตัว ค้านแนวคิด ผบ.ทบ.ที่จะให้ทหารบวชพระ ชี้หัวดื้อไม่ยอมปฏิบัติศาสนกิจ ขณะที่พระสงฆ์ใน อ.สุไหงปาดี ออกบิณฑบาตวันแรกหลังเกิดเหตุยิงถล่มวัดทำพระมรณภาพ 2 รูป ท่ามกลางการรักษาความปลอดภัยเข้มงวด ด้านชาวพุทธ 3 จังหวัดชายแดนใต้กว่า 600 คน ตั้งขบวนแห่เรียกร้องสันติ\n")
    matches = re.finditer(regex, read_str, re.MULTILINE)
    match_i = []
    for matchNum, match in enumerate(matches, start=1):
        match_i.append(match.start())  # เก็บตำแหน่ง tag ตัวแรกที่เจอ
        match_i.append(match.end())  # เก็บตำแหน่ง tag ตัวสุดท้ายที่เจอ

        str_s = ''  # สร้างตัวแปรมาเก็บ string ที่ไม่มี tag
        index_match = 0  # สร้างตัวแปรเพื่อเช็ค index match_i
        str_tag = ''  # สร้างตัวแปรมาเก็บ string ที่มี tag
    for i in range(len(read_str)):
        if index_match <= len(match_i):
            if index_match % 2 == 0:  # if index_match % 2 เท่ากับ 0
                if index_match < len(match_i):  # if index_match < length for match_i
                    if match_i[index_match] == i:  # if match_i[index_match] = i
                        index_match = index_match + 1  # ให้ทำการเพิ่มค่า index_match
                        str_tag += read_str[i]  # ใส่ข้อมูลแรกของ tag ลงไปใน str_tag
                        str_s += ' ='  # ใส่ช่องว่างให้ตัวสุดท้ายก่อนที่จะเจอ tag
                    else:
                        str_s += read_str[i]  # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_s
                else:
                    str_s += read_str[i]  # เก็บ str แถวสุดท้ายหลังจาก tag
            elif index_match % 2 != 0:  # if index_match % 2 ไม่เท่ากับ 0
                if match_i[index_match] == i:  # if match_i[index_match] = i
                    index_match = index_match + 1  # ให้ทำการเพิ่มค่า index_match
                    str_tag += '\n'  # ใส่ช่องว่างให้ตัวสุดท้ายให้หลัง tag
                else:
                    str_tag += read_str[i]  # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_tag

    tag_split = (str_tag.split('\n'))
    word_cut = deepcut.tokenize(str_s, custom_dict='corpus/compond_word.txt')
    ind = 0
    for i in range(len(word_cut)):
        if word_cut[i] == '=':
            word_cut[i] = tag_split[ind]
            ind = ind + 1

    word = ''
    for i in range(len(word_cut)):
        if word_cut[i] != '=':
            word = ('|'.join(word_cut))

    return word


if __name__ == '__main__':
    URL = input("Enter URL:")
    news = get_news(URL)
    news = word_tokenize(news)

    news_none_cut = get_news(URL)
    print(tag.tag_start(news_none_cut))
    print(tag.tag_start(news))
