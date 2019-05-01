# alpha_project
โปรเจคนี้อยู่ขั้นตอนการพัฒนา 

## ความสามารถ ณ ตอนนี้คือ ##
1. ค้นพบบุคคล สถานที่ วัน เวลาจากข่าวอาชญากรรม 

## อธิบายเเต่ละ module ##
1. main.py 
  ไฟล์นี้คือ ไฟล์ที่ไว้รันฟังก์ชั่นทั้งหมดที่เขียนขึ้น 
2. word_tokenize.py
  ไฟล์นี้เเยกเป็น method ตามนี้ 
  * run 
    คือ method ที่เอาไว้ใช้รัน function ทั้งหมด 
  * get_news
    คือ method ดึงค่ามาจากเว็บไซต์ข่าว thairath 
  * word_segment
    คือ method ตัดคำ
  * word_segment_identify_tag 
    คือ method ถ้าเจอ <tag> text </tag> มองข้ามไป คือไม่ตัดคำที่อยู่ใน tag  
