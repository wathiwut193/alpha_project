import codecs


# export result news
def export_text(data_text, n_news):
    name = 'D:/58160702/alpha_export/output_tag/' + n_news + '/news_' + n_news + '_tag.txt'
    write_file = codecs.open(name, 'w+', 'utf8')
    write_file.write(''.join(data_text))
    write_file.close()


def export_obj(result_rule, n_news):
    write_file = codecs.open('D:/58160702/alpha_export/output_obj_tag/' + n_news + '/' + n_news + '.txt', 'w+', 'utf8')
    for i in range(len(result_rule)):
        write_file.write('_____________________________' + str(i + 1) + '_____________________________')
        write_file.write('\n')
        # print('-----------------',i+1,'-----------------')
        for j in range(len(result_rule[i])):
            if str(result_rule[i][j]) == 'คน':
                write_file.write(
                    str(i + 1) + ' ' + str(j + 1) + ' ' + result_rule[i][j].status + ':' + result_rule[i][j].firstname +
                    result_rule[i][j].lastname)
                write_file.write('\n')
                # print(i+1,j,result_rule[i][j].status ,':', result_rule[i][j].firstname , result_rule[i][j].lastname)
            elif (str(result_rule[i][j]) == 'กระทำ1' or str(result_rule[i][j]) == 'กระทำ2'
                  or str(result_rule[i][j]) == 'กระทำ3' or str(result_rule[i][j]) == 'กระทำ4'
                  or str(result_rule[i][j]) == 'กระทำ5' or str(result_rule[i][j]) == 'กระทำ6'
                  or str(result_rule[i][j]) == 'กระทำ7' or str(result_rule[i][j]) == 'กระทำ8'
                  or str(result_rule[i][j]) == 'กระทำรอง1'):
                write_file.write(
                    str(i + 1) + ' ' + str(j + 1) + ' ' + str(result_rule[i][j]) + ':' + result_rule[i][j].name_action)
                write_file.write('\n')
                # print(i+1,j,str(result_rule[i][j]),':',result_rule[i][j].name_action)

            elif (str(result_rule[i][j]) == 'คำบ่งบอก' or str(result_rule[i][j]) == 'คำบ่งบอก2'
                  or str(result_rule[i][j]) == 'คำบ่งบอก3' or str(result_rule[i][j]) == 'คำบ่งบอก4'):
                write_file.write(
                    str(i + 1) + ' ' + str(j + 1) + ' ' + str(result_rule[i][j]) + ':' + result_rule[i][j].name_verb)
                write_file.write('\n')
                # print(i+1,j,str(result_rule[i][j]),':',result_rule[i][j].name_verb)

            elif str(result_rule[i][j]) == 'สถานที่':
                write_file.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(result_rule[i][j]) + ':' + str(
                    result_rule[i][j].split_location))
                write_file.write('\n')
                # print(i+1,j,str(result_rule[i][j]),':',result_rule[i][j].split_location)

            elif str(result_rule[i][j]) == 'วัน':
                write_file.write(
                    str(i + 1) + ' ' + str(j + 1) + ' ' + str(result_rule[i][j]) + ':' + result_rule[i][j].date)
                write_file.write('\n')
                # print(i+1,j,str(result_rule[i][j]),':',result_rule[i][j].date)

            elif str(result_rule[i][j]) == 'เวลา':
                write_file.write(
                    str(i + 1) + ' ' + str(j + 1) + ' ' + str(result_rule[i][j]) + ':' + result_rule[i][j].time)
                write_file.write('\n')
                # print(i+1,j,str(result_rule[i][j]),':',result_rule[i][j].time)

        write_file.write('___________________________________________________________')
        write_file.write('\n')

    write_file.close()


def export_rule(result_rule, number_rule, number_news, name_type):
    if number_rule == 1:
        name = 'news_' + number_news + '_result_' + name_type + 'rule1.txt'
        title = '1.→  คน (ร้าย) + กระทำ (ผิด)*'
    elif number_rule == 2:
        name = 'news_' + number_news + '_result_rule2.txt'
        title = '2.→  คน (ร้าย)* + กระทำ (ผิด)* + คน (เสียหาย)*'
    elif number_rule == 3:
        name = 'news_' + number_news + '_result_rule3.txt'
        title = '3.→  คน (เสียหาย)* + คำ (บ่งบอกว่าถูกกระทำ) + กระทำ (ผิด) +- คน (ร้าย)'
    elif number_rule == 4:
        name = 'news_' + number_news + '_result_rule4.txt'
        title = '4.→ คน(เสียหาย) + คำ (บ่งบอกว่าถูกกระทำ) + คน(ร้าย) + กระทำ(ผิด)'
    elif number_rule == 5:
        name = 'news_' + number_news + '_result_rule5.txt'
        title = '5.→ คน (เจ้าหน้าที่)* + กระทำ3* +- คน (ร้าย)'
    elif number_rule == 6:
        name = 'news_' + number_news + '_result_rule6.txt'
        title = '6.→ คน (เจ้าหน้าที่) + กระทำ + คน (เสียหาย)* + กระทำ'
    elif number_rule == 7:
        name = 'news_' + number_news + '_result_rule7.txt'
        title = '7.→ คน (เสียหาย)* + กระทำ + คน (เจ้าหน้าที่)***'
    elif number_rule == 8:
        name = 'news_' + number_news + '_result_rule8.txt'
        title = '8.→ คน (ร้าย) + กระทำ + คน (เจ้าหน้าที่)***'
    elif number_rule == 9:
        name = 'news_' + number_news + '_result_rule9.txt'
        title = '9.→ คน (ร้าย) + คำ (บ่งบอกว่าถูกกระทำ) +- เจ้าหน้าที่ + กระทำ'
    elif number_rule == 10:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '10.→ คน (เสียหาย) + กระทำ*  + เกริ่น 3 +- คน (ร้าย)'
    elif number_rule == 11:
        name = 'news_' + number_news + '_result_rule11.txt'
        title = '11.→ คน (ร้าย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 11.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (ร้าย)'
    elif number_rule == 12:
        name = 'news_' + number_news + '_result_rule12.txt'
        title = '12.→ คน (เสียหาย) + คำ (กริยาเติมเต็ม) + คน (ชื่อ) OR 12.→ คน (ชื่อ) + คำ (กริยาเติมเต็ม) + คน (เสียหาย)'
    elif number_rule == 13:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '13.→ กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)'
    elif number_rule == 14:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '14.→ คน (ร้าย)* + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)'
    elif number_rule == 15:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '15.→ กระทำ (ผิด) + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)'
    elif number_rule == 16:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '16.→ กระทำ (ผิด) + คน + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) + สถานที่ (เกิดเหตุ)'
    elif number_rule == 17:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '17.→ คน + คำกริยา + คำ (บ่งบอกว่าเป็นที่เกิดเหตุ) +- กระทำ (ผิด) + สถานที่ (เกิดเหตุ)'
    elif number_rule == 18:
        name = 'news_' + number_news + '_result_rule10.txt'
        title = '18.→ เวลา + กระทำ (ผิด)* + สถานที่ (เกิดเหตุ)'

    if result_rule != 'Empty':
        write_file = codecs.open('D:/58160702/alpha_export/result_by_rule/' + number_news + '/' + name, 'w+', 'utf8')
        write_file.write(''.join(title))
        write_file.write('\n')

        # for i in range(len(list_text2)):
        #    write_file.write('___________________________________________________________________________________________')
        #    write_file.write('\n')
        #    write_file.write(' '.join(list_text2[i]))
        #    write_file.write('\n')

        # write_file.write('___________________________________________________________________________________________')
        # write_file.close()

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
                write_file.write('__________________________________________________________________________________')
                write_file.write('\n')
                write_file.write(p + ': ' + str(index))
                write_file.write('\n')
                # print('-----------------------------------')
                for k in range(len(result_rule[i][j])):
                    if str(result_rule[i][j][k]) == 'คน':
                        # write_file.write(result_rule[i][j][k].status +':'+ result_rule[i][j][k].firstname + result_rule[i][j][k].lastname)
                        write_file.write(
                            result_rule[i][j][k].firstname + result_rule[i][j][k].lastname + ' (' + result_rule[i][j][
                                k].status + ') + ')
                        # write_file.write('\n')
                        # print(result_rule[i][j][k].status ,':', result_rule[i][j][k].firstname , result_rule[i][j][k].lastname)
                    elif (str(result_rule[i][j][k]) == 'กระทำ1' or str(result_rule[i][j][k]) == 'กระทำ2'
                          or str(result_rule[i][j][k]) == 'กระทำ3' or str(result_rule[i][j][k]) == 'กระทำ4'
                          or str(result_rule[i][j][k]) == 'กระทำ5' or str(result_rule[i][j][k]) == 'กระทำ6'
                          or str(result_rule[i][j][k]) == 'กระทำ7' or str(result_rule[i][j][k]) == 'กระทำ8'):
                        # write_file.write(str(result_rule[i][j][k])+':'+result_rule[i][j][k].name_action)
                        write_file.write(result_rule[i][j][k].name_action + ' (' + str(result_rule[i][j][k]) + ')')
                        write_file.write('\n')
                        # print(str(result_rule[i][j][k]),':',result_rule[i][j][k].name_action)
                    elif (str(result_rule[i][j][k]) == 'คำบ่งบอก' or str(result_rule[i][j][k]) == 'คำบ่งบอก2'
                          or str(result_rule[i][j][k]) == 'คำบ่งบอก3' or str(result_rule[i][j][k]) == 'คำบ่งบอก4'):
                        write_file.write(str(result_rule[i][j][k]) + ':' + result_rule[i][j][k].name_verb)
                        write_file.write('\n')
                        # print(str(result_rule[i][j][k]),':',result_rule[i][j][k].name_verb)
                    elif str(result_rule[i][j][k]) == 'สถานที่':
                        write_file.write(str(result_rule[i][j][k]) + ':' + str(result_rule[i][j][k].split_location))
                        write_file.write('\n')
                        # print('L',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].split_location)
                    elif str(result_rule[i][j][k]) == 'วัน':
                        write_file.write(str(result_rule[i][j][k]) + ':' + result_rule[i][j][k].date)
                        # print('T',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].date)
                    elif str(result_rule[i][j][k]) == 'เวลา':
                        write_file.write(str(result_rule[i][j][k]) + ':' + result_rule[i][j][k].time)
                        # print('D',i+1,'|',str(result_rule[i][j][k]),':',result_rule[i][j][k].time)

        write_file.write('__________________________________________________________________________________')
        write_file.close()