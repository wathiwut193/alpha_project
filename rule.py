import ngram
import numpy as np
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint
import class_object as obj
import tag_object as tag
import write_file as wr
import rule_nonskiptag as rnt
import rule_skiptag as rst


def split_column(str_text):
    list_text = str_text.split('\n')
    str_text = '&'.join(list_text)
    str_text = str_text.replace('>', '> ')
    str_text = str_text.replace('<', ' <')
    list_text = str_text.split('&')
    list_text2d = []

    for i in range(len(list_text)):
        list_text2d.append(list_text[i].split(' '))

    # delete list empty
    index_delete = []
    for i in range(len(list_text2d)):
        index_delete.append([])
        for j in range(len(list_text2d[i])):
            if (list_text2d[i][j] == 'Share:' or list_text2d[i][j] == '') and j == 0:
                index_delete[i].append(j)

    di = 0
    dj = 0
    for i in range(len(list_text2d)):
        for j in range(len(list_text2d[i])):
            if i == di:
                if len(index_delete[di]) > 0:
                    if j == index_delete[di][dj]:
                        list_text2d[di].pop(dj)
                        di += 1
                else:
                    di += 1

    list2_text_new = [x for x in list_text2d if x != []]

    return list2_text_new


def tag_to_obj(list_tag_text):
    list_tag_person = ['<คน>']
    # person 2 ex นาย... หรือ ... ตามด้วยนามสกุล
    list_tag_person2 = ['<คน2>']
    list_tag_action = ['<กระทำ1>', '<กระทำรอง1>', '<กระทำ2>', '<กระทำ3>', '<กระทำ4>', '<กระทำ5>', '<กระทำ6>',
                       '<กระทำ7>', '<กระทำ8>']
    list_tag_adverb = ['<คำบ่งบอก>', '<คำบ่งบอก2>', '<คำบ่งบอก3>', '<คำบ่งบอก4>']
    list_tag_location = ['<ประเทศ>', '<จังหวัด>', '<อำเภอ>', '<เขต>', '<ตำบล>', '<แขวง>', '<ถนน>', '<แม่น้ำ>',
                         '<สถานที่>'
        , '<ห้าง>', '<โรงพยาบาล>', '<มหาวิทยาลัย>']
    list_tag_country = ['<ประเทศ>']
    list_tag_province = ['<จังหวัด>']
    list_tag_amphoe = ['<อำเภอ>']
    list_tag_area = ['<เขต>']
    list_tag_tambon = ['<ตำบล>']
    list_tag_district = ['<แขวง>']
    list_tag_road = ['<ถนน>']
    list_tag_river = ['<แม่น้ำ>']
    list_tag_place = ['<สถานที่>']
    list_tag_mall = ['<ห้าง>']
    list_tag_hospital = ['<โรงพยาบาล>']
    list_tag_university = ['<มหาวิทยาลัย>']
    # date and time
    list_tag_time = ['<เวลา>']
    list_tag_date = ['<วัน>']

    person_tag = ngram.NGram(list_tag_person)
    person_tag2 = ngram.NGram(list_tag_person2)
    action_tag = ngram.NGram(list_tag_action)
    adverb_tag = ngram.NGram(list_tag_adverb)
    location_tag = ngram.NGram(list_tag_location)
    country_tag = ngram.NGram(list_tag_country)
    province_tag = ngram.NGram(list_tag_province)
    amphoe_tag = ngram.NGram(list_tag_amphoe)
    area_tag = ngram.NGram(list_tag_area)
    tambon_tag = ngram.NGram(list_tag_tambon)
    district_tag = ngram.NGram(list_tag_district)
    road_tag = ngram.NGram(list_tag_road)
    river_tag = ngram.NGram(list_tag_river)
    place_tag = ngram.NGram(list_tag_place)
    mall_tag = ngram.NGram(list_tag_mall)
    hospital_tag = ngram.NGram(list_tag_hospital)
    university_tag = ngram.NGram(list_tag_university)
    time_tag = ngram.NGram(list_tag_time)
    date_tag = ngram.NGram(list_tag_date)

    list_tag_2d = []
    check_l = False
    stop = False

    for i in range(len(list_tag_text)):
        list_tag_2d.append([])
        index_location = []
        for j in range(len(list_tag_text[i])):
            check_location = False

            if person_tag.search(list_tag_text[i][j], threshold=1.0):
                if j + 2 <= len(list_tag_text[i]) - 1:
                    if list_tag_text[i][j + 2] != '</คน>':
                        p = obj.Person(list_tag_text[i][j + 1], list_tag_text[i][j + 2])
                    else:
                        p = obj.Person(list_tag_text[i][j + 1])

                    list_tag_2d[i].append(p)
            # person 2
            elif person_tag2.search(list_tag_text[i][j], threshold=1.0):
                check_person = False
                check_p = j
                while (check_person != True):
                    if list_tag_text[i][check_p] == '</คน2>':
                        check_p += 0
                        check_person = True
                    else:
                        check_p += 1
                p = obj.Person(list_tag_text[i][j + 1], list_tag_text[i][check_p - 1])
                list_tag_2d[i].append(p)
            # end
            elif action_tag.search(list_tag_text[i][j], threshold=1.0):
                a = obj.Action(list_tag_text[i][j + 1], list_tag_text[i][j][1:len(list_tag_text[i][j]) - 1])
                list_tag_2d[i].append(a)

            elif adverb_tag.search(list_tag_text[i][j], threshold=1.0):
                if (list_tag_text[i][j][len(list_tag_text[i][j]) - 2] == '2' or
                        list_tag_text[i][j][len(list_tag_text[i][j]) - 2] == '3' or
                        list_tag_text[i][j][len(list_tag_text[i][j]) - 2] == '4'
                ):
                    v = obj.Verb(list_tag_text[i][j + 1], list_tag_text[i][j][len(list_tag_text[i][j]) - 2])
                else:
                    v = obj.Verb(list_tag_text[i][j + 1])
                list_tag_2d[i].append(v)
            # bug วัน เดือน ปี ไม่ครบ
            elif date_tag.search(list_tag_text[i][j], threshold=1.0):
                d = obj.Date(list_tag_text[i][j + 1])
                list_tag_2d[i].append(d)

            elif time_tag.search(list_tag_text[i][j], threshold=1.0):
                t = obj.Time(list_tag_text[i][j + 1])
                list_tag_2d[i].append(t)

            # fix bug location > 2 location in paragrah
            elif location_tag.search(list_tag_text[i][j], threshold=1.0):

                if (j not in index_location and stop == False):
                    country = ''
                    province = ''
                    amphoe = ''
                    area = ''
                    tambon = ''
                    district = ''
                    road = ''
                    river = ''
                    place = ''
                    mall = ''
                    hospital = ''
                    university = ''

                    count_r = j
                    check_r = False
                    # print(list_tag_text[i][j+1],stop)

                    while (check_r != True):
                        if country_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            country = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif province_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            province = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif amphoe_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            amphoe = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif area_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            area = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif tambon_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            tambon = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif district_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            district = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif road_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            road = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif river_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            river = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif place_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            place = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif mall_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            mall = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif hospital_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            hospital = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #
                        elif university_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            university = list_tag_text[i][count_r + 1]
                            check_location = True
                            index_location.append(count_r)  #

                        # new
                        elif person_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break
                        elif person_tag2.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break
                        elif action_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break
                        elif adverb_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break
                        elif date_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break
                        elif time_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            stop = True
                            break

                        # if check_location == True:
                        # print(province)
                        # l = obj.Location(country,province,amphoe,area,tambon,district,road,river,place,mall,hospital,university)
                        # list_tag_2d[i].append(l)

                        if count_r == len(list_tag_text[i]) - 1:
                            if check_location == True:
                                l = obj.Location(country, province, amphoe, area, tambon, district, road, river, place,
                                                 mall, hospital, university)
                                list_tag_2d[i].append(l)
                            check_r = True
                        else:
                            count_r += 1

                    # if check_location == True and check_r == True:
                    if stop == True:
                        l = obj.Location(country, province, amphoe, area, tambon, district, road, river, place, mall,
                                         hospital, university)
                        list_tag_2d[i].append(l)
                        stop = False
                else:
                    index_location.append(j)

                # print(index_location)

    return list_tag_2d


def print_in_obj(result_rule):
    print('-----------obj in paragraph-----------')
    for i in range(len(result_rule)):
        if i == 0:
            print('----------------- Topic -----------------')
            index = ' '
        elif i == 1:
            print('----------------- Secondary Topic -----------------')
            index = ' '
        else:
            print('----------------- Paragraph', i - 1, '-----------------')
            index = i - 1
        for j in range(len(result_rule[i])):
            if str(result_rule[i][j]) == 'คน':
                print(index, j, result_rule[i][j].status, ':', result_rule[i][j].firstname, result_rule[i][j].lastname)
            elif (str(result_rule[i][j]) == 'กระทำ1' or str(result_rule[i][j]) == 'กระทำ2'
                  or str(result_rule[i][j]) == 'กระทำ3' or str(result_rule[i][j]) == 'กระทำ4'
                  or str(result_rule[i][j]) == 'กระทำ5' or str(result_rule[i][j]) == 'กระทำ6'
                  or str(result_rule[i][j]) == 'กระทำ7' or str(result_rule[i][j]) == 'กระทำ8'
                  or str(result_rule[i][j]) == 'กระทำรอง1'):
                print(index, j, str(result_rule[i][j]), ':', result_rule[i][j].name_action)

            elif (str(result_rule[i][j]) == 'คำบ่งบอก' or str(result_rule[i][j]) == 'คำบ่งบอก2'
                  or str(result_rule[i][j]) == 'คำบ่งบอก3' or str(result_rule[i][j]) == 'คำบ่งบอก4'):
                print(index, j, str(result_rule[i][j]), ':', result_rule[i][j].name_verb)

            elif str(result_rule[i][j]) == 'สถานที่':
                print(index, j, str(result_rule[i][j]), ':', result_rule[i][j].split_location)

            elif str(result_rule[i][j]) == 'วัน':
                print(index, j, str(result_rule[i][j]), ':', result_rule[i][j].date)

            elif str(result_rule[i][j]) == 'เวลา':
                print(index, j, str(result_rule[i][j]), ':', result_rule[i][j].time)


def print_rule_result(result_rule, n):
    # print(result_rule)
    if n <= 12:
        print('_______________ Person Rule', n, '_______________')
    else:
        print('--------------- L R', n, '-------------------')

    if result_rule == 'Empty':
        print('Empty')
    else:
        for i in range(len(result_rule)):
            if i == 0:
                p = 'Topic'
                index = ' '
            elif i == 1:
                p = 'Secondary Topic'
                index = ' '
            else:
                p = 'Paragraph'
                index = i - 1
            for j in range(len(result_rule[i])):
                print('-----------------', p, index, '-----------------')
                for k in range(len(result_rule[i][j])):
                    if str(result_rule[i][j][k]) == 'คน':
                        print(result_rule[i][j][k].status, ':', result_rule[i][j][k].firstname,
                              result_rule[i][j][k].lastname)
                        # print('P',i+1,'|',result_rule[i][j][k].status ,':', result_rule[i][j][k].firstname , result_rule[i][j][k].lastname)
                    elif (str(result_rule[i][j][k]) == 'กระทำ1' or str(result_rule[i][j][k]) == 'กระทำ2'
                          or str(result_rule[i][j][k]) == 'กระทำ3' or str(result_rule[i][j][k]) == 'กระทำ4'
                          or str(result_rule[i][j][k]) == 'กระทำ5' or str(result_rule[i][j][k]) == 'กระทำ6'
                          or str(result_rule[i][j][k]) == 'กระทำ7' or str(result_rule[i][j][k]) == 'กระทำ8'
                          or str(result_rule[i][j][k]) == 'กระทำรอง1'):
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].name_action)
                        # print('P',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].name_action)
                    elif (str(result_rule[i][j][k]) == 'คำบ่งบอก' or str(result_rule[i][j][k]) == 'คำบ่งบอก2'
                          or str(result_rule[i][j][k]) == 'คำบ่งบอก3' or str(result_rule[i][j][k]) == 'คำบ่งบอก4'):
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].name_verb)
                        # print('P',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].name_verb)
                    elif str(result_rule[i][j][k]) == 'สถานที่':
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].split_location)
                        # print('L',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].split_location)
                    elif str(result_rule[i][j][k]) == 'วัน':
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].date)
                        # print('T',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].date)
                    elif str(result_rule[i][j][k]) == 'เวลา':
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].time)
                        # print('D',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].time)


def count_result(result_rule):
    if result_rule == 'Empty':
        # print('Empty')
        result = 0
    else:
        result = 0
        for i in range(len(result_rule)):
            check_len = False
            for j in range(len(result_rule[i])):
                if len(result_rule[i]) >= 2 and check_len == False:
                    check_len = True
                    result += len(result_rule[i])
                elif len(result_rule[i]) == 1:
                    result += len(result_rule[i])
    return result


def results_from_rules(str_text, n):
    """
    """
    list_text2d = split_column(str_text)
    list_tag_2d = tag_to_obj(list_text2d)
    print_in_obj(list_tag_2d)
    list_tag_1 = tag_to_obj(list_text2d)
    list_tag_2 = tag_to_obj(list_text2d)
    list_tag_3 = tag_to_obj(list_text2d)
    list_tag_4 = tag_to_obj(list_text2d)
    list_tag_5 = tag_to_obj(list_text2d)
    list_tag_6 = tag_to_obj(list_text2d)
    list_tag_7 = tag_to_obj(list_text2d)
    list_tag_8 = tag_to_obj(list_text2d)
    list_tag_9 = tag_to_obj(list_text2d)
    list_tag_10 = tag_to_obj(list_text2d)
    list_tag_11 = tag_to_obj(list_text2d)
    list_tag_12 = tag_to_obj(list_text2d)
    list_tag_13 = tag_to_obj(list_text2d)
    list_tag_14 = tag_to_obj(list_text2d)
    list_tag_15 = tag_to_obj(list_text2d)
    list_tag_16 = tag_to_obj(list_text2d)
    list_tag_17 = tag_to_obj(list_text2d)
    list_tag_18 = tag_to_obj(list_text2d)

    # wr.export_obj(list_tag_2d, str(n))
    # wr.export_text(str_text, str(n))
    list_person = findperson(list_tag_2d)

    print('--------------- Rule Result NonSkipTag ---------------')
    count = 0
    # Non Skip Tag
    print('1.→  คน (ร้าย) + กระทำ (ผิด)*')
    nonskip_result1 = rnt.rule1(list_tag_1)
    print_rule_result(nonskip_result1, 1)
    count += count_result(nonskip_result1)
    print('------------------------------')
    print('Result Count NonSkipTag R1 : ', count)
    # wr.export_rule(nonskip_result1, 1, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*')
    nonskip_result2 = rnt.rule2(list_tag_2)
    print_rule_result(nonskip_result2, 2)
    count += count_result(nonskip_result2)
    print('------------------------------')
    print('Result Count NonSkipTag R2 : ', count)
    # wr.export_rule(nonskip_result2, 2, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)')
    nonskip_result3 = rnt.rule3(list_tag_3)
    print_rule_result(nonskip_result3, 3)
    count += count_result(nonskip_result3)
    print('------------------------------')
    print('Result Count NonSkipTag R3 : ', count)
    # wr.export_rule(nonskip_result3, 3, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)')
    nonskip_result4 = rnt.rule4(list_tag_4)
    print_rule_result(nonskip_result4, 4)
    count += count_result(nonskip_result4)
    print('------------------------------')
    print('Result Count NonSkipTag R4 : ', count)
    # wr.export_rule(nonskip_result4, 4, str(n), 'NonSkipTag', count)

    # when rule 1,2,3 and 4 result = Empty 
    # tag secondary action 1
    # check result by rule 8
    if nonskip_result1 == 'Empty' and nonskip_result2 == 'Empty' and nonskip_result3 == 'Empty' and nonskip_result4 == 'Empty':
        str_text = tag.tag_secondary_action(str_text,1)
        #print(str_text)
        list_text2d = split_column(str_text)
        list_tag_8 = tag_to_obj(list_text2d)
        count = 0
        print('8.→ คน (ร้าย) + กระทำ + คน (เจ้าหน้าที่)')
        nonskip_result8 = rnt.rule8(list_tag_8)
        print_rule_result(nonskip_result8, 8)
        count += count_result(nonskip_result8)
        print('------------------------------')
        print('Result Count NonSkipTag R8 : ', count)
        # wr.export_rule(nonskip_result8, 8, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('5.→ คน (เจ้าหน้าที่)* + กระทำ3* +- คน (ร้าย)')
    nonskip_result5 = rnt.rule5(list_tag_5)
    print_rule_result(nonskip_result5, 5)
    count += count_result(nonskip_result5)
    print('------------------------------')
    print('Result Count NonSkipTag R5 : ', count)
    # wr.export_rule(nonskip_result5, 5, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('6.→ คน (เจ้าหน้าที่) + กระทำ + คน (เสียหาย)* + กระทำ')
    nonskip_result6 = rnt.rule6(list_tag_6)
    print_rule_result(nonskip_result6, 6)
    count += count_result(nonskip_result6)
    print('------------------------------')
    print('Result Count NonSkipTag R6 : ', count)
    # wr.export_rule(nonskip_result6, 6, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('7.→ คน (เสียหาย)* + กระทำ + คน (เจ้าหน้าที่)')
    nonskip_result7 = rnt.rule7(list_tag_7)
    print_rule_result(nonskip_result7, 7)
    count += count_result(nonskip_result7)
    print('------------------------------')
    print('Result Count NonSkipTag R7 : ', count)
    # wr.export_rule(nonskip_result7, 7, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('9.→ คน (ร้าย) + คำ (บ่งบอกว่าถูกกระทำ) +- เจ้าหน้าที่ + กระทำ *** เหมือน3.')
    nonskip_result9 = rnt.rule9(list_tag_9)
    print_rule_result(nonskip_result9, 9)
    count += count_result(nonskip_result9)
    print('------------------------------')
    print('Result Count NonSkipTag R9 : ', count)
    # wr.export_rule(nonskip_result9, 9, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('10.→ คน (เสียหาย) + กระทำ* ')
    nonskip_result10 = rnt.rule10(list_tag_10)
    print_rule_result(nonskip_result10, 10)
    count += count_result(nonskip_result10)
    print('------------------------------')
    print('Result Count NonSkipTag R10 : ', count)
    # wr.export_rule(nonskip_result10, 10, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('11.→ คน (ร้าย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 11.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (ร้าย)')
    nonskip_result11 = rnt.rule11(list_tag_11)
    print_rule_result(nonskip_result11, 11)
    count += count_result(nonskip_result11)
    print('------------------------------')
    print('Result Count NonSkipTag R11 : ', count)
    # wr.export_rule(nonskip_result11, 11, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('12.→ คน (เสียหาย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 12.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (เสียหาย)')
    nonskip_result12 = rnt.rule12(list_tag_12)
    print_rule_result(nonskip_result12, 12)
    count += count_result(nonskip_result12)
    print('------------------------------')
    print('Result Count NonSkipTag R12 : ', count)
    # wr.export_rule(nonskip_result12, 12, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('13.→  กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)')
    nonskip_result13 = rnt.rule13(list_tag_13)
    print_rule_result(nonskip_result13, 13)
    count += count_result(nonskip_result13)
    print('------------------------------')
    print('Result Count NonSkipTag R13 : ', count)
    # wr.export_rule(nonskip_result13, 13, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('14.→ คน (ร้าย)* + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)')
    nonskip_result14 = rnt.rule14(list_tag_14)
    print_rule_result(nonskip_result14, 14)
    count += count_result(nonskip_result14)
    print('------------------------------')
    print('Result Count NonSkipTag R14 : ', count)
    # wr.export_rule(nonskip_result14, 14, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('15.→ กระทำ (ผิด) + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)')
    nonskip_result15 = rnt.rule15(list_tag_15)
    print_rule_result(nonskip_result15, 15)
    count += count_result(nonskip_result15)
    print('------------------------------')
    print('Result Count NonSkipTag R15 : ', count)
    # wr.export_rule(nonskip_result15, 15, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('16.→ กระทำ (ผิด) + คน + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)')
    nonskip_result16 = rnt.rule16(list_tag_16)
    print_rule_result(nonskip_result16, 16)
    count += count_result(nonskip_result16)
    print('------------------------------')
    print('Result Count NonSkipTag R16 : ', count)
    # wr.export_rule(nonskip_result16, 16, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('17.→ คน + คำกริยา + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) +- กระทำ (ผิด) + สถานที่ (เกิดเหตุ)')
    nonskip_result17 = rnt.rule17(list_tag_17)
    print_rule_result(nonskip_result17, 17)
    count += count_result(nonskip_result17)
    print('------------------------------')
    print('Result Count NonSkipTag R17 : ', count)
    # wr.export_rule(nonskip_result17, 17, str(n), 'NonSkipTag', count)

    print('\n')
    count = 0
    print('18.→ เวลา + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)')
    nonskip_result18 = rnt.rule18(list_tag_18)
    print_rule_result(nonskip_result18, 18)
    count += count_result(nonskip_result18)
    print('------------------------------')
    print('Result Count NonSkipTag R18 : ', count)
    # wr.export_rule(nonskip_result18, 18, str(n), 'NonSkipTag', count)
    
    # ==========================================================================================================
    print('\n--------------- Rule Result SkipTag ---------------')
    count = 0
    # Skip Tag
    print('1.→  คน (ร้าย) + กระทำ (ผิด)*')
    skip_result1 = rst.rule1(list_tag_1)
    print_rule_result(skip_result1, 1)
    count += count_result(skip_result1)
    print('------------------------------')
    print('Result Count SkipTag R1 : ', count)
    # wr.export_rule(skip_result1, 1, str(n), 'SkipTag', count)

    print('\n')
    count = 0
    print('2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*')
    skip_result2 = rst.rule2(list_tag_2)
    print_rule_result(skip_result2, 2)
    count += count_result(skip_result2)
    print('------------------------------')
    print('Result Count SkipTag R2 : ', count)
    # wr.export_rule(skip_result2, 2, str(n), 'SkipTag', count)

    print('\n')
    count = 0
    print('3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)')
    skip_result3 = rst.rule3(list_tag_3)
    print_rule_result(skip_result3, 3)
    count += count_result(skip_result3)
    print('------------------------------')
    print('Result Count SkipTag R3 : ', count)
    # wr.export_rule(skip_result3, 3, str(n), 'SkipTag', count)

    print('\n')
    count = 0
    print('4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)')
    skip_result4 = rst.rule4(list_tag_4)
    print_rule_result(skip_result4, 4)
    count += count_result(skip_result4)
    print('------------------------------')
    print('Result Count SkipTag R4 : ', count)
    # wr.export_rule(skip_result4, 4, str(n), 'SkipTag', count)


    # Output R1
    # print(nonskip_result1)
    # print('-------------- union result --------------')
    # -------------- union result --------------
    # Non Skip Tag
    u1 = union_result(nonskip_result1,list_person,1)
    u2 = union_result(nonskip_result2,list_person,2)
    u3 = union_result(nonskip_result3,list_person,3)
    u4 = union_result(nonskip_result4,list_person,4)
    u5 = union_result(nonskip_result5,list_person,5)
    u6 = union_result(nonskip_result6,list_person,6)
    u7 = union_result(nonskip_result7,list_person,7)
    # u8 = union_result(nonskip_result8,list_person)
    u13 = union_result(nonskip_result13,list_person,13)
    u14 = union_result(nonskip_result14,list_person,14)
    u15 = union_result(nonskip_result15,list_person,15)
    u16 = union_result(nonskip_result16,list_person,16)
    print('----------------CL------------------')
    # Skip Tag
    un1 = union_result(skip_result1,list_person,1)
    un2 = union_result(skip_result2,list_person,2)
    un3 = union_result(skip_result3,list_person,3)
    un4 = union_result(skip_result4,list_person,4)
    # print(u1)
    # print(u2)
    # print(u13)
    # print(u14)
    # print(u15)
    # print(u16)
    # print(u7)
    # print(u8)
    # union_result(skip_result1,list_person)
    u_result = []
    # for i in range(len(u1)):
    #     for j in range(len(u2)):
    #         if i == j:
    #             u1[i].extend(u2[j])
    # uu.extend(u1)
    # uu.extend(u2)
    # uu.extend(u3)
    # uu.extend(u4)
    # uu.extend(u5)
    # uu.extend(u6)
    # uu.extend(u7)

    u_result.append(u1)
    u_result.append(u2)
    u_result.append(u3)
    u_result.append(u4)
    u_result.append(un1)
    u_result.append(un2)
    u_result.append(un3)
    u_result.append(un4)
    u_result.append(u13)
    u_result.append(u14)
    u_result.append(u15)
    u_result.append(u16)

    # uu.append(u5)
    # uu.append(u6)
    # uu.append(u7)
    # print('----------')
    # print(u_result)
    
    # print(u1)
    u_result = join_results(u_result,list_person)
    # print('----------')
    # print(u_result)

    # print(nonskip_result1)
    # wr.export_text(str_text, str(n))
    # wr.export_rule(nonskip_result1, 1, str(n), 'NonSkipTag')
    # wr.export_rule(skip_result1, 1, str(n), 'SkipTag')
    return u_result


def findperson(list_tag):
    # print('------------- find person ------------------')
    # print(list_tag)
    # list_person = set()
    list_person = []
    list_person_firstname = []
    list_person_lastname = []

    for list_i in list_tag:
        for obj_j in list_i:
            p = None
            if str(obj_j) == 'คน':
                # if len(list_person) == 0:
                if len(list_person_firstname) == 0:
                    # print(obj_j , obj_j.firstname , '||' , obj_j.lastname)
                    list_person_firstname.append(obj_j.firstname)
                    list_person_lastname.append(obj_j.lastname)
                else:
                    if obj_j.firstname in list_person_firstname:
                        index_i = list_person_firstname.index(obj_j.firstname)
                        if list_person_lastname[index_i] == '' and obj_j.lastname != '':
                            list_person_lastname[index_i] = obj_j.lastname
                    else:
                        list_person_firstname.append(obj_j.firstname)
                        list_person_lastname.append(obj_j.lastname)

    for i in range(len(list_person_firstname)):
        for j in range(len(list_person_lastname)):
            if i == j:
                # p = obj.Person(list_person_firstname[i],list_person_lastname[j])
                # list_person.append(p)
                list_person.append({'firstname': list_person_firstname[i],'lastname': list_person_lastname[j]})

    return list_person


def union_result(result_rule,list_person,number_rule):
    # print('----------------- union -----------------')
    # villain = set()
    villain = []
    action_1 = []
    action_2 = []
    victim = []
    officer = []
    location = []

    for list_i in result_rule:
        for tuble_j in list_i:
            for obj_index in tuble_j:
                if str(obj_index) == 'คน':
                    if obj_index.status == 'คนร้าย':
                        if obj_index.firstname != 'ผู้ต้องหา':
                            if obj_index.firstname == 'ด.ญ.':
                                obj_index.firstname = 'เด็กหญิง'
                            # print(obj_index.status,obj_index.firstname,obj_index.lastname)
                            villain.append(obj_index.firstname)

                    elif obj_index.status == 'คนเสียหาย':
                        if obj_index.firstname != 'ผู้เสียหาย':
                            if obj_index.firstname == 'ด.ญ.':
                                obj_index.firstname = 'เด็กหญิง'
                            # print(obj_index.status,obj_index.firstname,obj_index.lastname)
                            victim.append(obj_index.firstname)

                    elif obj_index.status == 'เจ้าหน้าที่':
                        officer.append(obj_index.firstname)

                if number_rule == 1 or number_rule == 2 or number_rule == 3 or number_rule == 4:
                    if str(obj_index) == 'กระทำ1':
                        action_1.append(obj_index.name_action)
                elif number_rule == 13 or number_rule == 14 or number_rule == 15 or number_rule == 16:
                    if str(obj_index) == 'สถานที่':
                        # print(number_rule)
                        location.append(obj_index.split_location)
                if number_rule == 1:
                    if str(obj_index) == 'กระทำ2':
                        action_2.append(obj_index.name_action)


    # print('=====--===--===-=-=-=-=')
    # print(location)
    # print('----------------')
    villain = unique_array(villain)
    # print(villain)
    action_1 = unique_array(action_1)
    # print(action_1)
    action_2 = unique_array(action_2)
    # print(action_2)
    victim = unique_array(victim)
    # print(victim)
    officer = unique_array(officer)
    # print(officer)

    # print(str(villain))
    # add lastname form list_person when listname is empty and listperson have lastname
    # for i in range(len(villain)):
    #     for j in range(len(list_person)):
    #         if villain[i].firstname == list_person[j].firstname:
    #             if villain[i].lastname == '' and list_person[j].lastname != '':
    #                 villain[i].lastname = list_person[j].lastname
    #                 # print(villain[i].firstname,villain[i].lastname)

    list_obj = []
    # list_obj.append(villain)
    # list_obj.append(action_1)
    # list_obj.append(victim)
    # list_obj.append([])
    # list_obj.append(officer)
    if number_rule == 1 or number_rule == 2 or number_rule == 3 or number_rule == 4:
        list_obj.append(villain)
        list_obj.append(action_1)
        list_obj.append(victim)
        list_obj.append(location)
    elif number_rule == 13 or number_rule == 14 or number_rule == 15 or number_rule == 16:
        list_obj.append(villain)
        list_obj.append(action_1)
        list_obj.append(victim)
        list_obj.append(location)
    # elif 
    # print(list_obj)
    # print('------------------- output --------------------')

    # # add lastname form list_person
    # villain_list = []
    # for i in range(len(villain)):
    #     for j in range(len(list_person)):
    #         if villain[i] == list_person[j].get('firstname'):
    #             villain_list.append({'firstname': villain[i],'lastname': list_person[j].get('lastname'),'status': 'คนร้าย'})
    # print(villain_list)
    # # list action to dict action
    # action_1_dict = []
    # for action in action_1:
    #     action_1_dict.append({'name':action})
    # print(action_1_dict)
    
    return list_obj


def unique_array(list_array):
    list_array = np.array(list_array)
    list_array = np.unique(list_array)
    list_array = list_array.tolist()
    return list_array


def join_results(union_result,list_person):
    list_villain = []
    list_action1 = []
    list_victim = []
    list_location = []
    # print('------------ check result ------------')
    # print(union_result[0])
    # print(union_result[0][0])
    # print(union_result[0][1])
    # print(union_result[0][2])
    for i in range(len(union_result)):
        for j in range(len(union_result[i])):
            for k in range(len(union_result[i][j])):
                if j == 0:
                    list_villain.append(union_result[i][j][k])
                elif j == 1:
                    list_action1.append(union_result[i][j][k])
                elif j == 2:
                    list_victim.append(union_result[i][j][k])
                elif j == 3:
                    list_location.append(union_result[i][j][k])

    # print(list_villain)
    # print(list_action1)
    # print(list_victim)

    list_villain = unique_array(list_villain)
    # print(list_villain)
    list_action1 = unique_array(list_action1)
    # print(list_action1)
    list_victim = unique_array(list_victim)
    # print(list_victim)

    # add lastname form list_person when listname is empty and listperson have lastname
    villain = []
    for i in range(len(list_villain)):
        for j in range(len(list_person)):
            if list_villain[i] == list_person[j].get('firstname'):
                villain.append({'firstname': list_villain[i],'lastname': list_person[j].get('lastname'),'status': 'คนร้าย'})
    # print(villain)

    action_1 = []
    for action in list_action1:
        action_1.append({'name':action})
    # print(action_1)

    victim = []
    for i in range(len(list_victim)):
        for j in range(len(list_person)):
            if list_victim[i] == list_person[j].get('firstname'):
                victim.append({'firstname': list_victim[i],'lastname': list_person[j].get('lastname'),'status': 'คนเสียหาย'})
    # print(victim)
    r = obj.Result(villain,action_1,victim,list_location)
    # print(r.__dict__)
    # pprint(r.__dict__)

    return r

def convert_obj_json(result_obj):
    a = ''


# def insert_database(result):
#     # 2 list
#     r = obj.Result(result)
#     print(r.__dict__)
#     list_r = []
#     list_r.append(r.__dict__)
#     print(list_r)
#   client = MongoClient('localhost', 27017)
    # db = client.get_database("datanews")
    # news = db.news
    # news.insert_many(list_r)

    # client = MongoClient('mongodb+srv://wathiwut193:<Cc2191996>@cluster0-pjudc.mongodb.net/test?retryWrites=true', 27017)
    # db = client.get_database("news")
    # news = db.datanews
    # news.insert_many(list_r)