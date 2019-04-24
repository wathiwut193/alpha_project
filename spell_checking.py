import regex
import time
import json


def spell_checker(spell):
    spell = province_fail(spell)
    spell = province_amphoe_fail(spell)
    spell = province_tambon_fail(spell)
    spell = amphoe_tambon_fail(spell)
    spell = province_amphoe_fail_tambon_fail(spell)
    # read_text = tag_......
    return spell


def get_json_data():
    with open('dictionary/json_dict/raw_database.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def province_fail(pro_matches, Data):
    province_set = set()
    province_set.add('กรุงเทพฯ')
    for i in pro_matches:
        for k in Data:
            for att, val in k.items():
                if att == 'province':
                    province_set.add(val)
    province_list = list(province_set)
    res = find_result(province_list, pro_matches)
    return res


def province_amphoe_fail(pro_amp_matches, Data):
    amphoe_set = set()
    for i in range(len(pro_amp_matches)):
        for j in range(len(pro_amp_matches[i])):
            if pro_amp_matches and j != len(pro_amp_matches[i]) - 1:
                # print(pro_amp_matches[i][j])
                for k in Data:
                    for att, val in k.items():
                        if att == 'province' and val == pro_amp_matches[i][j]:
                            # print(val)
                            for att, val in k.items():
                                if att == 'amphoe':
                                    amphoe_set.add(val)

    # print(amphoe_set)
    amphoe_list = list(amphoe_set)
    res = find_result(amphoe_list, pro_amp_matches[0][1])
    return res


def province_tambon_fail(pro_tam_matches, Data):
    tambon_set = set()

    for i in range(len(pro_tam_matches)):
        for j in range(len(pro_tam_matches[i])):
            if pro_tam_matches and j != len(pro_tam_matches[i]) - 1:
                for k in Data:
                    for att, val in k.items():
                        if att == 'province' and val == pro_tam_matches[i][j]:
                            for att, val in k.items():
                                if att == 'district':
                                    tambon_set.add(val)

    tambon_list = list(tambon_set)
    res = find_result(tambon_list, pro_tam_matches[0][1])
    return res


def amphoe_tambon_fail(amp_tam_matches, Data):
    tambon_set = set()

    for i in range(len(amp_tam_matches)):
        for j in range(len(amp_tam_matches[i])):
            if amp_tam_matches and j != len(amp_tam_matches[i]) - 1:
                for k in Data:
                    for att, val in k.items():
                        if att == 'amphoe' and val == amp_tam_matches[i][j]:
                            for att, val in k.items():
                                if att == 'district':
                                    tambon_set.add(val)

    tambon_list = list(tambon_set)
    res = find_result(tambon_list, amp_tam_matches[0][1])
    return res


def province_amphoe_fail_tambon_fail(pro_amp_tam_matches, Data):
    amphoe_set = set()
    tambon_set = set()
    for i in range(len(pro_amp_tam_matches)):
        for j in range(len(pro_amp_tam_matches[i])):
            if pro_amp_tam_matches and j != len(pro_amp_tam_matches[i]) - 1:
                for k in Data:
                    for att, val in k.items():
                        if att == 'province' and val == pro_amp_tam_matches[i][0]:
                            for att, val in k.items():
                                if att == 'amphoe':
                                    amphoe_set.add(val)

                for k in Data:
                    for att, val in k.items():
                        if att == 'province' and val == pro_amp_tam_matches[i][0]:
                            for att, val in k.items():
                                if att == 'district':
                                    tambon_set.add(val)

    # print(amphoe_set)
    amphoe_list = list(amphoe_set)
    res1 = find_result(amphoe_list, pro_amp_tam_matches[i][1])
    # print(district_set)
    tambon_list = list(tambon_set)
    res2 = find_result(tambon_list, pro_amp_tam_matches[i][2])
    return res1, res2


def dict_action():
    with open('corpus/Action.txt', 'r', encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict


def dict_hospital():
    with open('corpus/hospital.txt', 'r', encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict


def dict_country():
    with open('corpus/country.txt', 'r', encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict


def dict_store():
    with open('corpus/store.txt', 'r', encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict


def dict_university():
    with open('corpus/university.txt', 'r', encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict


def Autocorrection(x):
    Data = get_json_data()

    action_fail = r"<กระทำ_ผิด>([^<]*)</กระทำ_ผิด>"
    hospital_fail = r"<โรงพยาบาล_ผิด>([^<]*)</โรงพยาบาล_ผิด>"
    country_fail = r"<ประเทศ_ผิด>([^<]*)</ประเทศ_ผิด>"
    store_fail = r"<ห้าง_ผิด>([^<]*)</ห้าง_ผิด>"
    university_fail = r"<มหาวิทยาลัย_ผิด>([^<]*)</มหาวิทยาลัย_ผิด>"
    pro = r"<จังหวัด_ผิด>([^<]*)</จังหวัด_ผิด>"
    pro_amp = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<อำเภอ_ผิด>([^<]*)</อำเภอ_ผิด>(?!<ตำบล_ผิด>)"
    pro_tam = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"
    amp_tam = r"<อำเภอ>([^<]*)</อำเภอ>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"
    pro_amp_tam = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<อำเภอ_ผิด>([^<]*)</อำเภอ_ผิด>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"

    action_fail_matches = regex.findall(action_fail, x)
    hospital_fail_matches = regex.findall(hospital_fail, x)
    country_fail_matches = regex.findall(country_fail, x)
    store_fail_matches = regex.findall(store_fail, x)
    university_fail_matches = regex.findall(university_fail, x)
    pro_matches = regex.findall(pro, x)
    pro_amp_matches = regex.findall(pro_amp, x)
    pro_tam_matches = regex.findall(pro_tam, x)
    amp_tam_matches = regex.findall(amp_tam, x)
    pro_amp_tam_matches = regex.findall(pro_amp_tam, x)

    if pro_amp_tam_matches:
        # province_amphoe_fail_tambon_fail(pro_amp_tam_matches,Data)
        for i in pro_amp_tam_matches:
            correct_x = regex.sub(r'<จังหวัด>' + i[0] + '</จังหวัด>', r'<จังหวัด>' + i[0] + '</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<อำเภอ_ผิด>' + i[1] + '</อำเภอ_ผิด>',
                                  r'<อำเภอ>' + province_amphoe_fail_tambon_fail(pro_amp_tam_matches, Data)[
                                      0] + '</อำเภอ>', x)
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>' + i[2] + '</ตำบล_ผิด>',
                                  r'<ตำบล>' + province_amphoe_fail_tambon_fail(pro_amp_tam_matches, Data)[
                                      1] + '</ตำบล>', x)
            x = correct_x

    if pro_amp_matches:
        # province_amphoe_fail(pro_amp_matches,Data)
        for i in pro_amp_matches:
            correct_x = regex.sub(r'<จังหวัด>' + i[0] + '</จังหวัด>', r'<จังหวัด>' + i[0] + '</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<อำเภอ_ผิด>' + i[1] + '</อำเภอ_ผิด>',
                                  r'<อำเภอ>' + province_amphoe_fail(pro_amp_matches, Data) + '</อำเภอ>', x)
            x = correct_x

    if pro_tam_matches:
        # province_district_fail(pro_dis_matches,Data)
        for i in pro_tam_matches:
            correct_x = regex.sub(r'<จังหวัด>' + i[0] + '</จังหวัด>', r'<จังหวัด>' + i[0] + '</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>' + i[1] + '</ตำบล_ผิด>',
                                  r'<ตำบล>' + province_tambon_fail(pro_tam_matches, Data) + '</ตำบล>', x)
            x = correct_x
    if amp_tam_matches:
        # amphoe_district_fail(amp_dis_matches,Data)
        for i in amp_tam_matches:
            correct_x = regex.sub(r'<อำเภอ>' + i[0] + '</อำเภอ>', r'<อำเภอ>' + i[0] + '</อำเภอ>', x)
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>' + i[1] + '</ตำบล_ผิด>',
                                  r'<ตำบล>' + amphoe_tambon_fail(amp_tam_matches, Data) + '</ตำบล>', x)
            x = correct_x
    if pro_matches:
        # province_fail(pro_matches,Data)

        for i in pro_matches:
            correct_x = regex.sub(r'<จังหวัด_ผิด>' + i + '</จังหวัด_ผิด>',
                                  r'<จังหวัด>' + province_fail(i, Data) + '</จังหวัด>', x)
            x = correct_x

    if action_fail_matches:
        for i in action_fail_matches:
            res = find_result(dict_action(), i)
            correct_x = regex.sub(r'<กระทำ_ผิด>' + i + '</กระทำ_ผิด>', '<กระทำ>' + res + '</กระทำ>', x)
            x = correct_x

    if hospital_fail_matches:
        for i in hospital_fail_matches:
            res = find_result(dict_hospital(), i)
            correct_x = regex.sub(r'<โรงพยาบาล_ผิด>' + i + '</โรงพยาบาล_ผิด>', '<โรงพยาบาล>' + res + '</โรงพยาบาล>', x)
            x = correct_x

    if country_fail_matches:
        for i in country_fail_matches:
            res = find_result(dict_country(), i)
            correct_x = regex.sub(r'<ประเทศ_ผิด>' + i + '</ประเทศ_ผิด>', '<ประเทศ>' + res + '</ประเทศ>', x)
            x = correct_x

    if store_fail_matches:
        for i in store_fail_matches:
            res = find_result(dict_store(), i)
            correct_x = regex.sub(r'<ห้าง_ผิด>' + i + '</ห้าง_ผิด>', '<ห้าง>' + res + '</ห้าง>', x)
            x = correct_x

    if university_fail_matches:
        for i in university_fail_matches:
            res = find_result(dict_university(), i)
            correct_x = regex.sub(r'<มหาวิทยาลัย_ผิด>' + i + '</มหาวิทยาลัย_ผิด>',
                                  '<มหาวิทยาลัย>' + res + '</มหาวิทยาลัย>', x)
            x = correct_x

    return x
