# https://www.babelcoder.com/blog/posts/python-classes-and-objects
# https://www.tutorialspoint.com/python/python_classes_objects.htm
# https://www.tutorialspoint.com/python/
class Person:
    PersonCount = 0

    # status = 'คน'

    def __init__(self, firstname, lastname='', status='คน'):
        self.firstname = firstname
        self.lastname = lastname

        if (firstname == 'คนร้าย' or firstname == 'ผู้ร้าย' or firstname == 'ผู้ต้องหา'
                or firstname == 'ผู้ก่อเหตุ' or firstname == 'โจรใต้' or firstname == 'โจร'):
            self.status = 'คนร้าย'
        elif (firstname == 'ผู้เสียหาย' or firstname == 'ผู้ตาย' or firstname == 'ผู้เสียชีวิต'):
            self.status = 'คนเสียหาย'
        else:
            self.status = status

        Person.PersonCount += 1

    def __str__(self):
        return 'คน'

    @property
    def status(self):  # getter
        return self.__status

    @status.setter
    def status(self, status):  # setter
        if status in ['คนร้าย', 'คน', 'คนเสียหาย', 'เจ้าหน้าที่']:
            if self.firstname == 'คนร้าย':
                self.__status = 'คนร้าย'
            else:
                self.__status = status
        else:
            raise ValueError('ไม่มีสถานะคนในเซตข้อมูล')


class Action:

    def __init__(self, name_action, number_action):
        self.number_action = number_action
        self.name_action = name_action

    def __str__(self):
        # return 'กระทำ'+self.number_action
        return self.number_action


class Verb:

    def __init__(self, name_verb, number=0):
        self.number = number
        self.name_verb = name_verb

    def __str__(self):
        if self.number == 0:
            return 'คำบ่งบอก'
        else:
            return 'คำบ่งบอก' + self.number


class Date:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return 'วัน'


class Time:

    def __init__(self, time):
        self.time = time

    def __str__(self):
        return 'เวลา'


class Location:

    def __init__(self, country='', province='', amphoe='', area=''
                 , tambon='', district='', road='', river='', place='', mall=''
                 , hospital='', university=''):
        self.country = country
        self.province = province
        self.amphoe = amphoe
        self.area = area
        self.tambon = tambon
        self.district = district
        self.road = road
        self.river = river
        self.place = place
        self.mall = mall
        self.hospital = hospital
        self.university = university

    def __str__(self):
        return 'สถานที่'
