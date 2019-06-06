import ngram
import class_object as obj
import tag_object as tag
import write_file as wr
from pprint import pprint


# 1.→  คน (ร้าย) + กระทำ (ผิด)*
def rule1(list_tag_2d):
    result_rule = []
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_rule.append(list_tag_2d[i][j])
                # print('AM',i,j,list_tag_2d[i][j])
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนร้าย')
                                    and list_tag_2d[i][count_l].status != 'คนเสียหาย'):
                                check_p_l = True
                                list_tag_2d[i][count_l].status = 'คนร้าย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL',i,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1':  # or str(list_tag_2d[i][count_l]) == 'คำบ่งบอก':
                            check_l = True

                count_r = j
                check_r = False
                while (check_r != True):
                    if count_r == len(list_tag_2d[i]) - 1:
                        check_r = True
                    else:
                        count_r += 1
                        if str(list_tag_2d[i][count_r]) == 'กระทำ1':
                            list_rule.append(list_tag_2d[i][count_r])
                            # print('AR',i,count_r,list_tag_2d[i][count_r])
                        elif str(list_tag_2d[i][count_r]) != 'กระทำ1':
                            check_r = True

                if check_p_l == True:
                    # print('-------------------')
                    tuple_rule = tuple(list_rule)
                    result_rule[i].append(tuple_rule)

            elif str(list_tag_2d[i][j]) == 'กระทำ2' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_rule.append(list_tag_2d[i][j])
                # print('AM',i,j,list_tag_2d[i][j])
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนร้าย')
                                    and list_tag_2d[i][count_l].status != 'คนเสียหาย'):
                                check_p_l = True
                                list_tag_2d[i][count_l].status = 'คนร้าย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL',i,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ2':
                            check_l = True

                count_r = j
                check_r = False
                while (check_r != True):
                    if count_r == len(list_tag_2d[i]) - 1:
                        check_r = True
                    else:
                        count_r += 1
                        if str(list_tag_2d[i][count_r]) == 'กระทำ1':
                            list_rule.append(list_tag_2d[i][count_r])
                            # print('AR',i,count_r,list_tag_2d[i][count_r])
                        elif str(list_tag_2d[i][count_r]) != 'กระทำ1':
                            check_r = True

                if check_p_l == True:
                    # print('-------------------')
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
def rule2(list_tag_2d):
    result_rule = []
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_rule.append(list_tag_2d[i][j])
                # print('AM',i,j,list_tag_2d[i][j])
                count_l = j
                check_l = False
                check_p_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนร้าย')
                                    and list_tag_2d[i][count_l].status != 'คนเสียหาย'):
                                check_p_l = True
                                list_tag_2d[i][count_l].status = 'คนร้าย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL',i,count_l,list_tag_2d[i][count_l])
                        elif (str(list_tag_2d[i][count_l]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'คำบ่งบอก' ):
                            #   or str(list_tag_2d[i][count_l]) == 'กระทำ3'):
                            check_l = True

                count_r = j
                check_r = False
                while (check_r != True):
                    if count_r == len(list_tag_2d[i]) - 1:
                        check_r = True
                    else:
                        count_r += 1
                        if str(list_tag_2d[i][count_r]) == 'กระทำ1':
                            list_rule.append(list_tag_2d[i][count_r])
                            # print('AR',i,count_r,list_tag_2d[i][count_r])
                        elif str(list_tag_2d[i][count_r]) != 'กระทำ1':
                            check_r = True

                count_r = count_r - 1
                check_p_r = False
                check_r = False
                while (check_r != True):
                    if count_r == len(list_tag_2d[i]) - 1:
                        check_r = True
                    else:
                        count_r += 1
                        if str(list_tag_2d[i][count_r]) == 'คน':
                            if ((list_tag_2d[i][count_r].status == 'คน' or list_tag_2d[i][count_r].status == 'คนเสียหาย')
                                    and list_tag_2d[i][count_r].status != 'คนร้าย'):
                                check_p_r = True
                                list_tag_2d[i][count_r].status = 'คนเสียหาย'
                                list_rule.append(list_tag_2d[i][count_r])
                                # print('PR',i,count_r,list_tag_2d[i][count_r])
                        elif str(list_tag_2d[i][count_r]) == 'กระทำ1':
                            check_l = True

                if check_p_l == True and check_p_r == True:
                    # print('-------------------')
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


# 3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)
def rule3(list_tag_2d):
    result_rule = []
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_rule.append(list_tag_2d[i][j])
                # print('AM',i+1,j,list_tag_2d[i][j])
                count_l = j
                check_l = False
                check_ad_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คำบ่งบอก':
                            check_ad_l = True
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            # print('ADL',i+1,count_l,list_tag_2d[i][count_l])
                            break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
                            check_l = True

                count_l = count_l + 1
                check_l = False
                check_p_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนเสียหาย')
                                    and list_tag_2d[i][count_l].status != 'คนร้าย'):
                                check_p_l = True
                                list_tag_2d[i][count_l].status = 'คนเสียหาย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL',i+1,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'กระทำ3':
                            check_l = True

                count_r = j
                check_p_r = False
                check_r = False
                while (check_r != True):

                    if count_r == len(list_tag_2d[i]) - 1:
                        check_r = True
                    else:
                        count_r += 1
                        # print('PR',i+1,count_r,list_tag_2d[i][count_r])
                        if str(list_tag_2d[i][count_r]) == 'คน':
                            # print('PRC',i+1,count_r,list_tag_2d[i][count_r].status)
                            if ((list_tag_2d[i][count_r].status == 'คน' or list_tag_2d[i][count_r].status == 'คนร้าย')
                                    and list_tag_2d[i][count_r].status != 'คนเสียหาย'):
                                check_p_r = True
                                list_tag_2d[i][count_r].status = 'คนร้าย'
                                list_rule.append(list_tag_2d[i][count_r])
                                # print('PR',i+1,count_r,list_tag_2d[i][count_r])
                                break
                        elif str(list_tag_2d[i][count_r]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'กระทำ3':
                            check_l = True

                # print(check_ad_l,check_p_l,check_p_r)
                if check_ad_l == True and check_p_l == True and (check_p_r == True or check_p_r == False):
                    # print('-------------------')
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


# 4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)
def rule4(list_tag_2d):
    result_rule = []
    for i in range(len(list_tag_2d)):
        result_rule.append([])
        for j in range(len(list_tag_2d[i])):
            if str(list_tag_2d[i][j]) == 'กระทำ1' and j != 0 and j != len(list_tag_2d[i]):
                list_rule = []
                tuple_rule = ()
                list_rule.append(list_tag_2d[i][j])
                # print('AM',i+1,j,list_tag_2d[i][j])
                count_l = j
                check_l = False
                check_pv_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][count_l].status == 'คนร้าย')
                                    and list_tag_2d[i][count_l].status != 'คนเสียหาย'):
                                check_pv_l = True
                                list_tag_2d[i][count_l].status = 'คนร้าย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL1',i+1,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'คำบ่งบอก':
                            check_l = True

                # print('AAA',count_l,list_tag_2d[i][count_l])
                # count_l = count_l+1
                check_l = False
                check_ad_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        if str(list_tag_2d[i][count_l]) == 'คำบ่งบอก':
                            check_ad_l = True
                            list_rule.insert(0, list_tag_2d[i][count_l])
                            # print('ADL',i+1,count_l,list_tag_2d[i][count_l])
                            break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
                            check_l = True

                # print('AAA',count_l,list_tag_2d[i][count_l])
                check_l = False
                check_ps_l = False
                while (check_l != True):
                    if count_l == 0:
                        check_l = True
                    else:
                        count_l -= 1
                        # print('PL0',i+1,count_l,list_tag_2d[i][count_l])
                        if str(list_tag_2d[i][count_l]) == 'คน':
                            # print('PL0',i+1,count_l,list_tag_2d[i][count_l].status)
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][
                                count_l].status == 'คนเสียหาย')
                                    and list_tag_2d[i][count_l].status != 'คนร้าย'):
                                check_ps_l = True
                                list_tag_2d[i][count_l].status = 'คนเสียหาย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL0',i+1,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'คำบ่งบอก':
                            check_l = True

                # print(check_pv_l,check_ad_l,check_ps_l)
                if check_pv_l == True and check_ad_l == True and check_ps_l == True:
                    # print('-------------------')
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
