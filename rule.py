import ngram
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
        print('Empty')
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
    # print_in_obj(list_tag_2d)
    list_tag_1 = tag_to_obj(list_text2d)
    list_tag_2 = tag_to_obj(list_text2d)
    list_tag_3 = tag_to_obj(list_text2d)
    list_tag_4 = tag_to_obj(list_text2d)
    list_tag_5 = tag_to_obj(list_text2d)
    list_tag_6 = tag_to_obj(list_text2d)
    list_tag_7 = tag_to_obj(list_text2d)
    list_tag_8 = tag_to_obj(list_text2d)

    wr.export_obj(list_tag_2d, str(n))

    # 1.→  คน (ร้าย) + กระทำ (ผิด)*
    print('--------------- Rule Result NonSkipTag ---------------')
    count = 0
    # Non Skip Tag
    nonskip_result1 = rnt.rule1(list_tag_1)
    print_rule_result(nonskip_result1, 1)
    count += count_result(nonskip_result1)
    print('------------------------------')
    print('Result Count NonSkipTag R1 : ', count)

    print('--------------- Rule Result SkipTag ---------------')
    count = 0
    # Skip Tag
    skip_result1 = rst.rule1(list_tag_1)
    print_rule_result(skip_result1, 1)
    count += count_result(skip_result1)
    print('------------------------------')
    print('Result Count SkipTag R1 : ', count)

    # Output R1
    wr.export_text(str_text, str(n))
    wr.export_rule(nonskip_result1, 1, str(n), 'NonSkipTag')
    wr.export_rule(skip_result1, 1, str(n), 'SkipTag')


import ngram
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
        print('Empty')
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
    # print_in_obj(list_tag_2d)
    list_tag_1 = tag_to_obj(list_text2d)
    list_tag_2 = tag_to_obj(list_text2d)
    list_tag_3 = tag_to_obj(list_text2d)
    list_tag_4 = tag_to_obj(list_text2d)
    list_tag_5 = tag_to_obj(list_text2d)
    list_tag_6 = tag_to_obj(list_text2d)
    list_tag_7 = tag_to_obj(list_text2d)
    list_tag_8 = tag_to_obj(list_text2d)

    wr.export_obj(list_tag_2d, str(n))

    # 1.→  คน (ร้าย) + กระทำ (ผิด)*
    print('--------------- Rule Result NonSkipTag ---------------')
    count = 0
    # Non Skip Tag
    nonskip_result1 = rnt.rule1(list_tag_1)
    print_rule_result(nonskip_result1, 1)
    count += count_result(nonskip_result1)
    print('------------------------------')
    print('Result Count NonSkipTag R1 : ', count)

    print('--------------- Rule Result SkipTag ---------------')
    count = 0
    # Skip Tag
    skip_result1 = rst.rule1(list_tag_1)
    print_rule_result(skip_result1, 1)
    count += count_result(skip_result1)
    print('------------------------------')
    print('Result Count SkipTag R1 : ', count)

    # Output R1
    wr.export_text(str_text, str(n))
    wr.export_rule(nonskip_result1, 1, str(n), 'NonSkipTag')
    wr.export_rule(skip_result1, 1, str(n), 'SkipTag')

