import requests
from bs4 import BeautifulSoup
import deepcut
import regex


# -*- coding: utf-8 -*-

def run(text):
    text = get_news(text)
    # text = word_segment(text)
    return text


def get_news(text):
    web_token = requests.get(text)
    html_parser = BeautifulSoup(web_token.text, 'html.parser')

    paragraphs = html_parser.find_all("p")
    content = []
    #print(paragraphs)
    for p in paragraphs:
        s1 = str(p).replace("</p>", "<p>")
        s2 = s1.replace("<br>", "<p>")
        s3 = s2.replace("<br/>", "<p>")
        s4 = s3.split("<p>")
        for sub in s4:
           if len(sub) > 0:
            if sub != ' ':
                content.append(sub)
                text = "\n".join(content)

    return text


def word_segment(text):
    text = deepcut.tokenize(text, custom_dict="custom_dict/custom_dict.txt")
    text = "|".join(text)
    return text


def word_segment_identify_tag(text):
    pattern = r"(<[^<]วันที่>[^<]*</[^<]วันที่>)"
    matches = regex.finditer(pattern, text, regex.MULTILINE)
    match_i = []
    for matchNum, match in enumerate(matches, start=1):
        match_i.append(match.start())  # เก็บตำแหน่ง tag ตัวแรกที่เจอ
        match_i.append(match.end())  # เก็บตำแหน่ง tag ตัวสุดท้ายที่เจอ

    # print(match_i) #ดูข้อมูลเริ่มต้น สุดท้ายของ tag
    str_s = ''  # สร้างตัวแปรมาเก็บ string ที่ไม่มี tag
    index_match = 0  # สร้างตัวแปรเพื่อเช็ค index match_i
    str_tag = ''  # สร้างตัวแปรมาเก็บ string ที่มี tag
    print(len(match_i))  # check index tag
    for i in range(len(text)):
        if index_match <= len(match_i):
            if index_match % 2 == 0:  # if index_match % 2 = 0
                if index_match < len(match_i):  # if index_match < length for match_i
                    if match_i[index_match] == i:  # if match_i[index_match] = i
                        index_match = index_match + 1  # ให้ทำการเพิ่มค่า index_match
                        str_tag += text[i]  # ใส่ข้อมูลแรกของ tag ลงไปใน str_tag
                        str_s += ' ='  # ใส่ช่องว่างให้ตัวสุดท้ายก่อนที่จะเจอ tag
                    else:
                        str_s += text[i]  # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_s
                else:
                    str_s += text[i]  # เก็บ str แถวสุดท้ายหลังจาก tag
            elif index_match % 2 != 0:
                if match_i[index_match] == i:  # if match_i[index_match] = i
                    index_match += index_match  # ให้ทำการเพิ่มค่า index_match
                    str_tag += '\n'  # ใส่ช่องว่างให้ตัวสุดท้ายให้หลัง tag
                else:
                    str_tag += text[i]  # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_tag

    tag_split = (str_tag.split('\n'))

    word_cut = deepcut.tokenize(str_s, custom_dict='dictionary/custom_dict/custom_dict.txt')

    ind = 0
    # word_cut = [w.replace('=',tag_split[ind]) for w in word_cut]

    for i in range(len(word_cut)):
        if word_cut[i] == '=':
            word_cut[i] = tag_split[ind]
            ind += ind

    word = ''

    for i in range(len(word_cut)):
        if word_cut[i] != '=':
            word = ('|'.join(word_cut))

    return word
