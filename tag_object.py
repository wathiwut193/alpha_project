from bs4 import BeautifulSoup
import requests
import re
import regex
import numpy as np
import codecs


def tag_start(read_text):
    """
    function start is function run all function can edit should func to run
    :param read_text
    :return: text with tag
    """
    # read_text = tag_time(read_text)
    # read_text = tag_date(read_text)
    read_text = tag_action(read_text)
    read_text = tag_adverb(read_text)
    #read_text = tag_location(read_text)
    # read_text = tag_person(read_text)
    # read_text = tag_......
    return read_text


def tag_time(read_text):
    """
    function tag time format
    :param read_text
    :return: text with tag <เวลา> </เวลา>
    """
    # tad_date_and_time
    regex_time = r"(([0-1][\d]|[2][0-4])\s?(:|.)([0-5][\d])\s?(นาฬิกา|น\.|น))"
    regex_time1 = r"((ช่วง|ตอน)(เช้า))"
    regex_time2 = r"((ช่วง|ตอน)(สาย))"
    regex_time3 = r"((ช่วง|ตอน)(เที่ยง))"
    regex_time4 = r"((ช่วง|ตอน)(บ่าย))"
    regex_time5 = r"((ช่วง|ตอน)(เย็น))"
    regex_time6 = r"((ช่วง|ตอน)(ค่ำ))"
    regex_time7 = r"((ช่วง|ตอน)(ดึก))"
    regex_time8 = r"((ช่วง|ตอน)(กลางดึก))"
    regex_time9 = r"((ช่วง|ตอน)(เช้ามืด|เช้าตรู่))"

    matches_time = regex.sub(regex_time, r'<เวลา>\1</เวลา>', read_text)
    read_text = matches_time
    matches_time9 = regex.sub(regex_time9, r'<เวลา>03:00 น. - 05:59 น.</เวลา>', read_text)
    read_text = matches_time9
    matches_time1 = regex.sub(regex_time1, r'<เวลา>06:00 น. - 08:59 น.</เวลา>', read_text)
    read_text = matches_time1
    matches_time2 = regex.sub(regex_time2, r'<เวลา>09:00 น. - 10:59 น.</เวลา>', read_text)
    read_text = matches_time2
    matches_time3 = regex.sub(regex_time3, r'<เวลา>11:00 น. - 12:59 น.</เวลา>', read_text)
    read_text = matches_time3
    matches_time4 = regex.sub(regex_time4, r'<เวลา>13:00 น. - 15:59 น.</เวลา>', read_text)
    read_text = matches_time4
    matches_time5 = regex.sub(regex_time5, r'<เวลา>16:00 น. - 18:59 น.</เวลา>', read_text)
    read_text = matches_time5
    matches_time6 = regex.sub(regex_time6, r'<เวลา>19:00 น. - 20:59 น.</เวลา>', read_text)
    read_text = matches_time6
    matches_time7 = regex.sub(regex_time7, r'<เวลา>21:00 น. - 02:59 น.</เวลา>', read_text)
    read_text = matches_time7
    matches_time8 = regex.sub(regex_time8, r'<เวลา>01:00 น. - 03:59 น.</เวลา>', read_text)
    read_text = matches_time8

    return read_text


def tag_date(read_text):
    """
    tag <วัน> </วัน> in date pattern
    :param read_text:
    :return: <วัน> date </วัน>
    """
    regex_date = (
        r"(([1-9]|[0-2][\d]|[3][0-1])\s?(/)?(ม\.ค\.|มกราคม|มกรา|ก\.พ\.|กุมภาพันธ์|กุมภา|มี\.ค\.|มีนาคม|มีนา|เม\.ย\.|"
        "เมษายน|เมษา|พ\.ค\.|พฤษภาคม|พฤษภา|มิ\.ย\.|มิถุนายน|มิถุนา|ก\.ค\.|กรกฎาคม|กรกฎา|ส\.ค\.|สิงหาคม|สิงหา|ก\.ย\.|"
        "กันยายน|กันยา|ต\.ค\.|ตุลาคม|ตุลา|พ\.ย\.|พฤศจิกายน|พฤศจิกา|ธ\.ค\.|ธันวาคม|ธันวาคม)\s?(/)?(พ.ศ.|ค.ศ.|พศ|คศ)?\s?"
        "(\d\d\d\d|\d\d)?|([1-9]|[0-2][\d]|[3][0-1])\s?(/|-|\.)([0][\d]|[1][0-2])\s?(/|-|\.)(\d\d\d\d|\d\d))")

    matches_date = regex.sub(regex_date, r'<วัน>\1</วัน>', read_text)
    read_text = matches_date

    return read_text


def tag_secondary_action_1(read_text):
    regex_action = (
        r'(ทำร้าย|ตี|ต่อย|เตะ|ตบ|ชก|ทุบ|ซ้อม|ทะเลาะวิวาท|ต่อสู้|ปล้น|จี้|ชิงทรัพย์|ลักทรัพย์|วิ่งราว|ล้วงกระเป๋า|'
        'แบล็คเมล์|ค้ายา|เสพยา|ขายยา|ล่อลวง|ก่อเหตุ|ระเบิด|'
        'หลบหนี|หลบ|หนี|กบดาน|ซ่อนตัว|มอบตัว|สารภาพ|ยอมรับ|ให้การปฏิเสธ)')
    data_text = regex.sub(regex_action, r'<กระทำรอง1>\1</กระทำรอง1>', read_text)
    return data_text


def tag_action(read_text):
    """
    tag verb with <กระทำ> ... </กระทำ>
    :param read_text:
    :return: <กระทำ> verb </กระทำ>
    """
    # read dictionary
    read_file_act1 = codecs.open('dictionary/dict_verb/กระทำ1.txt', 'r', 'utf8')
    read_act1 = read_file_act1.read()
    read_act1_list = read_act1.split('\n')
    list_str_act1 = '|'.join(read_act1_list[:len(read_act1_list) - 1])
    list_str_act1 += '|' + read_act1_list[len(read_act1_list) - 1]

    read_file_act2 = codecs.open('dictionary/dict_verb/กระทำ2.txt', 'r', 'utf8')
    read_act2 = read_file_act2.read()
    read_act2_list = read_act2.split('\n')
    list_str_act2 = '|'.join(read_act2_list[:len(read_act2_list) - 1])
    list_str_act2 += '|' + read_act2_list[len(read_act2_list) - 1]

    read_file_act3 = codecs.open('dictionary/dict_verb/กระทำ3.txt', 'r', 'utf8')
    read_act3 = read_file_act3.read()
    read_act3_list = read_act3.split('\n')
    list_str_act3 = '|'.join(read_act3_list[:len(read_act3_list) - 1])
    list_str_act3 += '|' + read_act3_list[len(read_act3_list) - 1]

    read_file_act4 = codecs.open('dictionary/dict_verb/กระทำ4.txt', 'r', 'utf8')
    read_act4 = read_file_act4.read()
    read_act4_list = read_act4.split('\n')
    list_str_act4 = '|'.join(read_act4_list[:len(read_act4_list) - 1])
    list_str_act4 += '|' + read_act4_list[len(read_act4_list) - 1]

    read_file_act5 = codecs.open('dictionary/dict_verb/กระทำ5.txt', 'r', 'utf8')
    read_act5 = read_file_act5.read()
    read_act5_list = read_act5.split('\n')
    list_str_act5 = '|'.join(read_act5_list[:len(read_act5_list) - 1])
    list_str_act5 += '|' + read_act5_list[len(read_act5_list) - 1]

    read_file_act6 = codecs.open('dictionary/dict_verb/กระทำ6.txt', 'r', 'utf8')
    read_act6 = read_file_act6.read()
    read_act6_list = read_act6.split('\n')
    list_str_act6 = '|'.join(read_act6_list[:len(read_act6_list) - 1])
    list_str_act6 += '|' + read_act6_list[len(read_act6_list) - 1]

    read_file_act8 = codecs.open('dictionary/dict_verb/กระทำ8.txt', 'r', 'utf8')
    read_act8 = read_file_act8.read()
    read_act8_list = read_act8.split('\n')
    list_str_act8 = '|'.join(read_act8_list[:len(read_act8_list) - 1])
    list_str_act8 += '|' + read_act8_list[len(read_act8_list) - 1]
    # rule tag action
    regex_act1 = (r"((?!ยิง\|?ตัว|ฆ่า\|?ตัว|ฟัน\|?กำไร)(" + list_str_act1 + "))")
    regex_act2 = (r"((" + list_str_act2 + "))")
    regex_act3 = (r"((" + list_str_act3 + "))")
    regex_act4 = (r"(((?!พาล|พานิช|พาย|พาหนะ|พาน|พาด)(?<!พก\|?|พัด\|?|สะ|วิ|ยาน|เฉ|บูร|อัม|อัล|อ|พิ|อาคาร\|?)พา))")
    regex_act5 = (r"((?!ให้การ\|?ปฏิเสธ)(" + list_str_act5 + "))")
    regex_act6 = (r"((" + list_str_act6 + "))")
    regex_act8 = (r"((" + list_str_act8 + "))")
    # add tag
    matches_act1 = regex.sub(regex_act1, r'<กระทำ1>\1</กระทำ1>', read_text)
    read_text = matches_act1
    matches_act2 = regex.sub(regex_act2, r'<กระทำ2>\1</กระทำ2>', read_text)
    read_text = matches_act2
    matches_act3 = regex.sub(regex_act3, r'<กระทำ3>\1</กระทำ3>', read_text)
    read_text = matches_act3
    matches_act4 = regex.sub(regex_act4, r'<กระทำ4>\1</กระทำ4>', read_text)
    read_text = matches_act4
    matches_act5 = regex.sub(regex_act5, r'<กระทำ5>\1</กระทำ5>', read_text)
    read_text = matches_act5
    matches_act6 = regex.sub(regex_act6, r'<กระทำ6>\1</กระทำ6>', read_text)
    read_text = matches_act6
    matches_act8 = regex.sub(regex_act8, r'<กระทำ8>\1</กระทำ8>', read_text)
    read_text = matches_act8
    return read_text


def tag_location(read_text):
    """
    read text file this is dictionary of location or place
    :param read_text:
    :return tag <สภานที่> </สถานที่>
    """

    read_file_p = codecs.open('dictionary/dict_location/จังหวัด.txt', 'r', 'utf-8')
    read_p = read_file_p.read()
    read_p_list = read_p.split('\n')
    list_str_p = '|'.join(read_p_list[:len(read_p_list) - 1])
    list_str_p += '|' + read_p_list[len(read_p_list) - 1]

    read_file_c = codecs.open('dictionary/dict_location/ประเทศ.txt', 'r', 'utf-8')
    read_c = read_file_c.read()
    read_c_list = read_c.split('\n')
    list_str_c = '|'.join(read_c_list[:len(read_c_list) - 1])
    list_str_c += '|' + read_c_list[len(read_c_list) - 1]

    read_file_t = codecs.open('dictionary/dict_location/ตำบล.txt', 'r', 'utf-8')
    read_t = read_file_t.read()
    read_t_list = read_t.split('\n')
    list_str_t = '|'.join(read_t_list[:len(read_t_list) - 1])
    list_str_t += '|' + read_t_list[len(read_t_list) - 1]

    read_file_a = codecs.open('dictionary/dict_location/อำเภอ.txt', 'r', 'utf-8')
    read_a = read_file_a.read()
    read_a_list = read_a.split('\n')
    list_str_a = '|'.join(read_a_list[:len(read_a_list) - 1])
    list_str_a += '|' + read_a_list[len(read_a_list) - 1]

    read_file_area = codecs.open('dictionary/dict_location/เขต.txt', 'r', 'utf-8')
    read_area = read_file_area.read()
    read_area_list = read_area.split('\n')
    list_str_area = '|'.join(read_area_list[:len(read_area_list) - 1])
    list_str_area += '|' + read_area_list[len(read_area_list) - 1]

    read_file_d = codecs.open('dictionary/dict_location/แขวง.txt', 'r', 'utf-8')
    read_d = read_file_d.read()
    read_d_list = read_d.split('\n')
    list_str_d = '|'.join(read_d_list[:len(read_d_list) - 1])
    list_str_d += '|' + read_d_list[len(read_d_list) - 1]

    read_file_r = codecs.open('dictionary/dict_location/ถนน.txt', 'r', 'utf-8')
    read_r = read_file_r.read()
    read_r_list = read_r.split('\n')
    list_str_r = '|'.join(read_r_list[:len(read_r_list) - 1])
    list_str_r += '|' + read_r_list[len(read_r_list) - 1]

    read_file_ri = codecs.open('dictionary/dict_location/แม่น้ำ.txt', 'r', 'utf-8')
    read_ri = read_file_ri.read()
    read_ri_list = read_ri.split('\n')
    list_str_ri = '|'.join(read_ri_list[:len(read_ri_list) - 1])
    list_str_ri += '|' + read_ri_list[len(read_ri_list) - 1]

    read_file_m = codecs.open('dictionary/dict_location/ห้าง.txt', 'r', 'utf-8')
    read_m = read_file_m.read()
    read_m_list = read_m.split('\n')
    list_str_m = '|'.join(read_m_list[:len(read_m_list) - 1])
    list_str_m += '|' + read_m_list[len(read_m_list) - 1]

    read_file_h = codecs.open('dictionary/dict_location/โรงบาล1.txt', 'r', 'utf-8')
    read_h = read_file_h.read()
    read_h_list = read_h.split('\n')
    list_str_h = '|'.join(read_h_list[:len(read_h_list) - 1])
    list_str_h += '|' + read_h_list[len(read_h_list) - 1]

    read_file_uni = codecs.open('dictionary/dict_location/มหาลัย.txt', 'r', 'utf-8')
    read_uni = read_file_uni.read()
    read_uni_list = read_uni.split('\n')
    list_str_uni = '|'.join(read_uni_list[:len(read_uni_list) - 1])
    list_str_uni += '|' + read_uni_list[len(read_uni_list) - 1]

    regex_province2 = (
            r"(((?<!ผว|\.)จ\.|จังหวัด|(?<!\.)จว.)\s?(" + list_str_p + "){e<=1}|(กรุงเทพมหานคร|กรุงเทพ|กทม\.))")

    regex_province = (
            r"<จังหวัด_ผิด>(((?<!\.)จ\.|จังหวัด|(?<!\.)จว.)\s?(" + list_str_p + ")|(กรุงเทพมหานคร|กรุงเทพ|กทม\.))</จังหวัด_ผิด>")

    regex_country2 = (r"((ประเทศ)\s?(" + list_str_c + "){e<=1})")

    regex_country = (r"<ประเทศ_ผิด>((ประเทศ)\s?(" + list_str_c + "))</ประเทศ_ผิด>")

    regex_area2 = (r"((เขต)\s?(" + list_str_area + "){e<=1})")

    regex_area = (r"<เขต_ผิด>((เขต)\s?(" + list_str_area + "))</เขต_ผิด>")

    regex_district2 = (r"((แขวง)\s?(" + list_str_d + "){e<=1})")

    regex_district = (r"<แขวง_ผิด>((แขวง)\s?(" + list_str_d + "))</แขวง_ผิด>")

    regex_road2 = (r"(((?<!\.)ถ\.|ถนน)\s?(" + list_str_r + "){e<=1})")

    regex_road = (r"<ถนน_ผิด>(((?<!\.)ถ\.|ถนน)\s?(" + list_str_r + "))</ถนน_ผิด>")

    regex_amphoe2 = (r"(((?<!นาย)อำเภอ|(?<!\.)อ\.)\s?(" + list_str_a + "){e<=1})")

    regex_amphoe = (r"<อำเภอ_ผิด>(((?<!นาย)อำเภอ|(?<!\.)อ\.)\s?(" + list_str_a + "))</อำเภอ_ผิด>")

    regex_river2 = (r"((แม่น้ำ)(" + list_str_ri + "){e<=1})")

    regex_river = (r"<แม่น้ำ_ผิด>((แม่น้ำ)(" + list_str_ri + "))</แม่น้ำ_ผิด>")

    regex_tambon2 = (r"((ตำบล|(?<!\.)ต\.)\s?(?![ก-๙]\.)(" + list_str_t + "){e<=1})")

    regex_tambon = (r"<ตำบล_ผิด>(\s?(ตำบล|(?<!\.)ต\.)\s?(?![ก-๙]\.)(" + list_str_t + ")\s?)</ตำบล_ผิด>")

    regex_all = (
        r"((?!ซอยดังกล่าว|ซอยเล็ก|ซอยหอ|ซอยใกล้|ซอยหรือ|ซอยไป|ซอยมี|ซอยถัด|สน.ที่|ซอยริมถนน|ซอยข้าง|ซอยเข้า|ซอยเปลี่ยว|ซอยที่เกิดเหตุ|ซอยตัน|ซอยหลบ|ซอยแคบ|ซอยด้วย|ซอยไม่มีชื่อ|ซอยข้างบ้าน|สน.ออก)(ซอย|\sซ\.|(?<!ท|\.)สภ\.|สน\.)(\d\d?|[ก-๙]{2,}(?=แล้ว|ชัก|ไป|สอบ|ได้|จะ|ดำเนิน|มายัง|ต่อไป|จับกุม|เพื่อ|กล่าว|ดำเนิน|และ|รับเเจ้ง|ได้รับ|รับตัว)"
        "|(?!ตาย|เพื่อ|ได้|ของ|ใกล้|แล้ว|ให้|แวะ)[ก-๙]{2,}\s?(\d?\d?))|(?!ย่านถนน|ย่านชุมชน|ย่านซอย|ย่านนี้)(ย่าน)([ก-๙]{2,}(?=ตาย|หาเงิน|เพื่อ)|[ก-๙]{2,})(\s?\d?\d?)|(บ้านเลขที่|ห้องเลขที่|บ้านเช่าเลขที่)\s?(\d\d?\d?\d?)"
        "(/)?(\d?\d?\d?)|((หมู่|หมู่ที่|(?<!ชั้น|\.|สาว)\sม\.)\s?(\d\d?))|((ที่|ใน|คา)(?<!พนักงาน)โรงแรม|โรงเรียน|โรงรับจำนำ|โรงงาน)(?!เถื่อน|ฟัง|เอง|ส่ง|ต่าง|เท่านั้น|ทั้ง|แห่งนี้|แต่|กับ|เพราะ|เป็น|ที่|ส่วน|สั่ง|แห่งเดียว|จะได้|เดียว|ได้สั่ง|ก็โดน|ใน|มี|ต่างหาก|ก็เห็น|ใกล้|ตนได้|และ|ว่า|ที่เกิดเหตุ)([ก-๙]{2,}(?=ชื่อ|ย่าน|ใน|ริม)|(?!จริง|ชื่อ|ดังกล่าว)[ก-๙]{2,})|"
        "(?!ที่คอนโดมิเดียมแห่งนี้)(บริเวณ|ภายใน|ที่|ใน|คา)(คอนโด|แมนชั่น|อะพาร์ตเมนต์|หน้าผับ|ผับ|ห้องเช่า|ห้องแถว)|"
        "(?!ที่ร้านอาหารดังกล่าว|ที่ร้านขายแต่)(บริเวณ|ภายใน|ที่|ใน|คา)(หน้าร้าน|ร้าน)(กาแฟ[ก-๙]{2,}|ข้าว[ก-๙]{2,}|อาหาร[ก-๙]{2,}(?=ใน|ชื่อ|ย่าน)|อาหาร[ก-๙]{2,}|"
        "ซ่อม[ก-๙]{2,}(?=ดังกล่าว)|ซ่อม[ก-๙]{2,}|ขาย[ก-๙]{2,}(?=ชื่อ|และ|ที่อยู่)|ขาย[ก-๙]{2,}|ทำ[ก-๙]{2,}|เสริม[ก-๙]{2,}|ร้านน้ำ[ก-๙]{2,}|สะดวกซื้อ|เซเว่นอีเลฟเว่น|เซเว่น|กาแฟ|อาหาร|คาราโอเกะ"
        "|เฟอร์นิเจอร์|เคเอฟซี|พิซซ่า|ทอง)|(ที่|ใน|คา)(บ้านพัก|บ้านหลังหนึ่ง|บ้านแห่งหนึ่ง|บ้านเช่า))")

    regex_mall = (r"((ห้างสรรพสินค้า|ห้าง)(" + list_str_m + "))")
    regex_mall2 = (
            r"((?!ห้างฉัตร)(ห้างสรรพสินค้า|ห้าง)((?!ร้าน|ดัง|เปิด|และ|ค้า|ได้|ซึ่ง|" + list_str_m + ")[ก-๙]{2,}))")

    regex_hos = (r"((โรงพยาบาล|ร\.พ\.|รพ\.)(" + list_str_h + "))")
    regex_hos2 = (
            r"((โรงพยาบาล|ร\.พ\.|รพ\.)(?!เสียก่อน|ก่อน|ยืนยัน|อื่น|จ่าย|เป็น|เอง|ทันที|หลาย|โทร|ได้|เพื่อ|ว่า|ให้การ|ตำบล|สต|แล้ว|ใน|ใส่|ขณะ|เดิน|ได้แล้ว|เขาก็|ใกล้|ก่อนหน้า|ดังกล่าว|" + list_str_h + ")([ก-๙]{2,}(?=หาสาเหตุ|อาการ|ทันที|โดย|อีก|เพื่อ|ในเวลา)|[ก-๙]{2,}))")

    regex_university = (r"((มหาวิทยาลัย|มหาลัย)(" + list_str_uni + "))")
    regex_university2 = (
            r"((มหาวิทยาลัย|มหาลัย)(?!แล้ว|ก่อน|อื่น|ยืนยัน|หลาย|ได้|เพื่อ|ตำบล|ชื่อดัง|ดังกล่าว|ที่เคย|ต้นสังกัด|ไม่|" + list_str_uni + ")([ก-๙]{2,}))")

    matches_province2 = regex.sub(regex_province2, r'<จังหวัด_ผิด>\1</จังหวัด_ผิด>', read_text)
    read_text = matches_province2
    matches_province = regex.sub(regex_province, r'<จังหวัด>\1</จังหวัด>', read_text)
    read_text = matches_province
    matches_country2 = regex.sub(regex_country2, r'<ประเทศ_ผิด>\1</ประเทศ_ผิด>', read_text)
    read_text = matches_country2
    matches_country = regex.sub(regex_country, r'<ประเทศ>\1</ประเทศ>', read_text)
    read_text = matches_country
    matches_area2 = regex.sub(regex_area2, r'<เขต_ผิด>\1</เขต_ผิด>', read_text)
    read_text = matches_area2
    matches_area = regex.sub(regex_area, r'<เขต>\1</เขต>', read_text)
    read_text = matches_area
    matches_district2 = regex.sub(regex_district2, r'<แขวง_ผิด>\1</แขวง_ผิด>', read_text)
    read_text = matches_district2
    matches_district = regex.sub(regex_district, r'<แขวง>\1</แขวง>', read_text)
    read_text = matches_district
    matches_road2 = regex.sub(regex_road2, r'<ถนน_ผิด>\1</ถนน_ผิด>', read_text)
    read_text = matches_road2
    matches_road = regex.sub(regex_road, r'<ถนน>\1</ถนน>', read_text)
    read_text = matches_road
    matches_tambon2 = regex.sub(regex_tambon2, r'<ตำบล_ผิด>\1</ตำบล_ผิด>', read_text)
    read_text = matches_tambon2
    matches_tambon = regex.sub(regex_tambon, r'<ตำบล>\1</ตำบล>', read_text)
    read_text = matches_tambon
    matches_amphoe2 = regex.sub(regex_amphoe2, r'<อำเภอ_ผิด>\1</อำเภอ_ผิด>', read_text)
    read_text = matches_amphoe2
    matches_amphoe = regex.sub(regex_amphoe, r'<อำเภอ>\1</อำเภอ>', read_text)
    read_text = matches_amphoe
    matches_river2 = regex.sub(regex_river2, r'<เเม่น้ำ_ผิด>\1</เเม่น้ำ_ผิด>', read_text)
    read_text = matches_river2
    matches_river = regex.sub(regex_river, r'<เเม่น้ำ>\1</เเม่น้ำ>', read_text)
    read_text = matches_river
    matches_all = regex.sub(regex_all, r'<สถานที่>\1</สถานที่>', read_text)
    read_text = matches_all
    matches_mall2 = regex.sub(regex_mall2, r'<ห้าง_ผิด>\1</ห้าง_ผิด>', read_text)
    read_text = matches_mall2
    matches_mall = regex.sub(regex_mall, r'<ห้าง>\1</ห้าง>', read_text)
    read_text = matches_mall
    matches_hos2 = regex.sub(regex_hos2, r'<โรงพยาบาล_ผิด>\1</โรงพยาบาล_ผิด>', read_text)
    read_text = matches_hos2
    matches_hos = regex.sub(regex_hos, r'<โรงพยาบาล>\1</โรงพยาบาล>', read_text)
    read_text = matches_hos
    matches_university2 = regex.sub(regex_university2, r'<มหาวิทยาลัย_ผิด>\1</มหาวิทยาลัย_ผิด>', read_text)
    read_text = matches_university2
    matches_university = regex.sub(regex_university, r'<มหาวิทยาลัย>\1</มหาวิทยาลัย>', read_text)
    read_text = matches_university

    regex_hos2 = (r"<โรงพยาบาล_ผิด>((โรงพยาบาล|ร\.พ\.|รพ\.)(?!ได้|" + list_str_h + ")([ก-๙]{2,}))</โรงพยาบาล_ผิด>")
    regex_mall2 = (
            r"<ห้าง_ผิด>((?!ห้างฉัตร)(ห้างสรรพสินค้า|ห้าง)((?!ร้าน|ดัง|เปิด|และ|ค้า|ได้|ซึ่ง|" + list_str_m + ")[ก-๙]{2,}))</ห้าง_ผิด>")
    regex_university2 = (
            r"<หมาวิทยาลัย_ผิด>((มหาวิทยาลัย|มหาลัย)(?!แล้ว|หลาย|ได้|เพื่อ|ตำบล|ชื่อดัง|ดังกล่าว|ที่เคย|ต้นสังกัด|ไม่|" + list_str_uni + ")([ก-๙]{2,}))</มหาวิทยาลัย_ผิด>")

    matches_hos2 = regex.finditer(regex_hos2, read_text, re.MULTILINE)
    matches_mall2 = regex.finditer(regex_mall2, read_text, re.MULTILINE)
    matches_university2 = regex.finditer(regex_university2, read_text, re.MULTILINE)

    count = 0
    for matchNum, match in enumerate(matches_hos2):
        count += 0

        word = match.group(2) + match.group(3)

        url = 'https://www.google.com/search?q=\"' + str(word) + '\"'
        # print(url)
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        x = soup.find_all("a", {"class": "gL9Hy"})

        for i in x:
            word = i.text.strip('\"')

        aof = ("แก้คำที่ใน tag <โรงพยาบาล_ผิด> เป็น: <โรงพยาบาล>" + word + "</โรงพยาบาล>")
        # print(aof)
        regex_hos1 = (r"((โรงพยาบาล|ร\.พ\.|รพ\.))")
        matches_hos1 = regex.sub(regex_hos1, r'', word)
        read_text1 = matches_hos1

        word_not_dict = matches_hos1

        fobj = open("dictionary/dict_location/โรงบาล1.txt", 'r', encoding='utf-8')
        text = fobj.read().strip().split()
        fobj.close()

        s = word_not_dict

        if s == "":
            continue
        if s in text:
            continue
        else:
            fobjw = open("dictionary/dict_location/โรงบาล1.txt", 'a', encoding='utf-8')
            fobjw.write("\n" + s)

            fobjw.close()
    for matchNum, match in enumerate(matches_mall2):
        count += 1

        word = match.group(2) + match.group(3)

        url = 'https://www.google.com/search?q=\"' + str(word) + '\"'

        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        x = soup.find_all("a", {"class": "gL9Hy"})

        for i in x:
            word = i.text.strip('\"')

        aof = ("แก้คำที่ใน tag <ห้าง_ผิด> เป็น: <ห้าง>" + word + "</ห้าง>")

        regex_mall1 = (r"((ห้างสรรพสินค้า|ห้าง))")
        matches_mall1 = regex.sub(regex_mall1, r'', word)
        read_text1 = matches_mall1

        word_not_dict = matches_mall1

        fobj = open("dictionary/dict_location/ห้าง.txt", 'r', encoding='utf-8')
        text = fobj.read().strip().split()
        fobj.close()
        # เงื่อนไข
        s = word_not_dict
        if s == "":
            continue
        if s in text:

            continue
        else:
            fobjw = open("dictionary/dict_location/ห้าง.txt", 'a', encoding='utf-8')
            fobjw.write("\n" + s)
            continue
        fobjw.close()
    for matchNum, match in enumerate(matches_university2):
        count += 1

        word = match.group(2) + match.group(3)

        url = 'https://www.google.com/search?q=' + str(word)
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        x = soup.find_all("a", {"class": "gL9Hy"})

        for i in x:
            word = i.text

        aof = ("แก้คำที่ใน tag <มหาวิทยาลัย_ผิด> เป็น : <มหาวิทยาลัย>" + word + "</มหาวิทยาลัย>")

        regex_uni1 = (r"((มหาวิทยาลัย|มหาลัย))")
        matches_uni1 = regex.sub(regex_uni1, r'', word)
        read_text1 = matches_uni1

        word_not_dict = matches_uni1

        fobj = open("dictionary/dict_location/มหาลัย.txt", 'r', encoding='utf-8')
        text = fobj.read().strip().split()
        fobj.close()
        # เงื่อนไข
        s = word_not_dict
        if s == "":
            continue
        if s in text:

            continue
        else:
            fobjw = open("dictionary/dict_location/มหาลัย.txt", 'a', encoding='utf-8')
            fobjw.write("\n" + s)

        fobjw.close()
    return read_text


def tag_person(read_text):
    regex_name = (
        r"((นาย|นาง|นางสาว|น\.ส\.|นพ\.|ส\.ต\.|ร\.ต\.อ\.|ร\.ต\.|ดร\.|ร\.อ\.|พ\.อ\.|จ\.ส\.ต\.|จ่าสิบตำรวจ|ส\.ต\.อ\.|สิบตำรวจเอก|ส\.ต\.ท\.|"
        "สิบตำรวจโท|ส\.ต\.ต\.|สิบตำรวจตรี|ด\.ต\.|แพทย์หญิง|พญ\.|ทันตแพทย์|ทพ\.|รองศาสตราจารย์|ผู้ช่วยศาสตราจารย์|"
        "พล\.อ\.ต\.|พลอากาศตรี|พล\.อ\.ท\.|พลอากาศโท|พล\.อ\.อ\.|พลอากาศเอก|พล\.อ\.|พลเอก|พล\.ท\.|พลโท|พลตรี|พล\.ต\.อ\.|พลตำรวจเอก|"
        "พลตำรวจโท|พล\.ต\.ท\.|พลตำรวจตรี|พล\.ต\.ต\.|พ\.ต\.อ\.|พันจ่าอากาศ|พันตำรวจเอก|พันตำรวจโท|พ\.ต\.ท\.|พันตำรวจตรี|พ\.ต\.ต\.|ร้อยตำรวจเอก|"
        "ร้อยตำรวจโท|ร\.ต\.ท\.|ร้อยตำรวจตรี|ร\.ต\.ต\.|พล\.ต\.|ส\.ต\.|เด็กชาย|ด\.ช\.|เด็กหญิง|ด\.ญ\.)\s?([ก-๙]{2,20})\s(หรือ\s?[ก-๙]{2,20})\s((?!สารภาพ|พฤติกรรม|สัมภาษณ์|สัญชาติ|ก้มกราบ|คู่กรณี|น้องของ|พนักงาน|เกิดความ|เยาวชน|สะบัด|ดิ้น|ร่วมรัก|โมโห|"
        "ยังอยู่|หลานของ|หลานชาย|หลานสาว|ตัดสิน|พยายาม|ชาวบ้าน|ชาว|พี่|พ่อ|ลูก|ลูก|หลบ|อยู่ใน|เพื่อน|แม่|คิดตัด|กล่าว|ทำงาน|น่าจะ|ปล่อย|นามสมมุติ|ภายใน|ภายนอก|กระทำ|แสดงตัว|ดูแล|ม่าย|"
        "พร้อม|จาก|จับ|ห้อย|โดย|เพิ่ง|ปั่น|นั้น|สวม|ด้วย|เบื้อง|ถึง|เล่า|ฟัง|กำลัง|ทราบ|ถือ|เริ่ม|บอก|แล้ว|ยกมือ|อดีต|ลง|ติดเชื้อ|ตกใจ|ทำร้าย|ใช่|จำเลย|ตั้ง|แต่ง|อย่าง|ย้อน|ข้อหา|บ่าย|เช้า|กลางวัน|ดึก|"
        "ภรรยา|มารดา|ซึ่ง|ญาติ|ตื่น|นั่ง|บิดา|เสียชีวิต|ย้าย|ระบุ|วิ่ง|หรือ|สามี|อายุ|อ้าง|เข้า|เปิด|เป็น|เห็น|กับ|ขณะ|ขับ|ขี่|จึง|จู่|ตอบ|ถูก|ทาง|ที่|ผู้|พัก|ยอม|ยัง|รับ|รุม|บริเวณ|ถอด|รอดคดี|น้อง|น้องสาว|เสพยา|โยน|"
        "เซล้ม|กลัว|โทร|ทั้งหมด|ทั้งสอง|ปรากฏ|ล้ม|กระโดด|แฟน|ก่อเหตุ|มากนัก|ค้างค่า|ตรวจค้น|เบื้องต้น|ประกอบ|ส่วน|ฟ้อง|ยื่น|ฐานะ|ตาม|จำนวน|เกลี้ยกล่อม|ขัดขวาง|ซุกซ่อน|บาดเจ็บ|อยู่บ้าน|เพียงลำพัง|หลอก|"
        "ขัดขืน|ต่อสู้|หมดสติ|อำพราง|กบดาน|อาวุธ|ขโมย|ต่อย|ทิ่ม|ล้วง|ปะทะ|เล็ง|อุ้ม|ข่ม|ค้น|ฆ่า|ตัด|แทง|ฟาด|ล่า|นอน|ตบ|พก|เอเย่นต์|ทะเลาะ|ลูกเขย|ยืม|หลังก่อ|ซ้อน|อยู่ที่|อยู่อีก|อยู่นั้น|อยู่ตรง|อยู่แล้ว|"
        "ลุก|ส่ง|ออก|อาจ|อีก|เคย|เผย|เอา|จริง|หาย|แชท|แต่|และ|แอบ|เจ้า|มือ|เพื่อ|กลับ|ใช้|ให้|ได้|ไม่|ไล่|ไว้|ก็|คน|จน|จะได้|ทน|มานี่|มีอาการ|มีหมาย|ไป|ใน|พบ|พาไป|พากลับ|พามา|นำ|ว่า|ยิง|หนี|ประสานมา|ชก|"
        "เพิ่มเติมได้|ฝาแฝด|คำให้การ|คาดว่า|ย่าน|เดิน|ร่วมกับ|ผ่านทาง|การ|ยื้อ|โทร|ห้าม|คุย|ชัก|เกิดสำนึก|ห่างจาก|นายก|ฝ่ายกฎหมาย|กระเด็น|ขึ้น|เล่นเกม|อาชีพ|อยู่ภาย|หยุดนิ่ง|เพียงว่า|"
        "พลาดท่า|ถาม|เองก็|จะ|เมื่อ|ทั้ง|ทั้ง |นาย|แจ้ง|ก่อน|ถวาย|ทันที|อาศัย|ขอเวลา|กระทั่ง|ต้อง|จ่อยิง|ดมกาว|เลิกรา|ครูสอน|หากเข้า|รู้ตัว|รู้จัก|ร่วมเดิน|หญิงสาว|อยากบอก|ทำแผน|"
        "เขย|คู่เขย|สลบ|ใส่|บุตรชาย|บุตรสาว|นักศึกษา|ศพ|หึงหวง|เนื่อง|ล้านวิว|ตีนตุ๊กแก|สอบสวน|แถลง|เช่นกัน|เท่านั้น|รวมกับ|หน้าตา|หน้าห้อง|ทำหน้าที่|นัดแรก|ถ้า|มีเพื่อน|มีลักษณะ|จมน้ำ|ลักษณะ|เรื่องจะ|"
        "เหยื่อ|หัวหน้าแก๊ง|พ้นโทษ|ตลอด|มักจะ|สองสามีภรรยา|คู่บัดดี้|พลขับรถ|หนุ่ม|ป่วย|หาคน|สร้างความ|ประกัน|รองนายก|เอง|มอบ|มาช่วย|มาสัก|มานาน|มาบริเวณ|มาแสดง|มาสอบ|ชื่อเล่น|เล่นการพนัน|ตุ๋น|ราษฎร|"
        "นางสาว|รออยู่|มาประกอบ|ต่อพนักงาน|เเละจำเลย|วัย|ต่อศาล|มาดำ|หนึ่งใน|แน่นิ่ง|ฐานฆ่า|ปกติจะ|โกง|ทำให้|ยืนยัน|ตนเอง|สภาพศพ|มาประมาณ|มีคำสั่ง|ของทาง|อยู่กิน|รองศาสตราจารย์|รองสารวัตร"
        "|มีสีหน้า|ตำรวจ|เลิกงาน|เตะ|มาทำ|ซ้ำอีก|สังเกต|ต่อมา|มาขอ|มาจาก|หัวหน้าทีม|รวมมูลค่า|มาตั้ง|มาห่าง|ระแวง|ร้องไห้|มาหา|มารับ|มามอบ|มาก่อน|มาคุม|มาพัก|บุกรุก"
        "|นักธุรกิจ|มาอยู่|มาให้|มีอาชีพ|มาที่|มีประวัติ|มาแจ้ง|มากโดย|มาเจรจา)[ก-๙]{2,20}|ชาววัง|อาจหาญ|จะนู|กำลังรัมย์|พานิชอัตรา|มาสะอาด|กลับอินทร์|ไล่คง|ณ นคร|ณ อยุธยา|สุนทรกุล ณ ชลบุรี|สุคนธาภิรมย์ ณ พัทลุง|รัตนดิลก ณ ภูเก็ต|"
        "ณ กาฬสินธุ์|ณ จัมปาศักดิ์|ณ เชียงใหม่|ณ เชียงตุง|ณ ตะกั่วทุ่ง|ณ ถลาง|ณ น่าน|ณ บางช้าง|ณ ป้อมเพชร|ณ พัทลุง|ณ พิศณุโลก|ณ มโนรม|ณ มหาไชย|ณ ราชสีมา|"
        "ณ ร้อยเอ็จ|ณ ลำพูน|ณ วิเชียร|ณ วังขนาย|ณ สงขลา|ณ หนองคาย|ณ อุบล|โกมารกุล ณ นคร|พรหมสาขา ณ สกลนคร|ภวภูตานนท์ ณ มหาสารคาม|ประทีป ณ ถลาง))")

    regex_name1 = (
        r"((?!นายอำเภอ|นายแบบ|นายาว|ด.ต.ปืน|นายช่าง|นายทะเบียน|เด็กชายที่|นายกรัฐ|นายกองค์การ|ร.ต.ท.ผ่าน|นายกเทศมนตรี|นายกสภา"
        "|นายกแพทย|นายกเทศบาล|นายเก่า|นายสิบ|นายดาบ|นายพลนักสืบ|ด.ต.ยิง|นายมา|นายอย|นายทหาร|นายสถานี|นางเงือก|ทนายมาดำ|ทนายเข้า|นายเข้า|นางนกต่อ|พ.ต.ท.ซิ่งกระบะ|ทันตแพทย์ชื่อ|ทันตแพทย์หลง|"
        "นายมาดำ|นางแบบ|นายกต่อ|นายหนึ่งได้|นางเลิ้ง|นางงาม|นางนอน|นายจ้าง|นางรอง|นายทุน|นายกสมาคม|นายเป้เพื่อน|ร.ต.ท.วัย|นายเตรียม|ด.ต.นอก|ด.ต.ตาม|ร.ต.อ.เพื่อนสนิท|นายและเพื่อน|"
        "นายยก|ด.ต.หึงโหด|นายต่าง|นายทั่วประเทศ|นายพร้อมดูแล|นายแพทย์รวม|ทนายเผย|นายสิบทหาร|ด.ต.คู่|ด.ต.ดับ|ด.ต.โรงพัก|ด.ต.รายนี้|นางบวช"
        "|นายกฯ|นายช่วย|นายความ|นายทุน|นายพราน|นายตรวจ|นางเอก|นายรอง|นายหน้า|นายตำรวจ|ทนายความ|ดร\.หนุ่ม|ส\.ต\. มา|นายทิ้ง|นายกรัฐมนตรี|ทนายเปรมชัย|"
        "นายมีความ|นายไม่)(?<!<คน2>|เจ้า|เจ้ากรรม|ท|ทำ|สิบ|ร้อย|พัน|หมื่น|แสน|ล้าน|ทุก|อีก|ตำรวจ|ทหาร|หนึ่ง|สอง|สาม|สี่|รอง|นิ้ว|ผีสาง)(นาย|สมเด็จพระนาง|"
        "นาง|นางสาว|น\.ส\.|นพ\.|ส\.ต\.|ร\.ต\.อ\.|ร\.ต\.|ดร\.|ร\.อ\.|พ\.อ\.|จ\.ส\.ต\.|จ่าสิบตำรวจ|ส\.ต\.อ\.|สิบตำรวจเอก"
        "|ส\.ต\.ท\.|สิบตำรวจโท|ส\.ต\.ต\.|สิบตำรวจตรี|ด\.ต\.|แพทย์หญิง|พญ\.|ทันตแพทย์|ทพ\.|รองศาสตราจารย์|ผู้ช่วยศาสตราจารย์|"
        "พล\.อ\.ต\.|พลอากาศตรี|พล\.อ\.ท\.|พลอากาศโท|พล\.อ\.อ\.|พลอากาศเอก|พล\.อ\.|พลเอก|พล\.ท\.|พลโท|พลตรี|พล\.ต\.อ\.|พลตำรวจเอก|"
        "พลตำรวจโท|พล\.ต\.ท\.|พลตำรวจตรี|พล\.ต\.ต\.|พ\.ต\.อ\.|พันจ่าอากาศ|พันตำรวจเอก|พันตำรวจโท|พ\.ต\.ท\.|พันตำรวจตรี|พ\.ต\.ต\.|ร้อยตำรวจเอก|"
        "ร้อยตำรวจโท|ร\.ต\.ท\.|ร้อยตำรวจตรี|ร\.ต\.ต\.|พล\.ต\.|ส\.ต\.|เด็กชาย|ด\.ช\.|เด็กหญิง|ด\.ญ\.)(?!ได้ส่ง|บนรถ|ตัดใจ|จะพยายาม|หาย|จับ|มาเพราะ|เพื่อ|ขาย|ออก|ดู|ทั้ง|ผู้|ราย|อีก|"
        "อายุ|อย่าง|วัย|เป็น|คน|ตาย|มี|ดังกล่าว|ให้การ|มาก่อ|และ)([ก-๙]{2,30}(?=ไม่|ผู้|ถ่าย|และ|เป็น|ด้วย|หรือ|ที่|จึง|ทำร้าย|ไป|ได้|เปิด|ให้|มาพร้อม|ว่า|อีกที|ค้าง|พร้อม|ระบุ|ให้การ)|[ก-๙]{2,30})(\s((?!บนรถ|สารภาพ|พฤติกรรม|สัมภาษณ์|สัญชาติ|ก้มกราบ|คู่กรณี|น้องของ|พนักงาน|เกิดความ|เยาวชน|สะบัด|ดิ้น|ร่วมรัก|โมโห|"
        "ยังอยู่|หลานของ|หลานชาย|หลานสาว|ตัดสิน|พยายาม|ชาวบ้าน|ชาว|พี่|พ่อ|ลูก|ลูก|หลบ|อยู่ใน|เพื่อน|แม่|คิดตัด|กล่าว|ทำงาน|น่าจะ|ปล่อย|นามสมมุติ|ภายใน|ภายนอก|กระทำ|แสดงตัว|ดูแล|ม่าย|"
        "พร้อม|จาก|จับ|ห้อย|โดย|เพิ่ง|ปั่น|นั้น|สวม|ด้วย|เบื้อง|ถึง|เล่า|ฟัง|กำลัง|ทราบ|ถือ|เริ่ม|บอก|แล้ว|ยกมือ|อดีต|ลง|ติดเชื้อ|ตกใจ|ทำร้าย|ใช่|จำเลย|ตั้ง|แต่ง|อย่าง|ย้อน|ข้อหา|บ่าย|เช้า|กลางวัน|ดึก|"
        "ภรรยา|มารดา|ซึ่ง|ญาติ|ตื่น|นั่ง|บิดา|เสียชีวิต|ย้าย|ระบุ|วิ่ง|หรือ|สามี|อายุ|อ้าง|เข้า|เปิด|เป็น|เห็น|กับ|ขณะ|ขับ|ขี่|จึง|จู่|ตอบ|ถูก|ทาง|ที่|ผู้|พัก|ยอม|ยัง|รับ|รุม|บริเวณ|ถอด|รอดคดี|น้อง|น้องสาว|เสพยา|โยน|"
        "เซล้ม|กลัว|โทร|ทั้งหมด|ทั้งสอง|ปรากฏ|ล้ม|กระโดด|แฟน|ก่อเหตุ|มากนัก|ค้างค่า|ตรวจค้น|เบื้องต้น|ประกอบ|ส่วน|ฟ้อง|ยื่น|ฐานะ|ตาม|จำนวน|เกลี้ยกล่อม|ขัดขวาง|ซุกซ่อน|บาดเจ็บ|อยู่บ้าน|เพียงลำพัง|หลอก|"
        "ขัดขืน|ต่อสู้|หมดสติ|อำพราง|กบดาน|อาวุธ|ขโมย|ต่อย|ทิ่ม|ล้วง|ปะทะ|เล็ง|อุ้ม|ข่ม|ค้น|ฆ่า|ตัด|แทง|ฟาด|ล่า|นอน|ตบ|พก|เอเย่นต์|ทะเลาะ|ลูกเขย|ยืม|หลังก่อ|ซ้อน|อยู่ที่|อยู่อีก|อยู่นั้น|อยู่ตรง|อยู่แล้ว|"
        "ลุก|ส่ง|ออก|อาจ|อีก|เคย|เผย|เอา|จริง|หาย|แชท|แต่|และ|แอบ|เจ้า|มือ|เพื่อ|กลับ|ใช้|ให้|ได้|ไม่|ไล่|ไว้|ก็|คน|จน|จะได้|ทน|มานี่|มีอาการ|มีหมาย|ไป|ใน|พบ|พาไป|พากลับ|พามา|นำ|ว่า|ยิง|หนี|ประสานมา|ชก|"
        "เพิ่มเติมได้|ฝาแฝด|คำให้การ|คาดว่า|ย่าน|เดิน|ร่วมกับ|ผ่านทาง|การ|ยื้อ|โทร|ห้าม|คุย|ชัก|เกิดสำนึก|ห่างจาก|นายก|ฝ่ายกฎหมาย|กระเด็น|ขึ้น|เล่นเกม|อาชีพ|อยู่ภาย|หยุดนิ่ง|เพียงว่า|"
        "พลาดท่า|ถาม|เองก็|จะ|เมื่อ|ทั้ง|ทั้ง |นาย|แจ้ง|ก่อน|ถวาย|ทันที|อาศัย|ขอเวลา|กระทั่ง|ต้อง|จ่อยิง|ดมกาว|เลิกรา|ครูสอน|หากเข้า|รู้ตัว|รู้จัก|ร่วมเดิน|หญิงสาว|อยากบอก|ทำแผน|"
        "เขย|คู่เขย|สลบ|ใส่|บุตรชาย|บุตรสาว|นักศึกษา|ศพ|หึงหวง|เนื่อง|ล้านวิว|ตีนตุ๊กแก|สอบสวน|แถลง|เช่นกัน|เท่านั้น|รวมกับ|หน้าตา|หน้าห้อง|ทำหน้าที่|นัดแรก|ถ้า|มีเพื่อน|มีลักษณะ|จมน้ำ|ลักษณะ|เรื่องจะ|"
        "เหยื่อ|หัวหน้าแก๊ง|พ้นโทษ|ตลอด|มักจะ|สองสามีภรรยา|คู่บัดดี้|พลขับรถ|หนุ่ม|ป่วย|หาคน|สะพาย|สร้างความ|ประกัน|รองนายก|เอง|มอบ|มาช่วย|มาสัก|มานาน|มาบริเวณ|มาแสดง|มาสอบ|ชื่อเล่น|เล่นการพนัน|ตุ๋น|ราษฎร|"
        "นางสาว|รออยู่|มาประกอบ|ต่อพนักงาน|เเละจำเลย|วัย|ต่อศาล|มาดำ|หนึ่งใน|แน่นิ่ง|ฐานฆ่า|ปกติจะ|โกง|ทำให้|ยืนยัน|ตนเอง|สภาพศพ|มาประมาณ|มีคำสั่ง|ของทาง|อยู่กิน|รองศาสตราจารย์|รองสารวัตร"
        "|มีสีหน้า|ตำรวจ|เลิกงาน|เตะ|มาทำ|ซ้ำอีก|สังเกต|ต่อมา|มาขอ|มาจาก|หัวหน้าทีม|รวมมูลค่า|มาตั้ง|รักกัน|มาห่าง|ระแวง|ร้องไห้|มาหา|มารับ|มามอบ|มาก่อน|มาคุม|มาพัก|บุกรุก|นักธุรกิจ|มาอยู่|มาให้|"
        "มีอาชีพ|มาที่|มีประวัติ|สภาพจิต|มาแจ้ง|มากโดย|เจอที่|มาเจรจา|ลวนลาม)[ก-๙]{2,25}\s|[ก-๙]{2,25}\,|[ก-๙]{2,25}\”|ชาววัง|อาจหาญ|จะนู|กำลังรัมย์|พานิชอัตรา|มาสะอาด|กลับอินทร์|ไล่คง|ณ นคร|ณ อยุธยา|สุนทรกุล ณ ชลบุรี|สุคนธาภิรมย์ ณ พัทลุง|รัตนดิลก ณ ภูเก็ต|"
        "ณ กาฬสินธุ์|ณ จัมปาศักดิ์|ณ เชียงใหม่|ณ เชียงตุง|ณ ตะกั่วทุ่ง|ณ ถลาง|ณ น่าน|ณ บางช้าง|ณ ป้อมเพชร|ณ พัทลุง|ณ พิศณุโลก|ณ มโนรม|ณ มหาไชย|ณ ราชสีมา|"
        "ณ ร้อยเอ็จ|ณ ลำพูน|ณ วิเชียร|ณ วังขนาย|ณ สงขลา|ณ หนองคาย|ณ อุบล|โกมารกุล ณ นคร|พรหมสาขา ณ สกลนคร|ภวภูตานนท์ ณ มหาสารคาม|ประทีป ณ ถลาง))?|นางมีนา)")

    matches_name = regex.sub(regex_name, r'<คน2>\1</คน2>', read_text)
    read_text = matches_name
    matches_name1 = regex.sub(regex_name1, r'<คน>\1</คน>', read_text)
    read_text2 = matches_name1

    regex_name = (
        r"<คน>((?!นายอำเภอ|นายแบบ|นายาว|ด.ต.ปืน|นายช่าง|นายทะเบียน|เด็กชายที่|นายกรัฐ|นายกองค์การ|ร.ต.ท.ผ่าน|นายกเทศมนตรี|นายกสภา"
        "|นายกแพทย|นายกเทศบาล|นายเก่า|นายสิบ|นายดาบ|นายพลนักสืบ|ด.ต.ยิง|นายมา|นายอย|นายทหาร|นายสถานี|นางเงือก|ทนายมาดำ|ทนายเข้า|นายเข้า|นางนกต่อ|พ.ต.ท.ซิ่งกระบะ|ทันตแพทย์ชื่อ|ทันตแพทย์หลง|"
        "นายมาดำ|นางแบบ|นายกต่อ|นายหนึ่งได้|นางเลิ้ง|นางงาม|นางนอน|นายจ้าง|นางรอง|นายทุน|นายกสมาคม|นายเป้เพื่อน|ร.ต.ท.วัย|นายเตรียม|ด.ต.นอก|ด.ต.ตาม|ร.ต.อ.เพื่อนสนิท|นายและเพื่อน|"
        "นายยก|ด.ต.หึงโหด|นายต่าง|นายทั่วประเทศ|นายพร้อมดูแล|นายแพทย์รวม|ทนายเผย|นายสิบทหาร|ด.ต.คู่|ด.ต.ดับ|ด.ต.โรงพัก|ด.ต.รายนี้|นางบวช"
        "|นายกฯ|นายช่วย|นายความ|นายทุน|นายพราน|นายตรวจ|นางเอก|นายรอง|นายหน้า|นายตำรวจ|ทนายความ|ดร\.หนุ่ม|ส\.ต\. มา|นายทิ้ง|นายกรัฐมนตรี|ทนายเปรมชัย|"
        "นายมีความ|นายไม่)(?<!<คน2>|เจ้า|เจ้ากรรม|ท|ทำ|สิบ|ร้อย|พัน|หมื่น|แสน|ล้าน|ทุก|อีก|ตำรวจ|ทหาร|หนึ่ง|สอง|สาม|สี่|รอง|นิ้ว|ผีสาง)(นาย|สมเด็จพระนาง|"
        "นาง|นางสาว|น\.ส\.|นพ\.|ส\.ต\.|ร\.ต\.อ\.|ร\.ต\.|ดร\.|ร\.อ\.|พ\.อ\.|จ\.ส\.ต\.|จ่าสิบตำรวจ|ส\.ต\.อ\.|สิบตำรวจเอก"
        "|ส\.ต\.ท\.|สิบตำรวจโท|ส\.ต\.ต\.|สิบตำรวจตรี|ด\.ต\.|แพทย์หญิง|พญ\.|ทันตแพทย์|ทพ\.|รองศาสตราจารย์|ผู้ช่วยศาสตราจารย์|"
        "พล\.อ\.ต\.|พลอากาศตรี|พล\.อ\.ท\.|พลอากาศโท|พล\.อ\.อ\.|พลอากาศเอก|พล\.อ\.|พลเอก|พล\.ท\.|พลโท|พลตรี|พล\.ต\.อ\.|พลตำรวจเอก|"
        "พลตำรวจโท|พล\.ต\.ท\.|พลตำรวจตรี|พล\.ต\.ต\.|พ\.ต\.อ\.|พันจ่าอากาศ|พันตำรวจเอก|พันตำรวจโท|พ\.ต\.ท\.|พันตำรวจตรี|พ\.ต\.ต\.|ร้อยตำรวจเอก|"
        "ร้อยตำรวจโท|ร\.ต\.ท\.|ร้อยตำรวจตรี|ร\.ต\.ต\.|พล\.ต\.|ส\.ต\.|เด็กชาย|ด\.ช\.|เด็กหญิง|ด\.ญ\.)(?!จะพยายาม|หาย|จับ|มาเพราะ|เพื่อ|ขาย|ออก|ดู|ทั้ง|ผู้|ราย|อีก|"
        "อายุ|อย่าง|วัย|เป็น|คน|ตาย|มี|ดังกล่าว|ให้การ|มาก่อ|และ)([ก-๙]{2,30}(?=ไม่|ผู้|ถ่าย|และ|เป็น|ด้วย|หรือ|ที่|จึง|ทำร้าย|ไป|ได้|เปิด|ให้|มาพร้อม|ว่า|อีกที|ค้าง|พร้อม|ระบุ|ให้การ)|[ก-๙]{2,30})(\s((?!สารภาพ|พฤติกรรม|สัมภาษณ์|สัญชาติ|ก้มกราบ|คู่กรณี|น้องของ|พนักงาน|เกิดความ|เยาวชน|สะบัด|ดิ้น|ร่วมรัก|โมโห|"
        "ยังอยู่|หลานของ|หลานชาย|หลานสาว|ตัดสิน|พยายาม|ชาวบ้าน|ชาว|พี่|พ่อ|ลูก|ลูก|หลบ|อยู่ใน|เพื่อน|แม่|คิดตัด|กล่าว|ทำงาน|น่าจะ|ปล่อย|นามสมมุติ|ภายใน|ภายนอก|กระทำ|แสดงตัว|ดูแล|ม่าย|"
        "พร้อม|จาก|จับ|ห้อย|โดย|เพิ่ง|ปั่น|นั้น|สวม|ด้วย|เบื้อง|ถึง|เล่า|ฟัง|กำลัง|ทราบ|ถือ|เริ่ม|บอก|แล้ว|ยกมือ|อดีต|ลง|ติดเชื้อ|ตกใจ|ทำร้าย|ใช่|จำเลย|ตั้ง|แต่ง|อย่าง|ย้อน|ข้อหา|บ่าย|เช้า|กลางวัน|ดึก|"
        "ภรรยา|มารดา|ซึ่ง|ญาติ|ตื่น|นั่ง|บิดา|เสียชีวิต|ย้าย|ระบุ|วิ่ง|หรือ|สามี|อายุ|อ้าง|เข้า|เปิด|เป็น|เห็น|กับ|ขณะ|ขับ|ขี่|จึง|จู่|ตอบ|ถูก|ทาง|ที่|ผู้|พัก|ยอม|ยัง|รับ|รุม|บริเวณ|ถอด|รอดคดี|น้อง|น้องสาว|เสพยา|โยน|"
        "เซล้ม|กลัว|โทร|ทั้งหมด|ทั้งสอง|ปรากฏ|ล้ม|กระโดด|แฟน|ก่อเหตุ|มากนัก|ค้างค่า|ตรวจค้น|เบื้องต้น|ประกอบ|ส่วน|ฟ้อง|ยื่น|ฐานะ|ตาม|จำนวน|เกลี้ยกล่อม|ขัดขวาง|ซุกซ่อน|บาดเจ็บ|อยู่บ้าน|เพียงลำพัง|หลอก|"
        "ขัดขืน|ต่อสู้|หมดสติ|อำพราง|กบดาน|อาวุธ|ขโมย|ต่อย|ทิ่ม|ล้วง|ปะทะ|เล็ง|อุ้ม|ข่ม|ค้น|ฆ่า|ตัด|แทง|ฟาด|ล่า|นอน|ตบ|พก|เอเย่นต์|ทะเลาะ|ลูกเขย|ยืม|หลังก่อ|ซ้อน|อยู่ที่|อยู่อีก|อยู่นั้น|อยู่ตรง|อยู่แล้ว|"
        "ลุก|ส่ง|ออก|อาจ|อีก|เคย|เผย|เอา|จริง|หาย|แชท|แต่|และ|แอบ|เจ้า|มือ|เพื่อ|กลับ|ใช้|ให้|ได้|ไม่|ไล่|ไว้|ก็|คน|จน|จะได้|ทน|มานี่|มีอาการ|มีหมาย|ไป|ใน|พบ|พาไป|พากลับ|พามา|นำ|ว่า|ยิง|หนี|ประสานมา|ชก|"
        "เพิ่มเติมได้|ฝาแฝด|คำให้การ|คาดว่า|ย่าน|เดิน|ร่วมกับ|ผ่านทาง|การ|ยื้อ|โทร|ห้าม|คุย|ชัก|เกิดสำนึก|ห่างจาก|นายก|ฝ่ายกฎหมาย|กระเด็น|ขึ้น|เล่นเกม|อาชีพ|อยู่ภาย|หยุดนิ่ง|เพียงว่า|"
        "พลาดท่า|ถาม|เองก็|จะ|เมื่อ|ทั้ง|ทั้ง |นาย|แจ้ง|ก่อน|ถวาย|ทันที|อาศัย|ขอเวลา|กระทั่ง|ต้อง|จ่อยิง|ดมกาว|เลิกรา|ครูสอน|หากเข้า|รู้ตัว|รู้จัก|ร่วมเดิน|หญิงสาว|อยากบอก|ทำแผน|"
        "เขย|คู่เขย|สลบ|ใส่|บุตรชาย|บุตรสาว|นักศึกษา|ศพ|หึงหวง|เนื่อง|ล้านวิว|ตีนตุ๊กแก|สอบสวน|แถลง|เช่นกัน|เท่านั้น|รวมกับ|หน้าตา|หน้าห้อง|ทำหน้าที่|นัดแรก|ถ้า|มีเพื่อน|มีลักษณะ|จมน้ำ|ลักษณะ|เรื่องจะ|"
        "เหยื่อ|หัวหน้าแก๊ง|พ้นโทษ|ตลอด|มักจะ|สองสามีภรรยา|คู่บัดดี้|พลขับรถ|หนุ่ม|ป่วย|หาคน|สะพาย|สร้างความ|ประกัน|รองนายก|เอง|มอบ|มาช่วย|มาสัก|มานาน|มาบริเวณ|มาแสดง|มาสอบ|ชื่อเล่น|เล่นการพนัน|ตุ๋น|ราษฎร|"
        "นางสาว|รออยู่|มาประกอบ|ต่อพนักงาน|เเละจำเลย|วัย|ต่อศาล|มาดำ|หนึ่งใน|แน่นิ่ง|ฐานฆ่า|ปกติจะ|โกง|ทำให้|ยืนยัน|ตนเอง|สภาพศพ|มาประมาณ|มีคำสั่ง|ของทาง|อยู่กิน|รองศาสตราจารย์|รองสารวัตร"
        "|มีสีหน้า|ตำรวจ|เลิกงาน|เตะ|มาทำ|ซ้ำอีก|สังเกต|ต่อมา|มาขอ|มาจาก|หัวหน้าทีม|รวมมูลค่า|มาตั้ง|รักกัน|มาห่าง|ระแวง|ร้องไห้|มาหา|มารับ|มามอบ|มาก่อน|มาคุม|มาพัก|บุกรุก|นักธุรกิจ|มาอยู่|มาให้|"
        "มีอาชีพ|มาที่|มีประวัติ|สภาพจิต|มาแจ้ง|มากโดย|มาเจรจา|ลวนลาม)[ก-๙]{2,25}\s|[ก-๙]{2,25}\,|[ก-๙]{2,25}\”|ชาววัง|อาจหาญ|จะนู|กำลังรัมย์|พานิชอัตรา|มาสะอาด|กลับอินทร์|ไล่คง|ณ นคร|ณ อยุธยา|สุนทรกุล ณ ชลบุรี|สุคนธาภิรมย์ ณ พัทลุง|รัตนดิลก ณ ภูเก็ต|"
        "ณ กาฬสินธุ์|ณ จัมปาศักดิ์|ณ เชียงใหม่|ณ เชียงตุง|ณ ตะกั่วทุ่ง|ณ ถลาง|ณ น่าน|ณ บางช้าง|ณ ป้อมเพชร|ณ พัทลุง|ณ พิศณุโลก|ณ มโนรม|ณ มหาไชย|ณ ราชสีมา|"
        "ณ ร้อยเอ็จ|ณ ลำพูน|ณ วิเชียร|ณ วังขนาย|ณ สงขลา|ณ หนองคาย|ณ อุบล|โกมารกุล ณ นคร|พรหมสาขา ณ สกลนคร|ภวภูตานนท์ ณ มหาสารคาม|ประทีป ณ ถลาง))?|(นางมีนา))</คน>")

    matches_name = regex.finditer(regex_name, read_text2, re.MULTILINE)
    count = 0
    for matchNum, match in enumerate(matches_name):
        count += 0

    def wrong_word_name(read_text2):
        """
        sub function in def tag_person
        :param read_text2:
        :return:
        """
        read_text2 = regex.finditer(r"<คน>([^<]*)</คน>", read_text2)

        list_name = []
        for matchNum, match in enumerate(read_text2):
            list_name.append(match.group(1))

        return list_name

    list_name = wrong_word_name(read_text2)

    arr = np.asarray(list_name)

    arr = np.unique(arr)

    list_name = arr.tolist()

    list_name2 = []

    for i in range(len(list_name)):
        list_name2.append(list_name[i].split(' '))

    index_reiteration = []
    for i in range(len(list_name2)):
        for j in range(len(list_name2[i])):
            for k in range(len(list_name2)):
                for l in range(len(list_name2[k])):
                    if j == 0 and l == 0:
                        # print(i,j,k,l)
                        if k != len(list_name2) - 1:
                            if list_name2[i][j][:len(list_name2[i][j])] == list_name2[k + 1][l][:len(list_name2[i][j])]:
                                if len(list_name2[i][j]) < len(list_name2[k + 1][l]):
                                    index_reiteration.append(k + 1)
                                    # print(k+1)

    index_re = np.asarray(index_reiteration)
    index_re = np.unique(index_re)
    index_reiteration = index_re.tolist()

    list_person1 = []
    j = 0
    for i in range(len(list_name2)):
        if j < len(index_reiteration):
            if i != index_reiteration[j]:
                list_person1.append(list_name2[i])
            else:
                j += 1
        else:
            list_person1.append(list_name2[i])

    # add firstname when firstname have word more than word follow long
    list_person2 = []
    count = 0
    for i in range(len(list_person1)):
        check_index = False
        check_person = False
        index_i = i

        while (check_index != True):

            if list_person1[i][0] == list_person1[index_i][0] and i != index_i:
                check_person = True

            if index_i == len(list_person1) - 1:
                check_index = True
            else:
                index_i += 1

        if check_person == False and len(list_person1[i]) > 1:
            list_person2.append([])
            list_person2[count].append(list_person1[i][0])
            count += 1
    # end
    # add list_person2 in list_person1
    list_person1.extend(list_person2)
    # end
    list_name2 = []
    for i in list_person1:
        count += 1
        list_name2.append(" ".join(i))

    list_name2.sort(reverse=True)
    str_name = '|'.join(list_name2)

    # add tag person
    regex_name = (
        r'(คนร้าย|กำนัน|คนเสียหาย|ผู้ร้าย|ผู้ต้องหา|ผู้ก่อเหตุ|ผู้เสียหาย|ผู้ตาย|ผู้เสียชีวิต|โจรใต้|โจร|เด็กหญิง)')
    read_text = regex.sub(regex_name, r'<คน>\1</คน>', read_text)
    # end
    if str_name != '':
        regex_name2 = (r"((?<!<คน2>)(" + str_name + "))")
        matches_name2 = regex.sub(regex_name2, r'<คน>\1</คน>', read_text)
        read_text = matches_name2

    return read_text


def tag_adverb(read_text):
    """
    tag <คำบ่งบอก> text </คำบ่งบอก> into a adverb
    :param read_text:
    :return: <คำบ่งบอก> </คำบ่งบอก>
    """
    regex_specify1 = (r"((หลังถูก|(?<!ราคา)ถูก(?!ล็อก)|โดน))")
    regex_specify2 = (
        r"((?!เป็นอย่าง|เป็นต้น|เป็นช่วง|เป็นอยู่|เป็นไป|เป็นกอง|เป็นประจำ|เป็นปกติ|เป็นเสียง|เป็นกอบ|เป็นทาง|เป็นกำ|เป็นแบบ|เป็นเรื่อง|เป็นแนว|เป็นที่|เป็นระยะ|เป็นจังหวะ|เป็นสิทธิ์|เป็นหุ้น|เป็นหน้า|เป็นฐาน|เป็นการ)(คือ|(?<!จำ|อยู่|แล้ว|อาจ|ให้|ความ|มา|อย่าง|เคย|กลาย|ว่า|ดูแล|ได้|ไม่|อัน|นั้น)เป็น))")

    matches_specify1 = regex.sub(regex_specify1, r'<คำบ่งบอก>\1</คำบ่งบอก>', read_text)
    read_text = matches_specify1
    matches_specify2 = regex.sub(regex_specify2, r'<คำบ่งบอก2>\1</คำบ่งบอก2>', read_text)
    read_text = matches_specify2
    return read_text
