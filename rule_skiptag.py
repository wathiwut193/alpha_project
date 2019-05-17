import ngram
import class_object as obj
import tag_object as tag
import write_file as wr
from pprint import pprint


def cause_rule_results(str_text, n):
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
    """
    wr.export_obj(list_tag_2d,str(n))
    """

    count = 0
    print('--------------- Rule Result skiptag ---------------')
    # 1.→  คน (ร้าย) + กระทำ (ผิด)*
    # result1 = rule1(list_tag_2d)
    result1 = rule1(list_tag_1)
    print_rule_result(result1, 1)
    count += count_result(result1)
    print('------------------------------')
    print('Result Count R1 : ', count)
    wr.export_text(str_text, str(n))
    wr.export_rule(result1, 1, str(n))
    """
    # 2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*
    result2 = rule2(list_tag_2)
    print_rule_result(result2,2)
    count += count_result(result2)
    # wr.export_rule(result2,2,str(n))

    # 3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)
    result3 = rule3(list_tag_3)
    print_rule_result(result3,3)
    count += count_result(result3)
    # wr.export_rule(result3,3,str(n))

    # 4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)
    result4 = rule4(list_tag_4)
    print_rule_result(result4,4)
    count += count_result(result4)
    # wr.export_rule(result4,4,str(n))

    print('------------------------------')
    print('Result Count : ',count)
    """
    """
    # 5.→ คน (เจ้าหน้าที่)* + กระทำ3* +- คน (ร้าย)
    result5 = rule5(list_tag_2d)
    result(result5,5)
    wr.export_rule(result5,5,str(n))

    # 6.→ คน (เจ้าหน้าที่) + กระทำ + คน (เสียหาย)* + กระทำ 
    result6 = rule6(list_tag_2d)
    result(result6,6)
    wr.export_rule(result6,6,str(n))

    # 7.→ คน (เสียหาย)* + กระทำ + คน (เจ้าหน้าที่)
    result7 = rule7(list_tag_2d)
    result(result7,7)
    wr.export_rule(result7,7,str(n))

    # 9.→ คน (ร้าย) + คำ (บ่งบอกว่าถูกกระทำ) +- เจ้าหน้าที่ + กระทำ *** เหมือน3.
    result9 = rule9(list_tag_2d)
    result(result9,9)
    wr.export_rule(result9,9,str(n))

    # 11.→ คน (ร้าย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 11.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (ร้าย)
    result11 = rule11(list_tag_2d)
    result(result11,11)
    wr.export_rule(result11,11,str(n))

    # 12.→ คน (เสียหาย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 12.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (เสียหาย)
    result12 = rule12(list_tag_2d)
    result(result12,12)
    wr.export_rule(result12,12,str(n))

    # when rule 1,2,3 and 4 result = Empty 
    # tag secondary action 1
    # check result by rule 8
    list_tag_2d_1 = list_tag_2d
    if result1 == 'Empty' and result2 == 'Empty' and result3 == 'Empty' and result4 == 'Empty':
        str_text = tag.tag_secondary_action(str_text,1)
        #print(str_text)
        list_text2d = split_column(str_text)
        list_tag_2d = tag_to_obj(list_text2d)
        #print(list_tag_2d)
        # 8.→ คน (ร้าย) + กระทำ + คน (เจ้าหน้าที่)
        result8 = rule8(list_tag_2d)
        result(result8,8)
        wr.export_rule(result8,8,str(n))

    # 13.→  กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
    result13 = rule13(list_tag_2d_1)
    result(result13,13)
    wr.export_rule(result13,13,str(n))

    # 14.→ คน (ร้าย)* + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
    result14 = rule14(list_tag_2d_1)
    result(result14,14)
    wr.export_rule(result14,14,str(n))

    # 15.→ กระทำ (ผิด) + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)
    result15 = rule15(list_tag_2d_1)
    result(result15,15)
    wr.export_rule(result15,15,str(n))

    # 16.→ กระทำ (ผิด) + คน + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)
    result16 = rule16(list_tag_2d_1)
    result(result16,16)
    wr.export_rule(result16,16,str(n))

    # 17.→ คน + คำกริยา + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) +- กระทำ (ผิด) + สถานที่ (เกิดเหตุ)
    result17 = rule17(list_tag_2d_1)
    result(result17,17)
    wr.export_rule(result17,17,str(n))

    # 18.→ เวลา + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)
    result18 = rule18(list_tag_2d_1)
    result(result18,18)
    wr.export_rule(result18,18,str(n))

    #print('\n')
    #print_in_obj(str_text)
    #count_result(str_text)
    """


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
                        elif (str(list_tag_2d[i][count_l]) == 'กระทำ1' or str(list_tag_2d[i][count_l]) == 'คำบ่งบอก'
                              or str(list_tag_2d[i][count_l]) == 'กระทำ3'):
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
                            if ((list_tag_2d[i][count_r].status == 'คน' or list_tag_2d[i][count_r].status == 'คนร้าย')
                                    and list_tag_2d[i][count_r].status != 'คนเสียหาย'):
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
                            if ((list_tag_2d[i][count_l].status == 'คน' or list_tag_2d[i][
                                count_l].status == 'คนเสียหาย')
                                    and list_tag_2d[i][count_l].status != 'คนร้าย'):
                                check_p_l = True
                                list_tag_2d[i][count_l].status = 'คนเสียหาย'
                                list_rule.insert(0, list_tag_2d[i][count_l])
                                # print('PL',i+1,count_l,list_tag_2d[i][count_l])
                                break
                        elif str(list_tag_2d[i][count_l]) == 'กระทำ1':
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
                        elif str(list_tag_2d[i][count_r]) == 'กระทำ1':
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
