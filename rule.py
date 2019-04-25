import ngram
import class_object as obj
from pprint import pprint

"""
function test rule search 
"""


def rule_strat(str_text):
    list_text2d = split_column(str_text)
    list_tag_2d = tag_to_obj(list_text2d)
    print(list_text2d)
    return list_tag_2d


def split_column(str_text):
    list_text = str_text.split('\r\n')
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
    list_tag_action = ['<กระทำ1>', '<กระทำ2>', '<กระทำ3>', '<กระทำ4>', '<กระทำ5>', '<กระทำ6>', '<กระทำ7>', '<กระทำ8>']
    list_tag_verb = ['<คำบ่งบอก>', '<คำบ่งบอก2>', '<คำบ่งบอก3>']
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

    person_tag = ngram.NGram(list_tag_person)
    action_tag = ngram.NGram(list_tag_action)
    verb_tag = ngram.NGram(list_tag_verb)
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

    list_tag_2d = []
    check_l = False

    for i in range(len(list_tag_text)):
        list_tag_2d.append([])
        for j in range(len(list_tag_text[i])):
            check_location = False

            if person_tag.search(list_tag_text[i][j], threshold=1.0):
                if j + 2 <= len(list_tag_text[i]):
                    if list_tag_text[i][j + 2] != '</คน>':
                        p = obj.Person(list_tag_text[i][j + 1], list_tag_text[i][j + 2])
                    else:
                        p = obj.Person(list_tag_text[i][j + 1])

                    list_tag_2d[i].append(p)

            elif action_tag.search(list_tag_text[i][j], threshold=1.0):
                a = obj.Action(list_tag_text[i][j + 1], list_tag_text[i][j][1:len(list_tag_text[i][j]) - 1])
                list_tag_2d[i].append(a)

            elif verb_tag.search(list_tag_text[i][j], threshold=1.0):

                if (list_tag_text[i][j][len(list_tag_text[i][j]) - 2] == '2' or
                        list_tag_text[i][j][len(list_tag_text[i][j]) - 2] == '3'):
                    v = obj.Verb(list_tag_text[i][j + 1], list_tag_text[i][j][len(list_tag_text[i][j]) - 2])
                else:
                    v = obj.Verb(list_tag_text[i][j + 1])
                list_tag_2d[i].append(v)

            elif location_tag.search(list_tag_text[i][j], threshold=1.0):
                if check_l != True:
                    check_l = True
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

                    while (check_r != True):
                        # print(count_r)
                        if country_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            country = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif province_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            # print(list_tag_text[i][count_r + 1])
                            province = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif amphoe_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            # print(list_tag_text[i][count_r + 1])
                            amphoe = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif area_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            area = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif tambon_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            tambon = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif district_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            district = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif road_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            road = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif river_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            river = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif place_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            place = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif mall_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            mall = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif hospital_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            hospital = list_tag_text[i][count_r + 1]
                            check_location = True
                        elif university_tag.search(list_tag_text[i][count_r], threshold=1.0):
                            university = list_tag_text[i][count_r + 1]
                            check_location = True

                        # if check_location == True:
                        # print(province)
                        # l = obj.Location(country,province,amphoe,area,tambon,district,road,river,place,mall,hospital,university)
                        # list_tag_2d[i].append(l)

                        if count_r == len(list_tag_text[i]) - 1:
                            check_r = True
                        else:
                            count_r += 1

                    if check_location == True and check_r == True:
                        l = obj.Location(country, province, amphoe, area, tambon, district, road, river, place, mall,
                                         hospital, university)
                        list_tag_2d[i].append(l)

    return list_tag_2d


# 1.→  คน (ร้าย) + กระทำ (ผิด)*
def rule1(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print('------------------1------------------')
    # print(list_tag_2d)

    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):

            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                """
                count_l = j
                check_l = False
                while(check_l == True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'คน':
                        check_l = True
                """
                if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย':
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index
                    # change status = คนร้าย
                    list_tag_2d[i][j - 1].status = 'คนร้าย'
                    # คน (ร้าย)
                    list_rule.append(list_tag_2d[i][j - 1])
                    # กระทำ (ผิด)
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j - 1)  # see index
                    list_index.append(j)  # see index

                    if j != len(list_tag_2d[i]) - 1:
                        count_r = j
                        check_r = False

                        while (check_r != True):

                            if count_r == len(list_tag_2d[i]) - 1:
                                count_r += 0
                            else:
                                count_r += 1

                            if count_r == len(list_tag_2d[i]) - 1:
                                if str(list_tag_2d[i][count_r]) != 'กระทำ1':
                                    # print(check_r)
                                    check_r = True
                                elif str(list_tag_2d[i][count_r]) == 'กระทำ1':
                                    # print(check_r)
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index
                                    check_r = True
                                else:
                                    check_r = True
                            else:
                                if str(list_tag_2d[i][count_r]) == 'กระทำ1':
                                    # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                    # กระทำ (ผิด)*
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index

                                elif str(list_tag_2d[i][count_r]) != 'กระทำ1':
                                    check_r = True

                    tuple_rule = tuple(list_rule)
                    result_rule[i].append(tuple_rule)
                    tuple_index = tuple(list_index)  # see index
                    result_index[i].append(tuple_index)  # see index

            elif str(list_tag_2d[i][j]) == 'กระทำ2' and j != 0 and j != len(list_tag_2d[i]):
                if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย':
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index
                    # change status = คนร้าย
                    list_tag_2d[i][j - 1].status = 'คนร้าย'
                    # คน (ร้าย)
                    list_rule.append(list_tag_2d[i][j - 1])
                    # กระทำ (ผิด)
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j - 1)  # see index
                    list_index.append(j)  # see index

                    if j != len(list_tag_2d[i]) - 1:
                        count_r = j
                        check_r = False

                        while (check_r != True):

                            if count_r == len(list_tag_2d[i]) - 1:
                                count_r += 0
                            else:
                                count_r += 1

                            if count_r == len(list_tag_2d[i]) - 1:
                                if str(list_tag_2d[i][count_r]) != 'กระทำ2':
                                    # print(check_r)
                                    check_r = True
                                elif str(list_tag_2d[i][count_r]) == 'กระทำ2':
                                    # print(check_r)
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index
                                    check_r = True
                                else:
                                    check_r = True
                            else:
                                if str(list_tag_2d[i][count_r]) == 'กระทำ2':
                                    # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                    # กระทำ (ผิด)*
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index

                                elif str(list_tag_2d[i][count_r]) != 'กระทำ2':
                                    check_r = True

                    tuple_rule = tuple(list_rule)
                    result_rule[i].append(tuple_rule)
                    tuple_index = tuple(list_index)  # see index
                    result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 1)
            return result_rule
        else:
            result('Empty', 1)
            return 'Empty'


# 2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*
def rule2(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)

    # print('------------------2------------------')

    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                # print('------------------------------------')
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    if ((str(list_tag_2d[i][count_l]) != 'คน' or list_tag_2d[i][count_l].status == 'คนเสียหาย') or str(
                            list_tag_2d[i][j - 1]) == 'คนร้าย' or count_l == -1):
                        check_l = True
                    elif ((str(list_tag_2d[i][count_l]) == 'คน' and list_tag_2d[i][count_l].status != 'คนเสียหาย')
                          or str(list_tag_2d[i][j - 1]) == 'คนร้าย'):
                        check_p_l = True
                        # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                        # change status = คนร้าย
                        list_tag_2d[i][count_l].status = 'คนร้าย'
                        # คน (ร้าย)*
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index

                if check_p_l == True:
                    # print('m',i,j,str(list_tag_2d[i][j]))
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j)  # see index
                    count_r = j
                    check_r = False
                    while (check_r != True):
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if str(list_tag_2d[i][count_r]) != 'กระทำ1' or count_r == len(list_tag_2d[i]) - 1:
                            # check_r = True
                            count_p_r = count_r - 1
                            check_p_r = False
                            count_pr = 0

                            while (check_p_r != True):

                                if count_p_r == len(list_tag_2d[i]) - 1:
                                    count_p_r += 0
                                else:
                                    count_p_r += 1

                                if count_p_r == len(list_tag_2d[i]) - 1:
                                    check_p_r = True
                                    check_r = True
                                if str(list_tag_2d[i][count_p_r]) != 'คน':
                                    check_p_r = True
                                    check_r = True
                                elif str(list_tag_2d[i][count_p_r]) == 'คน':
                                    # print('pr',i,j,count_r,str(list_tag_2d[i][count_p_r]))
                                    # count_p_r += 1
                                    count_pr += 1
                                    # change status = คนเสียหาย
                                    list_tag_2d[i][count_p_r].status = 'คนเสียหาย'
                                    # คน (เสียหาย)*
                                    list_rule.append(list_tag_2d[i][count_p_r])
                                    list_index.append(count_p_r)  # see index
                                # else:
                                # list_rule.clear
                            if count_pr > 0:
                                # list_rule.pop(0)
                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

                            # print(list_rule,tuple_rule)
                        elif str(list_tag_2d[i][count_r]) == 'กระทำ1':
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # กระทำ (ผิด)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index
                            # count_r += 1

            elif str(list_tag_2d[i][j]) == 'กระทำ2' and j != 0 and j != len(list_tag_2d[i]):
                # print('------------------------------------')
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย':
                        check_p_l = True
                        # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                        # change status = คนร้าย
                        list_tag_2d[i][count_l].status = 'คนร้าย'
                        # คน (ร้าย)*
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index

                if check_p_l == True:
                    # print('m',i,j,str(list_tag_2d[i][j]))
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j)  # see index
                    count_r = j
                    check_r = False
                    while (check_r != True):
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if str(list_tag_2d[i][count_r]) != 'กระทำ2' or count_r == len(list_tag_2d[i]) - 1:
                            # check_r = True
                            count_p_r = count_r - 1
                            check_p_r = False
                            count_pr = 0

                            while (check_p_r != True):

                                if count_p_r == len(list_tag_2d[i]) - 1:
                                    count_p_r += 0
                                else:
                                    count_p_r += 1

                                if count_p_r == len(list_tag_2d[i]) - 1:
                                    check_p_r = True
                                    check_r = True
                                if str(list_tag_2d[i][count_p_r]) != 'คน':
                                    check_p_r = True
                                    check_r = True
                                elif str(list_tag_2d[i][count_p_r]) == 'คน':
                                    # print('pr',i,j,count_r,str(list_tag_2d[i][count_p_r]))
                                    # count_p_r += 1
                                    count_pr += 1
                                    # change status = คนเสียหาย
                                    list_tag_2d[i][count_p_r].status = 'คนเสียหาย'
                                    # คน (เสียหาย)*
                                    list_rule.append(list_tag_2d[i][count_p_r])
                                    list_index.append(count_p_r)  # see index
                                # else:
                                # list_rule.clear
                            if count_pr > 0:
                                # list_rule.pop(0)
                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

                            # print(list_rule,tuple_rule)
                        elif str(list_tag_2d[i][count_r]) == 'กระทำ2':
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # กระทำ (ผิด)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index
                            # count_r += 1
                    # print('------------------------------------')

    # print(result_index) # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 2)
            return result_rule
        else:
            result('Empty', 2)
            return 'Empty'


# 3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)
def rule3(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)

    # print('------------------3------------------')
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก':

                    count_l = j - 1
                    check_l = False
                    check_p_l = False

                    while (check_l != True):
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) != 'คน' or count_l == -1:
                            check_l = True
                        elif str(list_tag_2d[i][count_l]) == 'คน':
                            check_p_l = True
                            # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                            # change status = คนเสียหาย
                            list_tag_2d[i][count_l].status = 'คนเสียหาย'
                            # คน (เสียหาย)*
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            list_index.insert(0, count_l)

                    if check_p_l == True:
                        # คำ (บ่งบอกว่าถูกกระทำ)
                        list_rule.append(list_tag_2d[i][j - 1])
                        # กระทำ (ผิด)
                        list_rule.append(list_tag_2d[i][j])
                        list_index.append(j - 1)  # see index
                        list_index.append(j)  # see index
                        # print('v',i,j-1,str(list_tag_2d[i][j-1]))
                        # print('a',i,j,str(list_tag_2d[i][j]))

                        if j != len(list_tag_2d[i]) - 1:
                            if str(list_tag_2d[i][j + 1]) == 'คน' or str(list_tag_2d[i][j + 1]) == 'คนร้าย':
                                # print('pr',i,j,str(list_tag_2d[i][j+1]))
                                # คน (ร้าย)
                                list_rule.append(list_tag_2d[i][j + 1])
                                list_index.append(j + 1)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

            elif str(list_tag_2d[i][j]) == 'กระทำ2' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก':

                    count_l = j - 1
                    check_l = False
                    check_p_l = False

                    while (check_l != True):
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) != 'คน' or count_l == -1:
                            check_l = True
                        elif str(list_tag_2d[i][count_l]) == 'คน':
                            check_p_l = True
                            # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                            # change status = คนเสียหาย
                            list_tag_2d[i][count_l].status = 'คนเสียหาย'
                            # คน (เสียหาย)*
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            list_index.insert(0, count_l)

                    if check_p_l == True:
                        # คำ (บ่งบอกว่าถูกกระทำ)
                        list_rule.append(list_tag_2d[i][j - 1])
                        # กระทำ (ผิด)
                        list_rule.append(list_tag_2d[i][j])
                        list_index.append(j - 1)  # see index
                        list_index.append(j)  # see index
                        # print('v',i,j-1,str(list_tag_2d[i][j-1]))
                        # print('a',i,j,str(list_tag_2d[i][j]))

                        if j != len(list_tag_2d[i]) - 1:
                            if str(list_tag_2d[i][j + 1]) == 'คน' or str(list_tag_2d[i][j + 1]) == 'คนร้าย':
                                # print('pr',i,j,str(list_tag_2d[i][j+1]))
                                # คน (ร้าย)
                                list_rule.append(list_tag_2d[i][j + 1])
                                list_index.append(j + 1)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index
    # print(result_index) # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 3)
            return result_rule
        else:
            result('Empty', 3)
            return 'Empty'


# 4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)
def rule4(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)

    # print('------------------4------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if (str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย') and j - 1 != 0:
                    if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                        if str(list_tag_2d[i][j - 3]) == 'คน' and j - 3 != 0:
                            # change status = คนเสียหาย
                            list_tag_2d[i][j - 3].status = 'คนเสียหาย'
                            # คน(เสียหาย)
                            list_rule.append(list_tag_2d[i][j - 3])
                            # คำ (บ่งบอกว่าถูกกระทำ)
                            list_rule.append(list_tag_2d[i][j - 2])
                            # change status = คนร้าย
                            list_tag_2d[i][j - 1].status = 'คนร้าย'
                            # คน(ร้าย)
                            list_rule.append(list_tag_2d[i][j - 1])
                            # กระทำ(ผิด)
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j - 3)  # see index
                            list_index.append(j - 2)  # see index
                            list_index.append(j - 1)  # see index
                            list_index.append(j)  # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

            elif str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if (str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย') and j - 1 != 0:
                    if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                        if str(list_tag_2d[i][j - 3]) == 'คน' and j - 3 != 0:
                            # change status = คนเสียหาย
                            list_tag_2d[i][j - 3].status = 'คนเสียหาย'
                            # คน(เสียหาย)
                            list_rule.append(list_tag_2d[i][j - 3])
                            # คำ (บ่งบอกว่าถูกกระทำ)
                            list_rule.append(list_tag_2d[i][j - 2])
                            # change status = คนร้าย
                            list_tag_2d[i][j - 1].status = 'คนร้าย'
                            # คน(ร้าย)
                            list_rule.append(list_tag_2d[i][j - 1])
                            # กระทำ(ผิด)
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j - 3)  # see index
                            list_index.append(j - 2)  # see index
                            list_index.append(j - 1)  # see index
                            list_index.append(j)  # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

    # print(result_index) # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 4)
            return result_rule
        else:
            result('Empty', 4)
            return 'Empty'


# 5.→ คน (เจ้าหน้าที่)* + กระทำ3* +- คน (ร้าย)
def rule5(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)

    # print('------------------5------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if (str(list_tag_2d[i][j]) == 'กระทำ3' or str(list_tag_2d[i][j]) == 'กระทำ37') and j != 0 and j != len(
                    list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'คน' or str(
                            list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่':
                        check_p_l = True
                        # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                        # change status = เจ้าหน้าที่
                        list_tag_2d[i][count_l].status = 'เจ้าหน้าที่'
                        # คน (เจ้าหน้าที่)*
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index

                if check_p_l == True:
                    if j != len(list_tag_2d[i]) - 1:
                        # print('m',i,j,str(list_tag_2d[i][j]))
                        # กระทำ
                        list_rule.append(list_tag_2d[i][j])
                        list_index.append(j)  # see index
                        count_r = j
                        check_r = False
                        while (check_r != True):
                            if count_r == len(list_tag_2d[i]) - 1:
                                count_r += 0
                            else:
                                count_r += 1

                            if (str(list_tag_2d[i][count_r]) != 'กระทำ3' and str(
                                    list_tag_2d[i][j]) != 'กระทำ37') or count_r == len(list_tag_2d[i]) - 1:
                                check_r = True
                            if str(list_tag_2d[i][count_r]) == 'กระทำ3' or str(list_tag_2d[i][j]) == 'กระทำ37':
                                # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                # กระทำ*
                                list_rule.append(list_tag_2d[i][count_r])
                                list_index.append(count_r)  # see index

                        count_p_r = count_r - 1
                        if count_p_r != len(list_tag_2d[i]) - 1:
                            if str(list_tag_2d[i][count_p_r + 1]) == 'คน' or str(
                                    list_tag_2d[i][count_p_r + 1]) == 'คนร้าย':
                                # print('pr',i,j,str(list_tag_2d[i][j+1]))
                                # คน (ร้าย)
                                list_rule.append(list_tag_2d[i][count_p_r + 1])
                                list_index.append(count_p_r + 1)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 5)
            return result_rule
        else:
            result('Empty', 5)
            return 'Empty'


# 6.→ คน (เจ้าหน้าที่) + กระทำ + คน (เสียหาย)* + กระทำ
def rule6(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d)

    # print('------------------6------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ4' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่' and j - 1 != 0:
                    list_rule.append(list_tag_2d[i][j - 1])
                    list_rule.append(list_tag_2d[i][j])

                    list_index.append(j - 1)  # see index
                    list_index.append(j)  # see index
                    # print(list_tag_2d[i][j-1])
                    # print(list_tag_2d[i][j])

                    count_r = j
                    check_r = False
                    check_pr = False
                    while (check_r != True):
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if str(list_tag_2d[i][count_r]) != 'คน' or count_r == len(list_tag_2d[i]) - 1:
                            check_r = True
                        elif str(list_tag_2d[i][count_r]) == 'คน':
                            check_pr = True
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # กระทำ (ผิด)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index
                            # count_r += 1

                    if check_pr == True:
                        count_p_r = count_r - 1
                        if str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ5' or count_p_r + 1 != len(list_tag_2d[i]) - 1:
                            # print(list_tag_2d[i][count_p_r+1])
                            list_rule.append(list_tag_2d[i][count_p_r + 1])

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

            elif str(list_tag_2d[i][j]) == 'กระทำ3' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                if list_tag_2d[i][j].name_action == 'รับแจ้ง':
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index

                    if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่' and j - 1 != 0:
                        list_rule.append(list_tag_2d[i][j - 1])
                        list_rule.append(list_tag_2d[i][j])

                        list_index.append(j - 1)  # see index
                        list_index.append(j)  # see index
                        # print(list_tag_2d[i][j-1])
                        # print(list_tag_2d[i][j])

                        count_r = j
                        check_r = False
                        check_pr = False
                        while (check_r != True):
                            if count_r == len(list_tag_2d[i]) - 1:
                                count_r += 0
                            else:
                                count_r += 1

                            if str(list_tag_2d[i][count_r]) != 'คน' or count_r == len(list_tag_2d[i]) - 1:
                                check_r = True
                            elif str(list_tag_2d[i][count_r]) == 'คน':
                                check_pr = True
                                # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                # กระทำ (ผิด)*
                                list_rule.append(list_tag_2d[i][count_r])
                                list_index.append(count_r)  # see index
                                # count_r += 1

                        if check_pr == True:
                            count_p_r = count_r - 1
                            if str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ5' or count_p_r + 1 != len(
                                    list_tag_2d[i]) - 1:
                                # print(list_tag_2d[i][count_p_r+1])
                                list_rule.append(list_tag_2d[i][count_p_r + 1])

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

            elif str(list_tag_2d[i][j]) == 'กระทำ8' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                if list_tag_2d[i][j].name_action == 'แจ้งความ':
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index

                    if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่' and j - 1 != 0:
                        list_rule.append(list_tag_2d[i][j - 1])
                        list_rule.append(list_tag_2d[i][j])

                        list_index.append(j - 1)  # see index
                        list_index.append(j)  # see index
                        # print(list_tag_2d[i][j-1])
                        # print(list_tag_2d[i][j])

                        count_r = j
                        check_r = False
                        check_pr = False
                        while (check_r != True):
                            if count_r == len(list_tag_2d[i]) - 1:
                                count_r += 0
                            else:
                                count_r += 1

                            if str(list_tag_2d[i][count_r]) != 'คน' or count_r == len(list_tag_2d[i]) - 1:
                                check_r = True
                            elif str(list_tag_2d[i][count_r]) == 'คน':
                                check_pr = True
                                # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                # กระทำ (ผิด)*
                                list_rule.append(list_tag_2d[i][count_r])
                                list_index.append(count_r)  # see index
                                # count_r += 1

                        if check_pr == True:
                            count_p_r = count_r - 1
                            if str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ5' or count_p_r + 1 != len(
                                    list_tag_2d[i]) - 1:
                                # print(list_tag_2d[i][count_p_r+1])
                                list_rule.append(list_tag_2d[i][count_p_r + 1])

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 6)
            return result_rule
        else:
            result('Empty', 6)
            return 'Empty'


# 7.→ คน (เสียหาย)* + กระทำ + คน (เจ้าหน้าที่)
def rule7(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d)

    # print('------------------7------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ5' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'คน' or str(
                            list_tag_2d[i][j - 1]) == 'คนเสียหาย' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนเสียหาย':
                        check_p_l = True
                        # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                        # change status = คนร้าย
                        list_tag_2d[i][count_l].status = 'คนเสียหาย'
                        # คน (เสียหาย)*
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index

                if check_p_l == True:
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j)  # see index

                    count_r = j
                    check_r = False
                    count_pr = 0
                    # print('r',i,j,count_r,str(list_tag_2d[i][count_r+1]))
                    while (check_r != True):
                        # print(count_r)
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if count_r == len(list_tag_2d[i]) - 1:
                            check_r = True
                        if str(list_tag_2d[i][count_r]) != 'คน':
                            check_r = True
                        elif str(list_tag_2d[i][count_r]) == 'คน':
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # คน (เจ้าหน้าที่)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index
                            count_pr += 1
                    """
                    if j != len(list_tag_2d[i])-1:
                        if str(list_tag_2d[i][j+1]) == 'คน' or str(list_tag_2d[i][j+1]) == 'เจ้าหน้าที่':
                            list_rule.append(list_tag_2d[i][j+1])
                            list_index.append(j+1) # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index) # see index
                            result_index[i].append(tuple_index) # see index
                    """

                    if count_pr >= 1:
                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 7)
            return result_rule
        else:
            result('Empty', 7)
            return 'Empty'

        # 8.→ คน (ร้าย) + กระทำ + คน (เจ้าหน้าที่)


def rule8(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d)

    # print('------------------8------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ6' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนร้าย':
                    list_rule.append(list_tag_2d[i][j - 1])
                    list_index.append(j - 1)
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j)

                    count_r = j
                    check_r = False
                    count_pr = 0
                    # print('r',i,j,count_r,str(list_tag_2d[i][count_r+1]))
                    while (check_r != True):
                        # print(count_r)
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if count_r == len(list_tag_2d[i]) - 1:
                            check_r = True
                        if str(list_tag_2d[i][count_r]) != 'คน':
                            check_r = True
                        elif str(list_tag_2d[i][count_r]) == 'คน':
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # คน (เจ้าหน้าที่)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index
                            count_pr += 1
                    """
                    if j != len(list_tag_2d[i])-1:
                        if str(list_tag_2d[i][j+1]) == 'คน' or str(list_tag_2d[i][j+1]) == 'เจ้าหน้าที่':
                            list_rule.append(list_tag_2d[i][j+1])
                            list_index.append(j+1) # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index) # see index
                            result_index[i].append(tuple_index) # see index
                    """
                    if count_pr >= 1:
                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(status_rule)
    # print(result_index)

    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 8)
            return result_rule
        else:
            result('Empty', 8)
            return 'Empty'


# 9.→ คน (ร้าย) + คำ (บ่งบอกว่าถูกกระทำ) +- เจ้าหน้าที่ + กระทำ *** เหมือน3.
def rule9(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d)

    # print('------------------9------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ3' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                if (list_tag_2d[i][j].name_action == 'จับกุม' or list_tag_2d[i][j].name_action == 'จับ'
                        or list_tag_2d[i][j].name_action == 'วิสามัญ'):
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index

                    if (str(list_tag_2d[i][j - 1]) == 'คน' or str(
                            list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่') and j - 1 != 0:
                        # print(list_tag_2d[i][j-1])
                        if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                            # print(list_tag_2d[i][j-2])
                            if (str(list_tag_2d[i][j - 3]) == 'คน' or str(list_tag_2d[i][j - 3]) == 'คนร้าย'):
                                # print(list_tag_2d[i][j-3])
                                # print(list_tag_2d[i][j-2])
                                # print(list_tag_2d[i][j-1])
                                # print(list_tag_2d[i][j])

                                list_rule.append(list_tag_2d[i][j - 3])
                                list_rule.append(list_tag_2d[i][j - 2])
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j - 3)
                                list_index.append(j - 2)
                                list_index.append(j - 1)
                                list_index.append(j)

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index


                    elif str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก' and j - 1 != 0:
                        if (str(list_tag_2d[i][j - 2]) == 'คน' or str(list_tag_2d[i][j - 2]) == 'คนร้าย'):
                            # print(list_tag_2d[i][j-2])
                            # print(list_tag_2d[i][j-1])
                            # print(list_tag_2d[i][j])

                            list_rule.append(list_tag_2d[i][j - 2])
                            list_rule.append(list_tag_2d[i][j - 1])
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j - 2)
                            list_index.append(j - 1)
                            list_index.append(j)

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index
            elif str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                if list_tag_2d[i][j].name_action == 'ยิง':
                    list_rule = []
                    tuple_rule = ()
                    list_index = []  # see index
                    tuple_index = ()  # see index

                    if (str(list_tag_2d[i][j - 1]) == 'คน' or str(
                            list_tag_2d[i][j - 1]) == 'เจ้าหน้าที่') and j - 1 != 0:
                        # print(list_tag_2d[i][j-1])
                        if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                            # print(list_tag_2d[i][j-2])
                            if (str(list_tag_2d[i][j - 3]) == 'คน' or str(list_tag_2d[i][j - 3]) == 'คนร้าย'):
                                # print(list_tag_2d[i][j-3])
                                # print(list_tag_2d[i][j-2])
                                # print(list_tag_2d[i][j-1])
                                # print(list_tag_2d[i][j])

                                list_rule.append(list_tag_2d[i][j - 3])
                                list_rule.append(list_tag_2d[i][j - 2])
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j - 3)
                                list_index.append(j - 2)
                                list_index.append(j - 1)
                                list_index.append(j)

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index


                    elif str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก' and j - 1 != 0:
                        if (str(list_tag_2d[i][j - 2]) == 'คน' or str(list_tag_2d[i][j - 2]) == 'คนร้าย'):
                            # print(list_tag_2d[i][j-2])
                            # print(list_tag_2d[i][j-1])
                            # print(list_tag_2d[i][j])

                            list_rule.append(list_tag_2d[i][j - 2])
                            list_rule.append(list_tag_2d[i][j - 1])
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j - 2)
                            list_index.append(j - 1)
                            list_index.append(j)

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 9)
            return result_rule
        else:
            result('Empty', 9)
            return 'Empty'


# 10.→ คน (เสียหาย) + กระทำ*  + เกริ่น 3 +- คน (ร้าย) *** เหมือน 6.
def rule10(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d)

    # print('------------------10------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ8' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน' or str(list_tag_2d[i][j - 1]) == 'คนเสียหาย':
                    # print(list_tag_2d[i][j-1])
                    # print(list_tag_2d[i][j])
                    list_rule.append(list_tag_2d[i][j - 1])
                    list_index.append(j - 1)  # see index
                    list_rule.append(list_tag_2d[i][j])
                    list_index.append(j)  # see index

                    count_r = j
                    check_r = False
                    while (check_r != True):
                        if count_r == len(list_tag_2d[i]) - 1:
                            count_r += 0
                        else:
                            count_r += 1

                        if str(list_tag_2d[i][count_r]) != 'กระทำ8' or count_r == len(list_tag_2d[i]) - 1:
                            check_r = True
                        if str(list_tag_2d[i][count_r]) == 'กระทำ8':
                            # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                            # กระทำ (ผิด)*
                            list_rule.append(list_tag_2d[i][count_r])
                            list_index.append(count_r)  # see index

                    count_ar = count_r - 1
                    if str(list_tag_2d[i][count_ar + 1]) == 'คำบ่งบอก3':
                        # print(list_tag_2d[i][count_ar+1])
                        list_rule.append(list_tag_2d[i][count_ar + 1])
                        list_index.append(count_ar + 1)  # see index

                        if count_ar + 2 <= len(list_tag_2d[i]) - 1:
                            if (str(list_tag_2d[i][count_ar + 2]) == 'คน' or str(
                                    list_tag_2d[i][count_ar + 2]) == 'คนร้าย'):
                                # print(list_tag_2d[i][count_ar+2])
                                list_rule.append(list_tag_2d[i][count_ar + 2])
                                list_index.append(count_ar + 2)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 10)
            return result_rule
        else:
            result('Empty', 10)
            return 'Empty'


# 11.→ คน (ร้าย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ)
# 12.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (ร้าย)
def rule11(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d[0][0].status)

    # print('------------------11------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'คำบ่งบอก2' and j != 0 and j != len(list_tag_2d[i]) - 1:  # คำบ่งบอก2
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน':
                    if list_tag_2d[i][j - 1].status == 'คนร้าย':
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            if list_tag_2d[i][j + 1].status != 'คนร้าย' and list_tag_2d[i][j + 1].status != 'คนเสียหาย':
                                # print(str(list_tag_2d[i][j-1]))
                                # print(str(list_tag_2d[i][j]))
                                # print(str(list_tag_2d[i][j+1]))
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_index.append(j - 1)  # see index
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j)  # see index
                                list_rule.append(list_tag_2d[i][j + 1])
                                list_index.append(j + 1)  # see index

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

                elif (str(list_tag_2d[i][j - 1]) == 'คน' and list_tag_2d[i][j - 1].status != 'คนร้าย'):
                    if str(list_tag_2d[i][j + 1]) == 'คน':
                        if list_tag_2d[i][j + 1].status == 'คนร้าย':
                            # print(str(list_tag_2d[i][j-1]))
                            # print(str(list_tag_2d[i][j]))
                            # print(str(list_tag_2d[i][j+1]))
                            list_rule.append(list_tag_2d[i][j - 1])
                            list_index.append(j - 1)  # see index
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j)  # see index
                            list_rule.append(list_tag_2d[i][j + 1])
                            list_index.append(j + 1)  # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 11)
            return result_rule
        else:
            result('Empty', 11)
            return 'Empty'


# 13.→ คน (เสียหาย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ)
# 14.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (เสียหาย)
def rule12(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    # list_tag_text = cut_untag(list_text2d)
    list_tag_2d = tag_to_obj(list_text2d)
    # print(list_tag_2d[0][0].status)

    # print('------------------11------------------')
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'คำบ่งบอก2' and j != 0 and j != len(list_tag_2d[i]) - 1:  # คำบ่งบอก2
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน':
                    if list_tag_2d[i][j - 1].status == 'คนเสียหาย':
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            if list_tag_2d[i][j + 1].status != 'คนร้าย':
                                # print(list_tag_2d[i][j-1])
                                # print(list_tag_2d[i][j])
                                # print(list_tag_2d[i][j+1])

                                # print(str(list_tag_2d[i][j-1]))
                                # print(str(list_tag_2d[i][j]))
                                # print(str(list_tag_2d[i][j+1]))
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_index.append(j - 1)  # see index
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j)  # see index
                                list_rule.append(list_tag_2d[i][j + 1])
                                list_index.append(j + 1)  # see index

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

                elif (str(list_tag_2d[i][j - 1]) == 'คน' and list_tag_2d[i][j - 1].status != 'คนร้าย'):
                    if str(list_tag_2d[i][j + 1]) == 'คน':
                        if list_tag_2d[i][j + 1].status == 'คนเสียหาย':
                            # print(list_tag_2d[i][j-1])
                            # print(list_tag_2d[i][j])
                            # print(list_tag_2d[i][j+1])

                            # print(str(list_tag_2d[i][j-1]))
                            # print(str(list_tag_2d[i][j]))
                            # print(str(list_tag_2d[i][j+1]))
                            list_rule.append(list_tag_2d[i][j - 1])
                            list_index.append(j - 1)  # see index
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j)  # see index
                            list_rule.append(list_tag_2d[i][j + 1])
                            list_index.append(j + 1)  # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
            # print('Empty')
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            result(result_rule, 12)
            return result_rule
        else:
            result('Empty', 12)
            return 'Empty'


# 15.→  กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
def rule13(str_text, need_count='N'):
    list_text2d = split_column(str_text)
    list_tag_2d = tag_to_obj(list_text2d)
    # print('------------------13------------------')
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                if str(list_tag_2d[i][j + 1]) == 'สถานที่':
                    a = ''


def result(result_rule, n):
    # print(result_rule)
    print('--------------- R', n, '-------------------')
    # for i in range(len(list_tag_2d)):
    #    for j in range(len(list_tag_2d[i])):
    #        print(i,j,str(list_tag_2d[i][j]))
    # print('----------------C-------------------')

    if result_rule == 'Empty':
        print('Empty')
    else:
        for i in range(len(result_rule)):
            for j in range(len(result_rule[i])):
                print('-----------------------------------')
                for k in range(len(result_rule[i][j])):
                    # if 'Person' in result_rule[i][j][k]:
                    #    print(result_rule[i][j][k].firstname , result_rule[i][j][k].lastname)
                    if str(result_rule[i][j][k]) == 'คน':
                        print(result_rule[i][j][k].status, ':', result_rule[i][j][k].firstname,
                              result_rule[i][j][k].lastname)
                    elif (str(result_rule[i][j]) == 'กระทำ17' or str(result_rule[i][j]) == 'กระทำ37'
                          or str(result_rule[i][j]) == 'กระทำ34' or str(result_rule[i][j]) == 'กระทำ58'
                          or str(result_rule[i][j][k]) == 'กระทำ1' or str(result_rule[i][j][k]) == 'กระทำ3'
                          or str(result_rule[i][j][k]) == 'กระทำ4' or str(result_rule[i][j][k]) == 'กระทำ5'
                          or str(result_rule[i][j][k]) == 'กระทำ6' or str(result_rule[i][j][k]) == 'กระทำ7'
                          or str(result_rule[i][j][k]) == 'กระทำ8'):
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].name_action)
                    elif (str(result_rule[i][j][k]) == 'คำบ่งบอก' or str(result_rule[i][j][k]) == 'คำบ่งบอก2'
                          or str(result_rule[i][j][k]) == 'คำบ่งบอก3'):
                        print(str(result_rule[i][j][k]), ':', result_rule[i][j][k].name_verb)

    # print(result_rule)
    # print(result_rule[i][j][0].name_action)


def count_result(str_text):
    count1 = rule1(str_text, 'Y')
    count2 = rule2(str_text, 'Y')
    count3 = rule3(str_text, 'Y')
    count4 = rule4(str_text, 'Y')
    count5 = rule5(str_text, 'Y')
    count6 = rule6(str_text, 'Y')
    count7 = rule7(str_text, 'Y')
    count8 = rule8(str_text, 'Y')
    count9 = rule9(str_text, 'Y')
    # count10 = rule10(str_text,'Y')
    count11 = rule11(str_text, 'Y')
    count12 = rule12(str_text, 'Y')

    print('---------- index by rule ------------')
    print('------------------1------------------')
    print(count1)
    print('------------------2------------------')
    print(count2)
    print('------------------3------------------')
    print(count3)
    print('------------------4------------------')
    print(count4)
    print('------------------5------------------')
    print(count5)
    print('------------------6------------------')
    print(count6)
    print('------------------7------------------')
    print(count7)
    print('------------------8------------------')
    print(count8)
    print('------------------9------------------')
    print(count9)
    # print('------------------10------------------')
    # print(count10)
    print('------------------11------------------')
    print(count11)
    print('------------------12------------------')
    print(count12)

# for i in range(len(count3)):
#    for j in range(len(count3[i])):
#        for k in range(len(count3[i][j])):
#            print(i,j,count3[i][j][k])
