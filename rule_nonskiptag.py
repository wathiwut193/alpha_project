import ngram
import class_object as obj
import tag_object as tag
import write_file as wr
from pprint import pprint


def cut_untag(list_text2d):
    list_tag = ['<คน>', '</คน>', '<คนร้าย>', '</คนร้าย>', '<เจ้าหน้าที่>', '</เจ้าหน้าที่>',
                '<กระทำ1>', '</กระทำ1>', '<อาวุธ>', '</อาวุธ>', '<กระทำ2>', '</กระทำ2>'
                                                                            '<กระทำ3>', '</กระทำ3>', '<กระทำ4>',
                '</กระทำ4>', '<กระทำ5>', '</กระทำ5>', '<กระทำ6>', '</กระทำ6>',
                '<กระทำ7>', '</กระทำ7>', '<กระทำ8>', '</กระทำ8>',
                '<คำบ่งบอก>', '</คำบ่งบอก>', '<คำบ่งบอก2>', '</คำบ่งบอก2>', '<คำบ่งบอก3>', '</คำบ่งบอก3>',
                '<คน2>', '</คน2>']

    ng = ngram.NGram(list_tag)
    index_tag = []

    for i in range(len(list_text2d)):
        index_tag.append([])
        for j in range(len(list_text2d[i])):
            if ng.search(list_text2d[i][j], threshold=1.0):
                # print(i)
                index_tag[i].append(j)

    # print(index_tag)
    index = 0
    list_tag_text = []

    for i in range(len(list_text2d)):
        list_tag_text.append([])
        for j in range(len(list_text2d[i])):

            if len(index_tag[i]) != 0:
                # print(index_tag[i][j])
                # print(i,j)
                if index < len(index_tag[i]) - 1:
                    if j >= index_tag[i][index] and j <= index_tag[i][index + 1]:
                        list_tag_text[i].append(list_text2d[i][j])
                        # print(i,j,index,index_tag[i][index],list_text2d[i][j])

                    if j == index_tag[i][index + 1]:
                        # print(i,j,index,index_tag[i][index])

                        if j == index_tag[i][len(index_tag[i]) - 1]:
                            index = 0
                        else:
                            index += 2

    # print(list_tag_text)
    return list_tag_text


# 1.→  คน (ร้าย) + กระทำ (ผิด)*
def rule1(list_tag_2d):
    result_rule = []
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                if str(list_tag_2d[i][j - 1]) == 'คน':
                    if ((list_tag_2d[i][j - 1].status == 'คน' or list_tag_2d[i][j - 1].status == 'คนร้าย')
                            and list_tag_2d[i][j - 1].status != 'คนเสียหาย'):
                        list_rule = []
                        tuple_rule = ()
                        # change status = คนร้าย
                        list_tag_2d[i][j - 1].status = 'คนร้าย'
                        # คน (ร้าย)
                        list_rule.append(list_tag_2d[i][j - 1])
                        # กระทำ (ผิด)
                        list_rule.append(list_tag_2d[i][j])
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
                                        check_r = True
                                    else:
                                        check_r = True
                                else:
                                    if str(list_tag_2d[i][count_r]) == 'กระทำ1':
                                        # กระทำ (ผิด)*
                                        list_rule.append(list_tag_2d[i][count_r])
                                    elif str(list_tag_2d[i][count_r]) != 'กระทำ1':
                                        check_r = True
                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)

            elif str(list_tag_2d[i][j]) == 'กระทำ2' and j != 0 and j != len(list_tag_2d[i]):
                if str(list_tag_2d[i][j - 1]) == 'คน':
                    if ((list_tag_2d[i][j - 1].status == 'คน' or list_tag_2d[i][j - 1].status == 'คนร้าย')
                            and list_tag_2d[i][j - 1].status != 'คนเสียหาย'):
                        list_rule = []
                        tuple_rule = ()
                        # change status = คนร้าย
                        list_tag_2d[i][j - 1].status = 'คนร้าย'
                        # คน (ร้าย)
                        list_rule.append(list_tag_2d[i][j - 1])
                        # กระทำ (ผิด)
                        list_rule.append(list_tag_2d[i][j])
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
                                        check_r = True
                                    else:
                                        check_r = True
                                else:
                                    if str(list_tag_2d[i][count_r]) == 'กระทำ2':
                                        # กระทำ (ผิด)*
                                        list_rule.append(list_tag_2d[i][count_r])
                                    elif str(list_tag_2d[i][count_r]) != 'กระทำ2':
                                        check_r = True
                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    if status_rule == True:
        return result_rule
    else:
        return 'Empty'


# 2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*
def rule2(list_tag_2d, need_count='N'):
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
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    # if ((str(list_tag_2d[i][count_l]) != 'คน' or list_tag_2d[i][count_l].status == 'คนเสียหาย') or str(
                    #         list_tag_2d[i][j - 1]) == 'คนร้าย' or count_l == -1):
                    #     check_l = True
                    if (str(list_tag_2d[i][count_l]) != 'คน' or list_tag_2d[i][count_l].status == 'คนเสียหาย' or count_l == -1):
                        check_l = True
                    elif (str(list_tag_2d[i][count_l]) == 'คน'):
                        if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนร้าย')
                            and list_tag_2d[i][count_l].status != 'คนเสียหาย'):
                            check_p_l = True
                            # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                            # change status = คนร้าย
                            list_tag_2d[i][count_l].status = 'คนร้าย'
                            # คน (ร้าย)*
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            list_index.insert(0, count_l)  # see index

                    # elif ((str(list_tag_2d[i][count_l]) == 'คน' and list_tag_2d[i][count_l].status != 'คนเสียหาย')
                    #       or str(list_tag_2d[i][j - 1]) == 'คนร้าย'):
                    #     check_p_l = True
                    #     # print('pl',i,j,count_l,str(list_tag_2d[i][count_l]))
                    #     # change status = คนร้าย
                    #     list_tag_2d[i][count_l].status = 'คนร้าย'
                    #     # คน (ร้าย)*
                    #     list_rule.insert(0, list_tag_2d[i][count_l])
                    #     list_index.insert(0, count_l)  # see index

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

    # print(result_index) # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)
def rule3(list_tag_2d, need_count='N'):
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
                        elif (str(list_tag_2d[i][count_l]) == 'คน' or list_tag_2d[i][count_l].status == 'คนเสียหาย') and list_tag_2d[i][count_l].status != 'คนร้าย':
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
                            if str(list_tag_2d[i][j + 1]) == 'คน':
                                if list_tag_2d[i][j + 1].status != 'คนเสียหาย':
                                    # print('pr',i,j,str(list_tag_2d[i][j+1]))
                                    # คน (ร้าย)
                                    list_tag_2d[i][j + 1].status = 'คนร้าย'
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
            return result_rule
        else:
            return 'Empty'


# 4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)
def rule4(list_tag_2d, need_count='N'):
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
                if str(list_tag_2d[i][j - 1]) == 'คน' and j - 1 != 0:
                    if list_tag_2d[i][j - 1].status == 'คนร้าย' and list_tag_2d[i][j - 1].status != 'คนเสียหาย':
                        if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                            if str(list_tag_2d[i][j - 3]) == 'คน' and j - 3 != 0:
                                if list_tag_2d[i][j - 3].status == 'คนเสียหาย' and list_tag_2d[i][j - 3].status != 'คนร้าย':
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
            return result_rule
        else:
            return 'Empty'


# 5.→ คน (เจ้าหน้าที่)* + กระทำ3* +- คน (ร้าย)
def rule5(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ3' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    count_l -= 1
                    if  str(list_tag_2d[i][count_l]) != 'คน' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'คน':
                        if (list_tag_2d[i][count_l].status != 'คนเสียหาย' and list_tag_2d[i][count_l].status != 'คนร้าย'):
                            check_p_l = True
                            # print('pl',i,j,count_l,str(list_tag_2d[i][count_l].status))
                            # change status = เจ้าหน้าที่
                            list_tag_2d[i][count_l].status = 'เจ้าหน้าที่'
                            # คน (เจ้าหน้าที่)*
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            list_index.insert(0, count_l)  # see index
                        elif list_tag_2d[i][count_l].status == 'คนเสียหาย' or list_tag_2d[i][count_l].status == 'คนร้าย':
                            check_l = True

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

                            if str(list_tag_2d[i][count_r]) != 'กระทำ3' or count_r == len(list_tag_2d[i]) - 1:
                                check_r = True
                            if str(list_tag_2d[i][count_r]) == 'กระทำ3':
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
                                list_tag_2d[i][count_p_r + 1].status = 'คนร้าย'
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
            return result_rule
        else:
            return 'Empty'


# 6.→ คน (เจ้าหน้าที่) + กระทำ + คน (เสียหาย)* + กระทำ
def rule6(list_tag_2d, need_count='N'):
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

                if str(list_tag_2d[i][j - 1]) == 'คน' and j - 1 != 0:
                    if list_tag_2d[i][j - 1].status != 'คนเสียหาย' and list_tag_2d[i][j - 1].status != 'คนร้าย':
                        list_tag_2d[i][j - 1].status = 'เจ้าหน้าที่'
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
                                if list_tag_2d[i][count_r].status != 'คนร้าย':
                                    check_pr = True
                                    # print('r',i,j,count_r,str(list_tag_2d[i][count_r]))
                                    # กระทำ (ผิด)*
                                    list_tag_2d[i][count_r].status = 'คนเสียหาย'
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index
                                    # count_r += 1

                        if check_pr == True:
                            count_p_r = count_r - 1
                            if str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ5' and count_p_r + 1 != len(list_tag_2d[i]) - 1:
                                # print(list_tag_2d[i][count_p_r+1])
                                list_rule.append(list_tag_2d[i][count_p_r + 1])
                                list_index.append(count_p_r + 1)  # see index

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index
                            
                            elif str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ8' and count_p_r + 1 != len(list_tag_2d[i]) - 1:
                                if list_tag_2d[i][count_p_r + 1].name_action == 'แจ้งความ':
                                    # print(list_tag_2d[i][count_p_r+1])
                                    list_rule.append(list_tag_2d[i][count_p_r + 1])
                                    list_index.append(count_p_r + 1)  # see index

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

                    if str(list_tag_2d[i][j - 1]) == 'คน' and j - 1 != 0:
                        if list_tag_2d[i][j - 1].status != 'คนเสียหาย' and list_tag_2d[i][j - 1].status != 'คนร้าย':
                            list_tag_2d[i][j - 1].status = 'เจ้าหน้าที่'
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
                                    list_tag_2d[i][j - 1].status = 'คนเสียหาย'
                                    list_rule.append(list_tag_2d[i][count_r])
                                    list_index.append(count_r)  # see index
                                    # count_r += 1

                            if check_pr == True:
                                count_p_r = count_r - 1
                                if str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ5' and count_p_r + 1 != len(
                                        list_tag_2d[i]) - 1:
                                    # print(list_tag_2d[i][count_p_r+1])
                                    list_rule.append(list_tag_2d[i][count_p_r + 1])

                                    tuple_rule = tuple(list_rule)
                                    result_rule[i].append(tuple_rule)
                                    tuple_index = tuple(list_index)  # see index
                                    result_index[i].append(tuple_index)  # see index

                                elif str(list_tag_2d[i][count_p_r + 1]) == 'กระทำ8' and count_p_r + 1 != len(
                                        list_tag_2d[i]) - 1:
                                    if list_tag_2d[i][count_p_r + 1].name_action == 'แจ้งความ':
                                        # print(list_tag_2d[i][count_p_r+1])
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
            return result_rule
        else:
            return 'Empty'


# 7.→ คน (เสียหาย)* + กระทำ + คน (เจ้าหน้าที่)
def rule7(list_tag_2d, need_count='N'):
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
                    if str(list_tag_2d[i][count_l]) != 'คน' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'คน':
                        if list_tag_2d[i][j - 1].status != 'คนร้าย':
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
                    if j != len(list_tag_2d[i]) - 1:
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            if list_tag_2d[i][j + 1].status != 'คนร้าย' and list_tag_2d[i][j + 1].status != 'คนเสียหาย':
                                list_tag_2d[i][j + 1].status = 'เจ้าหน้าที่'
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
            return result_rule
        else:
            return 'Empty'

   
# 8.→ คน (ร้าย) + กระทำ + คน (เจ้าหน้าที่)
def rule8(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index

    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            # if str(list_tag_2d[i][j]) == 'กระทำ6' and j != 0 and j != len(list_tag_2d[i]): #กระทำ
            if str(list_tag_2d[i][j]) == 'กระทำรอง1' and j != 0 and j != len(list_tag_2d[i]):  # กระทำ
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'คน':
                    if list_tag_2d[i][j - 1].status != 'คนเสียหาย':
                        list_tag_2d[i][j - 1].status = 'คนร้าย'
                        list_rule.append(list_tag_2d[i][j - 1])
                        list_index.append(j - 1)
                        list_rule.append(list_tag_2d[i][j])
                        list_index.append(j)

                        count_r = j
                        check_r = False
                        count_pr = 0
                        # print('r',i,j,count_r,str(list_tag_2d[i][count_r+1]))
                        if j != len(list_tag_2d[i]) - 1:
                            if str(list_tag_2d[i][j + 1]) == 'คน':
                                if (list_tag_2d[i][j + 1].status != 'คนเสียหาย' and list_tag_2d[i][j + 1].status != 'คนร้าย'):
                                    list_tag_2d[i][j + 1].status = 'เจ้าหน้าที่'
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

    # print(status_rule)
    # print(result_index)

    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 9.→ คน (ร้าย) + คำ (บ่งบอกว่าถูกกระทำ) +- เจ้าหน้าที่ + กระทำ *** เหมือน3.
def rule9(list_tag_2d, need_count='N'):
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

                    if str(list_tag_2d[i][j - 1]) == 'คน' and j - 1 != 0:
                        if list_tag_2d[i][j - 1].status != 'คนเสียหาย' and list_tag_2d[i][j - 1].status != 'คนร้าย':
                            # print(list_tag_2d[i][j-1])
                            if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                                # print(list_tag_2d[i][j-2])
                                if str(list_tag_2d[i][j - 3]) == 'คน':
                                    if list_tag_2d[i][j - 3].status != 'คนเสียหาย':
                                        # print(list_tag_2d[i][j-3])
                                        # print(list_tag_2d[i][j-2])
                                        # print(list_tag_2d[i][j-1])
                                        # print(list_tag_2d[i][j])

                                        list_tag_2d[i][j - 3].status = 'คนร้าย'
                                        list_rule.append(list_tag_2d[i][j - 3])
                                        list_rule.append(list_tag_2d[i][j - 2])
                                        list_tag_2d[i][j - 1].status = 'เจ้าหน้าที่'
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
                        if str(list_tag_2d[i][j - 2]) == 'คน':
                            if list_tag_2d[i][j - 2].status != 'คนเสียหาย':
                                # print(list_tag_2d[i][j-2])
                                # print(list_tag_2d[i][j-1])
                                # print(list_tag_2d[i][j])
                                list_tag_2d[i][j - 2].status = 'คนร้าย'
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

                    if str(list_tag_2d[i][j - 1]) == 'คน' and j - 1 != 0:
                        if list_tag_2d[i][j - 1].status != 'คนเสียหาย' and list_tag_2d[i][j - 1].status != 'คนร้าย':
                            # print(list_tag_2d[i][j-1])
                            if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก' and j - 2 != 0:
                                # print(list_tag_2d[i][j-2])
                                if str(list_tag_2d[i][j - 3]) == 'คน':
                                    if list_tag_2d[i][j - 3].status != 'คนเสียหาย':
                                        # print(list_tag_2d[i][j-3])
                                        # print(list_tag_2d[i][j-2])
                                        # print(list_tag_2d[i][j-1])
                                        # print(list_tag_2d[i][j])
                                        list_tag_2d[i][j - 3].status = 'เจ้าหน้าที่'
                                        list_rule.append(list_tag_2d[i][j - 3])
                                        list_rule.append(list_tag_2d[i][j - 2])
                                        list_tag_2d[i][j - 1].status = 'คนร้าย'
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
                        if (str(list_tag_2d[i][j - 2]) == 'คน'):
                            if list_tag_2d[i][j - 2].status != 'คนเสียหาย':
                                # print(list_tag_2d[i][j-2])
                                # print(list_tag_2d[i][j-1])
                                # print(list_tag_2d[i][j])
                                list_tag_2d[i][j - 2].status = 'คนร้าย'
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
            return result_rule
        else:
            return 'Empty'


# 10.→ คน (เสียหาย) + กระทำ*
def rule10(list_tag_2d, need_count='N'):
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
                    if list_tag_2d[i][j - 1].status != 'คนร้าย':
                        # print(list_tag_2d[i][j-1])
                        # print(list_tag_2d[i][j])
                        list_tag_2d[i][j - 1].status = 'คนเสียหาย'
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

                        # count_ar = count_r - 1
                        # if str(list_tag_2d[i][count_ar + 1]) == 'คำบ่งบอก3':
                        #     # print(list_tag_2d[i][count_ar+1])
                        #     list_rule.append(list_tag_2d[i][count_ar + 1])
                        #     list_index.append(count_ar + 1)  # see index

                        #     if count_ar + 2 <= len(list_tag_2d[i]) - 1:
                        #         if (str(list_tag_2d[i][count_ar + 2]) == 'คน' or str(
                        #                 list_tag_2d[i][count_ar + 2]) == 'คนร้าย'):
                        #             # print(list_tag_2d[i][count_ar+2])
                        #             list_tag_2d[i][count_ar + 2].status = 'คนร้าย'
                        #             list_rule.append(list_tag_2d[i][count_ar + 2])
                        #             list_index.append(count_ar + 2)  # see index

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
            return result_rule
        else:
            return 'Empty'


# 11.→ คน (ร้าย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 11.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (ร้าย)
def rule11(list_tag_2d, need_count='N'):
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
                    # คนร้าย | ผู้ร้าย | ผู้ต้องหา | ผู้ก่อเหตุ
                    if (list_tag_2d[i][j - 1].firstname == 'คนร้าย' or list_tag_2d[i][j - 1].firstname == 'ผู้ร้าย'
                        or list_tag_2d[i][j - 1].firstname == 'ผู้ต้องหา' or list_tag_2d[i][j - 1].firstname == 'ผู้ก่อเหตุ'):
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            if list_tag_2d[i][j + 1].status != 'คนเสียหาย':
                                # print(str(list_tag_2d[i][j-1]))
                                # print(str(list_tag_2d[i][j]))
                                # print(str(list_tag_2d[i][j+1]))
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_index.append(j - 1)  # see index
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j)  # see index

                                list_tag_2d[i][j + 1].status = 'คนร้าย'
                                list_rule.append(list_tag_2d[i][j + 1])
                                list_index.append(j + 1)  # see index

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

                elif (str(list_tag_2d[i][j - 1]) == 'คน'):
                    if list_tag_2d[i][j - 1].status != 'คนเสียหาย':
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            # คนร้าย | ผู้ร้าย | ผู้ต้องหา | ผู้ก่อเหตุ
                            if (list_tag_2d[i][j + 1].firstname == 'คนร้าย' or list_tag_2d[i][j + 1].firstname == 'ผู้ร้าย'
                                or list_tag_2d[i][j + 1].firstname == 'ผู้ต้องหา' or list_tag_2d[i][j + 1].firstname == 'ผู้ก่อเหตุ'):
                                # print(str(list_tag_2d[i][j-1]))
                                # print(str(list_tag_2d[i][j]))
                                # print(str(list_tag_2d[i][j+1]))
                                list_tag_2d[i][j - 1].status = 'คนร้าย'
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
            return result_rule
        else:
            return 'Empty'


# 12.→ คน (เสียหาย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 12.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (เสียหาย)
def rule12(list_tag_2d, need_count='N'):
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
                    # ผู้เสียหาย | ผู้ตาย | ผู้เสียชีวิต
                    if (list_tag_2d[i][j - 1].firstname == 'ผู้เสียหาย' or list_tag_2d[i][j - 1].firstname == 'ผู้ตาย'
                        or list_tag_2d[i][j - 1].firstname == 'ผู้เสียชีวิต'):
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

                elif (str(list_tag_2d[i][j - 1]) == 'คน'):
                    if list_tag_2d[i][j - 1].status != 'คนร้าย':
                        if str(list_tag_2d[i][j + 1]) == 'คน':
                            if (list_tag_2d[i][j + 1].firstname == 'ผู้เสียหาย' or list_tag_2d[i][j + 1].firstname == 'ผู้ตาย'
                                or list_tag_2d[i][j + 1].firstname == 'ผู้เสียชีวิต'):
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
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# ---------------- สถานที่ ----------------
# 13.→  กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
def rule13(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):

            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                list_rule.append(list_tag_2d[i][j])
                list_index.append(j)  # see index
                count_l = j
                check_l = False
                check_a_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'กระทำ1' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index
                        check_a_l = True

                if check_a_l == True:
                    tuple_rule = tuple(list_rule)
                    result_rule[i].append(tuple_rule)
                    tuple_index = tuple(list_index)  # see index
                    result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 14.→ คน (ร้าย)* + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
def rule14(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):

            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                list_rule.append(list_tag_2d[i][j])
                list_index.append(j)  # see index
                count_l = j
                check_l = False
                check_a_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'กระทำ1' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index
                        check_a_l = True

                if check_a_l == True:
                    count_p_l = count_l + 1
                    check_l = False
                    check_p_l = False

                    while (check_l != True):
                        count_p_l -= 1
                        # print(count_p_l,str(list_tag_2d[i][count_p_l]))

                        if ((str(list_tag_2d[i][count_p_l]) != 'คน') or count_p_l == -1):
                            check_l = True
                        elif (str(list_tag_2d[i][count_p_l]) == 'คน'):
                            if list_tag_2d[i][count_p_l].status != 'คนเสียหาย':
                                check_p_l = True
                                list_tag_2d[i][count_p_l].status = 'คนร้าย'
                                # คน (ร้าย)*
                                list_rule.insert(0, list_tag_2d[i][count_p_l])
                                list_index.insert(0, count_p_l)  # see index
                                check_p_l = True

                    if check_p_l == True:
                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 15.→ กระทำ (ผิด) + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)
def rule15(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก4' and j - 1 >= 0:
                    if str(list_tag_2d[i][j - 2]) == 'กระทำ1' and j - 2 >= 0:
                        list_rule.append(list_tag_2d[i][j - 2])
                        list_index.append(j - 2)  # see index
                        list_rule.append(list_tag_2d[i][j - 1])
                        list_index.append(j - 1)  # see index
                        list_rule.append(list_tag_2d[i][j])
                        list_index.append(j)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 16.→ กระทำ (ผิด) + คน + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)
def rule16(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                if str(list_tag_2d[i][j - 1]) == 'คำบ่งบอก4' and j - 1 >= 0:
                    if str(list_tag_2d[i][j - 2]) == 'คน' and j - 2 >= 0:
                        if str(list_tag_2d[i][j - 3]) == 'กระทำ1' and j - 3 >= 0:
                            list_rule.append(list_tag_2d[i][j - 3])
                            list_index.append(j - 3)  # see index
                            list_rule.append(list_tag_2d[i][j - 2])
                            list_index.append(j - 2)  # see index
                            list_rule.append(list_tag_2d[i][j - 1])
                            list_index.append(j - 1)  # see index
                            list_rule.append(list_tag_2d[i][j])
                            list_index.append(j)  # see index

                            tuple_rule = tuple(list_rule)
                            result_rule[i].append(tuple_rule)
                            tuple_index = tuple(list_index)  # see index
                            result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# 17.→ คน + คำกริยา + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) +- กระทำ (ผิด) + สถานที่ (เกิดเหตุ)
def rule17(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index

                if str(list_tag_2d[i][j - 1]) == 'กระทำ1' and j - 1 >= 0:
                    if str(list_tag_2d[i][j - 2]) == 'คำบ่งบอก4' and j - 2 >= 0:
                        if str(list_tag_2d[i][j - 3]) == 'คำบ่งบอก' and j - 3 >= 0:
                            if str(list_tag_2d[i][j - 4]) == 'คน' and j - 4 >= 0:
                                list_rule.append(list_tag_2d[i][j - 4])
                                list_index.append(j - 4)  # see index
                                list_rule.append(list_tag_2d[i][j - 3])
                                list_index.append(j - 3)  # see index
                                list_rule.append(list_tag_2d[i][j - 2])
                                list_index.append(j - 2)  # see index
                                list_rule.append(list_tag_2d[i][j - 1])
                                list_index.append(j - 1)  # see index
                                list_rule.append(list_tag_2d[i][j])
                                list_index.append(j)  # see index

                                tuple_rule = tuple(list_rule)
                                result_rule[i].append(tuple_rule)
                                tuple_index = tuple(list_index)  # see index
                                result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'


# ---------------- เวลา ----------------
# 18.→ เวลา + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
def rule18(list_tag_2d, need_count='N'):
    result_rule = []
    result_index = []  # see index
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        result_index.append([])  # see index
        for j in range(len(list_tag_2d[i])):

            if str(list_tag_2d[i][j]) == 'สถานที่' and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_index = []  # see index
                tuple_index = ()  # see index
                list_rule.append(list_tag_2d[i][j])
                list_index.append(j)  # see index
                count_l = j
                check_l = False
                check_a_l = False
                while (check_l != True):
                    count_l -= 1
                    if str(list_tag_2d[i][count_l]) != 'กระทำ1' or count_l == -1:
                        check_l = True
                    elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
                        list_rule.insert(0, list_tag_2d[i][count_l])
                        list_index.insert(0, count_l)  # see index
                        check_a_l = True

                if check_a_l == True:
                    count_l_dt = count_l
                    if str(list_tag_2d[i][count_l_dt]) == 'เวลา' and count_l_dt >= 0:

                        list_rule.insert(0, list_tag_2d[i][count_l_dt])
                        list_index.insert(0, count_l_dt)  # see index

                        if str(list_tag_2d[i][count_l_dt - 1]) == 'วัน' and count_l_dt - 1 >= 0:
                            list_rule.insert(0, list_tag_2d[i][count_l_dt - 1])
                            list_index.insert(0, count_l_dt - 1)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

                    elif str(list_tag_2d[i][count_l_dt]) == 'วัน' and count_l_dt >= 0:
                        list_rule.insert(0, list_tag_2d[i][count_l_dt])
                        list_index.insert(0, count_l_dt)  # see index

                        if str(list_tag_2d[i][count_l_dt - 1]) == 'เวลา' and count_l_dt - 1 >= 0:
                            list_rule.insert(0, list_tag_2d[i][count_l_dt - 1])
                            list_index.insert(0, count_l_dt - 1)  # see index

                        tuple_rule = tuple(list_rule)
                        result_rule[i].append(tuple_rule)
                        tuple_index = tuple(list_index)  # see index
                        result_index[i].append(tuple_index)  # see index

    status_rule = False
    for i in range(len(result_rule)):
        if not result_rule[i]:
            status_rule = False
        else:
            status_rule = True
            break

    # print(result_index)
    if need_count == 'Y':
        return result_index
    else:
        if status_rule == True:
            return result_rule
        else:
            return 'Empty'
