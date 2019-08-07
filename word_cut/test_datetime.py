import deepcut
import re

read_data_time1 = '09:22 น.'
read_data_time2 = '16:47 น.'
read_data_time3 = '09.22 น.'
read_data_time4 = '16.47 น.'
read_data_time5 = '09:22 นาฬิกา'
read_data_time6 = '16:47 นาฬิกา'
read_data_time7 = '09.22 นาฬิกา'
read_data_time8 = '16.47 นาฬิกา'

corpus = 'corpus/compond_word.txt'

word_cut1 = deepcut.tokenize(read_data_time1, custom_dict=corpus)
word_cut2 = deepcut.tokenize(read_data_time2, custom_dict=corpus)
word_cut3 = deepcut.tokenize(read_data_time3, custom_dict=corpus)
word_cut4 = deepcut.tokenize(read_data_time4, custom_dict=corpus)
word_cut5 = deepcut.tokenize(read_data_time5, custom_dict=corpus)
word_cut6 = deepcut.tokenize(read_data_time6, custom_dict=corpus)
word_cut7 = deepcut.tokenize(read_data_time7, custom_dict=corpus)
word_cut8 = deepcut.tokenize(read_data_time8, custom_dict=corpus)
"""
print(word_cut1)
print(word_cut2)
print(word_cut3)
print(word_cut4)
print(word_cut5)
print(word_cut6)
print(word_cut7)
print(word_cut8)
"""
read_text = ('ผหกฟหก ช่วงเช้า ฟหกฟหกฟหก\n'
    'ช่วงบ่าย ช่วงค่ำ ช่วงดึก 09:00 น. ตอนเช้า')

regex_time = r"([0-1][\d]|[2][0-4])\s?(:|.)([0-5][\d])\s?(นาฬิกา|น.|น)|(ช่วง|ตอน)(เช้า|ค่ำ|เย็น|ดึก|บ่าย|สาย)"
matches_time = re.finditer(regex_time, read_text, re.MULTILINE)
for matchNum, match in enumerate(matches_time):
    #count += 1
    if match.group() == 'ช่วงเช้า' or match.group() == 'ตอนเช้า':
        print('เวลา : 06:00 น. - 09:00 น.')
    elif match.group() == 'ช่วงบ่าย' or match.group() == 'ตอนบ่าย':
        print('เวลา : 13:00 น. - 15:00 น.')
    elif match.group() == 'ช่วงเย็น' or match.group() == 'ตอนเย็น':
        print('เวลา : 17:00 น. - 18:00 น.')
    elif match.group() == 'ช่วงค่ำ' or match.group() == 'ตอนค่ำ':
        print('เวลา : 19:00 น. - 20:00 น.')
    elif match.group() == 'ช่วงดึก' or match.group() == 'ตอนดึก':
        print('เวลา : 23:00 น. - 03:00 น.')
    else:
        print (str('เวลา : ')+match.group())