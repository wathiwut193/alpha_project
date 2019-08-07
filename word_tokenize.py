import requests
from bs4 import BeautifulSoup
import deepcut
import regex
import datetime


# -*- coding: utf-8 -*-

def run(text):
    """
    run all method in file
    :param text:
    :return: text with tag
    """
    text = get_text_news(text)
    text = get_html(text)
    # text = word_segment(text)
    return text


def get_text_news(text):
    """
    scraping content news from web thairath
    :param text:
    :return: text
    """
    paragraphs = text.find_all("p")
    content = []
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


def get_html(url):
    web_token = requests.get(url)
    html_parser = BeautifulSoup(web_token.text, 'html.parser')
    print(html_parser)
    return html_parser


def word_segment(text):
    """
    word segmentation
    :param text:
    :return: text
    """
    text = deepcut.tokenize(text, custom_dict="custom_dict/custom_dict.txt")
    text = "|".join(text)
    return text


def word_segment_identify_tag(text):
    """
    function skip tag this function when they found <tag> function will skip <tag>
    :param text:
    :return:
    """
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
    for i in range(len(word_cut)):
        if word_cut[i] == '=':
            word_cut[i] = tag_split[ind]
            ind += ind

    word = ''

    for i in range(len(word_cut)):
        if word_cut[i] != '=':
            word = ('|'.join(word_cut))

    return word


def read_file_get_news(file_name):
    with open("raw_data/input_html/" + str(file_name), 'r', encoding='utf-8') as rf:
        read_html = rf.read()
        soup = BeautifulSoup(read_html, "lxml")
        soup.prettify()
        paragraphs = soup.find_all("p")
        paragraphs_h1 = soup.find_all("h1")
        content = []
        for h1 in paragraphs_h1:
            s1 = str(h1).replace("</h1>", "<h1>")
            s2 = s1.split("<h1>")
            for sub in s2:
                if sub != '':
                    content.append(sub)
                    text = "".join(content)
        for p in paragraphs:
            s1 = str(p).replace("</p>", "<p>")
            s2 = s1.replace("<br>", "<p>")
            s3 = s2.replace("<br/>", "<p>")
            s4 = s3.split("<p>")
            for sub in s4:
                if len(sub) > 0:
                    if sub != ' ':
                        content.append(sub)
                        text = "\n\n".join(content)
    rf.close()
    return text


def get_topic_from_news(file_name):
    with open("raw_data/input_html/" + str(file_name), 'r', encoding='utf-8') as rf:
        read_html = rf.read()
        soup = BeautifulSoup(read_html, "lxml")
        soup.prettify()
        paragraphs_h1 = soup.find_all("h1")
        content = []
        for h1 in paragraphs_h1:
            s1 = str(h1).replace("</h1>", "<h1>")
            s2 = s1.split("<h1>")
            for sub in s2:
                if sub != '':
                    content.append(sub)
                    text = "".join(content)
    rf.close()
    return text


def get_datetime_from_news(file_name):
    with open("raw_data/input_html/" + str(file_name), 'r', encoding='utf-8') as rf:
        read_html = rf.read()
        soup = BeautifulSoup(read_html, "lxml")
        soup.prettify()
        paragraphs = soup.find_all("span")
        # print(paragraphs)
        regex_date = (
            r"(([1-9]|[0-2][\d]|[3][0-1])\s?(/)?(ม\.ค\.|มกราคม|มกรา|ก\.พ\.|กุมภาพันธ์|กุมภา|มี\.ค\.|มีนาคม|มีนา|เม\.ย\.|"
            "เมษายน|เมษา|พ\.ค\.|พฤษภาคม|พฤษภา|มิ\.ย\.|มิถุนายน|มิถุนา|ก\.ค\.|กรกฎาคม|กรกฎา|ส\.ค\.|สิงหาคม|สิงหา|ก\.ย\.|"
            "กันยายน|กันยา|ต\.ค\.|ตุลาคม|ตุลา|พ\.ย\.|พฤศจิกายน|พฤศจิกา|ธ\.ค\.|ธันวาคม|ธันวาคม)\s?(/)?(พ.ศ.|ค.ศ.|พศ|คศ)?\s?"
            "(\d\d\d\d|\d\d)?|([1-9]|[0-2][\d]|[3][0-1])\s?(/|-|\.)\s?([0][\d]|[1][0-2])\s?(/|-|\.)\s?(\d\d\d\d|\d\d))")

        regex_time = r"(([0-1][\d]|[2][0-4])\s?(:|.)\s?([0-5][\d])\s?(นาฬิกา|น\.|น))"

        date = ''
        time = ''
        for p in paragraphs:
            s1 = str(p)
            match_date = regex.search(regex_date, s1)
            if match_date != None:
                # print(m.group(1))
                date = match_date.group(1)
            match_time = regex.search(regex_time, s1)
            if match_time != None:
                time = match_time.group(1)

        date = date.replace(' ', '')
        date = (date.replace('ม.ค.', '-01-').replace('ก.พ.', '-02-').replace('มี.ค.', '-03-')
                .replace('เม.ย.', '-04-').replace('พ.ค.', '-05-').replace('มิ.ย.', '-06-').replace('ก.ค.', '-07-')
                .replace('ส.ค.', '-08-').replace('ก.ย.', '-09-').replace('ต.ค.', '-10-').replace('พ.ย.', '-11-')
                .replace('ธ.ค.', '-12-'))
        time = time.replace('น.', '').replace('น', '').replace('นาฬิกา', '').replace(' ', '')
        # print(time)
        # print(date)
        date_time_str = date + ' ' + time
        # print(date_time_str)
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M')
        # date_time_obj = datetime.datetime.strptime(date, '%d-%m-%Y')

        # print(date_time_obj.date())
        # date_time_obj = datetime.datetime.strptime(time, '%H:%M')
        # print(date_time_obj.time())
        # date_time = []
        # date_time.append(date_time_obj.date())
        # date_time.append(date_time_obj.time())
        # print(date_time_obj)

    rf.close()
    return date_time_obj


def remove_stopword(text):
    """
    remove stopword
    :return:
    """
    words = {'จะ', 'เเล้ว', 'ได้', 'อัน', 'ว่า', 'ที่', 'จึง', 'จาก', 'เป็น', 'ไป', 'หรือ',
             'นั้น', 'อาจ', 'ซึ่ง', 'ก็', 'มา', 'กับ', 'ไว้', 'ทั้งๆที่', 'น่า', 'ก่อน', 'ทำ',
             'โดย', 'นีั','ไร', 'ของ', 'ขอ', 'ว่า', 'เเค่', 'กัน', 'ก็', 'เพื่อ',
             'ละ', 'คือ', 'เเละ', 'ด้วย', 'จาก', 'จึง', 'ใน', 'ๆ', 'ของ', 'ครั้ง', 'เมื่อ',
             'ต่อ', 'นี้', '!', 'ทั้ง', 'มักจะ', 'ของ', 'เนื่องจาก', 'กับ', 'ดังนี้', 'เข้า'}

    stop_words = set(words)
    word_tokens = deepcut.tokenize(text, custom_dict="custom_dict.txt")
    filter_sence = [w for w in word_tokens if not w in stop_words]
    filter_sence = []

    for w in word_tokens:
        if w not in stop_words:
            filter_sence.append(w)

    word = ''.join(filter_sence)
    return word
