import regex
import time
import json

# -*- coding: utf-8 -*-
def get_json_data():
    """

    :return:
    """
    with open('dictionary/json_dict/raw_database.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def province_fail(pro_matches,Data):
    province_set = set()
    province_set.add('กรุงเทพฯ')
    for i in pro_matches:
        for k in Data:
            for att,val in k.items():
                if att=='province':
                    province_set.add(val)
    province_list = list(province_set)
    res = find_result(province_list,pro_matches)
    return res
    
def amphoe_fail(amp_matches,Data):
    amphoe_set = set()
    for i in amp_matches:
        for k in Data:
            for att,val in k.items():
                if att=='amphoe':
                    amphoe_set.add(val)
    amphoe_list = list(amphoe_set)
    res = find_result(amphoe_list,amp_matches)
    return res
    
def tambon_fail(tam_matches,Data):
    tambon_set = set()
    for i in tam_matches:
        for k in Data:
            for att,val in k.items():
                if att=='district':
                    tambon_set.add(val)
    tambon_list = list(tambon_set)
    res = find_result(tambon_list,tam_matches)
    return res

def province_amphoe_fail(pro_amp_matches,Data):
    amphoe_set = set()
    for i in range(len(pro_amp_matches)):
        for j in range(len(pro_amp_matches[i])):
            if pro_amp_matches and j != len(pro_amp_matches[i])-1:
                #print(pro_amp_matches[i][j])
                for k in Data:
                    for att,val in k.items():
                        if att=='province' and val == pro_amp_matches[i][j]:
                            #print(val)
                            for att,val in k.items():
                                if att=='amphoe':
                                    amphoe_set.add(val)

    #print(amphoe_set)
    amphoe_list = list(amphoe_set)
    res = find_result(amphoe_list,pro_amp_matches[0][1])
    return res   
    
def province_tambon_fail(pro_tam_matches,Data):
    tambon_set = set()

    for i in range(len(pro_tam_matches)):
        for j in range(len(pro_tam_matches[i])):
            if pro_tam_matches and j != len(pro_tam_matches[i])-1:
                for k in Data:
                    for att,val in k.items():
                        if att=='province' and val==pro_tam_matches[i][j]:
                            for att,val in k.items():
                                if att=='district':
                                    tambon_set.add(val)

    tambon_list = list(tambon_set)
    res = find_result(tambon_list,pro_tam_matches[0][1])
    return res

def amphoe_tambon_fail(amp_tam_matches,Data):
    tambon_set = set()

    for i in range(len(amp_tam_matches)):
        for j in range(len(amp_tam_matches[i])):
            if amp_tam_matches and j != len(amp_tam_matches[i])-1:
                for k in Data:
                    for att,val in k.items():
                        if att=='amphoe' and val==amp_tam_matches[i][j]:
                            for att,val in k.items():
                                if att=='district':
                                    tambon_set.add(val)

    tambon_list = list(tambon_set)
    res = find_result(tambon_list,amp_tam_matches[0][1])
    return res

def province_amphoe_fail_tambon_fail(pro_amp_tam_matches,Data):
    amphoe_set = set()
    tambon_set = set()
    for i in range(len(pro_amp_tam_matches)):
        for j in range(len(pro_amp_tam_matches[i])):
            if pro_amp_tam_matches and j != len(pro_amp_tam_matches[i])-1:
                for k in Data:
                    for att,val in k.items():
                        if att=='province' and val==pro_amp_tam_matches[i][0]:
                            for att,val in k.items():
                                if att=='amphoe':
                                    amphoe_set.add(val)

                for k in Data:
                    for att,val in k.items():
                        if att=='province' and val==pro_amp_tam_matches[i][0]:
                            for att,val in k.items():
                                if att=='district':
                                    tambon_set.add(val)

    #print(amphoe_set)
    amphoe_list = list(amphoe_set)
    res1 = find_result(amphoe_list,pro_amp_tam_matches[i][1])
    #print(district_set)
    tambon_list = list(tambon_set)
    res2 = find_result(tambon_list,pro_amp_tam_matches[i][2])
    return res1,res2

    
def dict_action2():
    with open('dictionary/dict_verb/กระทำ2.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
def dict_action5():
    with open('dictionary/dict_verb/กระทำ5.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
def dict_action6():
    with open('dictionary/dict_verb/กระทำ6.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
def dict_action8():
    with open('dictionary/dict_verb/กระทำ8.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
    
def dict_hospital():
    with open('dictionary/dict_location/โรงบาล1.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict

def dict_country():
    with open('dictionary/dict_location/ประเทศ.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
    
def dict_store():
    with open('dictionary/dict_location/ห้าง.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict

def dict_university():
    with open('dictionary/dict_location/มหาลัย.txt','r',encoding='utf8') as read_file:
        dict = read_file.read()
        list_dict = dict.split('\n')
        return list_dict
    
def Autocorrection(x):
    Data = get_json_data()
    
    action2_fail = r"<กระทำ2_ผิด>([^<]*)</กระทำ2_ผิด>"
    action5_fail = r"<กระทำ5_ผิด>([^<]*)</กระทำ5_ผิด>"
    action6_fail = r"<กระทำ6_ผิด>([^<]*)</กระทำ6_ผิด>"
    action8_fail = r"<กระทำ8_ผิด>([^<]*)</กระทำ8_ผิด>"
    hospital_fail = r"<โรงพยาบาล_ผิด>([^<]*)</โรงพยาบาล_ผิด>"
    country_fail = r"<ประเทศ_ผิด>([^<]*)</ประเทศ_ผิด>"
    store_fail = r"<ห้าง_ผิด>([^<]*)</ห้าง_ผิด>"
    university_fail = r"<มหาวิทยาลัย_ผิด>([^<]*)</มหาวิทยาลัย_ผิด>"
    pro = r"<จังหวัด_ผิด>([^<]*)</จังหวัด_ผิด>"
    amp = r"<อำเภอ_ผิด>([^<]*)</อำเภอ_ผิด>"
    amp2 = r"<เขต_ผิด>([^<]*)</เขต_ผิด>"
    tam = r"[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>[^<]*"
    tam2 = r"[^<]*<แขวง_ผิด>([^<]*)</แขวง_ผิด>[^<]*"
    pro_amp = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<อำเภอ_ผิด>([^<]*)</อำเภอ_ผิด>"
    pro_tam = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"
    pro_amp2 = r"<จังหวัด>กรุงเทพฯ</จังหวัด>[^<]*<เขต_ผิด>([^<]*)</เขต_ผิด>"
    pro_tam2 = r"<จังหวัด>กรุงเทพฯ</จังหวัด>[^<]*<แขวง_ผิด>([^<]*)</แขวง_ผิด>"
    amp_tam = r"<อำเภอ>([^<]*)</อำเภอ>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"
    pro_amp_tam = r"<จังหวัด>([^<]*)</จังหวัด>[^<]*<อำเภอ_ผิด>([^<]*)</อำเภอ_ผิด>[^<]*<ตำบล_ผิด>([^<]*)</ตำบล_ผิด>"
    
    action2_fail_matches = regex.findall(action2_fail,x)
    action5_fail_matches = regex.findall(action5_fail,x)
    action6_fail_matches = regex.findall(action6_fail,x)
    action8_fail_matches = regex.findall(action8_fail,x)
    hospital_fail_matches = regex.findall(hospital_fail,x)
    country_fail_matches = regex.findall(country_fail,x)
    store_fail_matches = regex.findall(store_fail,x)
    university_fail_matches = regex.findall(university_fail,x)
    pro_matches = regex.findall(pro,x)
    amp_matches = regex.findall(amp,x)
    amp_matches2 = regex.findall(amp2,x)
    tam_matches = regex.findall(tam,x)
    tam_matches2 = regex.findall(tam2,x)
    pro_amp_matches = regex.findall(pro_amp,x)
    pro_tam_matches = regex.findall(pro_tam,x)
    amp_tam_matches = regex.findall(amp_tam,x)
    pro_amp_tam_matches = regex.findall(pro_amp_tam,x)
    
    if pro_amp_tam_matches :
        #province_amphoe_fail_tambon_fail(pro_amp_tam_matches,Data)
        for i in pro_amp_tam_matches:
            correct_x = regex.sub(r'<จังหวัด>'+i[0]+'</จังหวัด>', r'<จังหวัด>'+i[0]+'</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<อำเภอ_ผิด>'+i[1]+'</อำเภอ_ผิด>', r'<อำเภอ>'+province_amphoe_fail_tambon_fail(pro_amp_tam_matches,Data)[0]+'</อำเภอ>' , x)                      
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>'+i[2]+'</ตำบล_ผิด>',r'<ตำบล>'+province_amphoe_fail_tambon_fail(pro_amp_tam_matches,Data)[1]+'</ตำบล>' , x)
            x = correct_x
        
    if pro_amp_matches :
        #province_amphoe_fail(pro_amp_matches,Data)
        for i in pro_amp_matches:
            correct_x = regex.sub(r'<จังหวัด>'+i[0]+'</จังหวัด>',r'<จังหวัด>'+i[0]+'</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<อำเภอ_ผิด>'+i[1]+'</อำเภอ_ผิด>', r'<อำเภอ>'+province_amphoe_fail(pro_amp_matches,Data)+'</อำเภอ>' , x)                      
            x = correct_x
    
    if pro_tam_matches :
        #province_district_fail(pro_dis_matches,Data)
        for i in pro_tam_matches:
            correct_x = regex.sub(r'<จังหวัด>'+i[0]+'</จังหวัด>', r'<จังหวัด>'+i[0]+'</จังหวัด>', x)
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>'+i[1]+'</ตำบล_ผิด>',r'<ตำบล>'+province_tambon_fail(pro_tam_matches,Data)+'</ตำบล>' , x)
            x = correct_x
    if amp_tam_matches :
        #amphoe_district_fail(amp_dis_matches,Data)
        for i in amp_tam_matches:
            correct_x = regex.sub(r'<อำเภอ>'+i[0]+'</อำเภอ>', r'<อำเภอ>'+i[0]+'</อำเภอ>', x)
            x = correct_x
            correct_x = regex.sub(r'<ตำบล_ผิด>'+i[1]+'</ตำบล_ผิด>',r'<ตำบล>'+amphoe_tambon_fail(amp_tam_matches,Data)+'</ตำบล>' , x)
            x = correct_x
    if pro_matches:
        #province_fail(pro_matches,Data)
        
        for i in pro_matches:
            correct_x = regex.sub(r'<จังหวัด_ผิด>'+i+'</จังหวัด_ผิด>',r'<จังหวัด>'+province_fail(i,Data)+'</จังหวัด>', x)
            x = correct_x 
    if amp_matches:
        
        for i in amp_matches:
            correct_x = regex.sub(r'<อำเภอ_ผิด>'+i+'</อำเภอ_ผิด>',r'<อำเภอ>'+amphoe_fail(i,Data)+'</อำเภอ>', x)
            x = correct_x 

    if amp_matches2:
        
        for i in amp_matches2:
            correct_x = regex.sub(r'<เขต_ผิด>'+i+'</เขต_ผิด>',r'<เขต>'+amphoe_fail(i,Data)+'</เขต>', x)
            x = correct_x 
            
    if tam_matches:
        
        for i in tam_matches:
            correct_x = regex.sub(r'<ตำบล_ผิด>'+i+'</ตำบล_ผิด>',r'<ตำบล>'+tambon_fail(i,Data)+'</ตำบล>', x)
            x = correct_x 
    
    if tam_matches2:
        
        for i in tam_matches:
            correct_x = regex.sub(r'<แขวง_ผิด>'+i+'</แขวง_ผิด>',r'<แขวง>'+tambon_fail(i,Data)+'</แขวง>', x)
            x = correct_x 
    
    if action2_fail_matches:
        for i in action2_fail_matches:
            res = find_result(dict_action2(),i)
            correct_x = regex.sub(r'<กระทำ2_ผิด>'+i+'</กระทำ2_ผิด>', '<กระทำ2>'+res+'</กระทำ2>' , x)
            x = correct_x
            
    if action5_fail_matches:
        for i in action5_fail_matches:
            res = find_result(dict_action5(),i)
            correct_x = regex.sub(r'<กระทำ5_ผิด>'+i+'</กระทำ5_ผิด>', '<กระทำ5>'+res+'</กระทำ5>' , x)
            x = correct_x
    if action6_fail_matches:
        for i in action6_fail_matches:
            res = find_result(dict_action6(),i)
            correct_x = regex.sub(r'<กระทำ6_ผิด>'+i+'</กระทำ6_ผิด>', '<กระทำ6>'+res+'</กระทำ6>' , x)
            x = correct_x
    if action8_fail_matches:
        for i in action8_fail_matches:
            res = find_result(dict_action8(),i)
            correct_x = regex.sub(r'<กระทำ8_ผิด>'+i+'</กระทำ8_ผิด>', '<กระทำ8>'+res+'</กระทำ8>' , x)
            x = correct_x
    
    if hospital_fail_matches:
        for i in hospital_fail_matches:
            res = find_result(dict_hospital(),i)
            correct_x = regex.sub(r'<โรงพยาบาล_ผิด>'+i+'</โรงพยาบาล_ผิด>', '<โรงพยาบาล>'+res+'</โรงพยาบาล>' , x)
            x = correct_x
            
    if country_fail_matches:
        for i in country_fail_matches:
            res = find_result(dict_country(),i)
            correct_x = regex.sub(r'<ประเทศ_ผิด>'+i+'</ประเทศ_ผิด>', '<ประเทศ>'+res+'</ประเทศ>' , x)
            x = correct_x
            
    if store_fail_matches:
        for i in store_fail_matches:
            res = find_result(dict_store(),i)
            correct_x = regex.sub(r'<ห้าง_ผิด>'+i+'</ห้าง_ผิด>', '<ห้าง>'+res+'</ห้าง>' , x)
            x = correct_x
            
    if university_fail_matches:
        for i in university_fail_matches:
            res = find_result(dict_university(),i)
            correct_x = regex.sub(r'<มหาวิทยาลัย_ผิด>'+i+'</มหาวิทยาลัย_ผิด>', '<มหาวิทยาลัย>'+res+'</มหาวิทยาลัย>' , x)
            x = correct_x
            
    return x

def edit_distance1(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

def find_result(list_result,word_fail):
    list_index = []
    #print(list_result) #แสดง list ชื่อที่เป็น subset ของข้อมูล tag ตัวหน้า
    for x in list_result:
        list_index.append(edit_distance1(word_fail, x))
    
    #print(list_index) #แสดง list ค่าการแก้คำ ระหว่างคำผิดที่เรา input มา เทียบกับคำที่อยู่ใน list_result
    for i in range(len(list_index)):
        if list_index[i] == min(list_index):
            #print(i,list_index[i])
            index_result = i
    
    #print(index_result) #แสดงตำแหน่งของคำที่มีการแก้น้อยที่สุด
    for i in range(len(list_result)):
        if index_result == i:
            result = list_result[i]
            return result