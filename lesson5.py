import codecs
import json #подключили библиотеку для работы с json
from pprint import pprint #подключили Pprint для красоты выдачи текста
from bs4 import BeautifulSoup

def sort_key(e):#Сортировка лябда
    return e[1]
def collects_an_archive(line):#Заполняем архив
   a = line.split()
   for word in a:
      coincidence=0
      for letter in archive_colektion:
        if letter[0]==word and len(word)>=5:
            coincidence=1
            letter[1]+=1
      if coincidence==0  and len(word)>=5:
         archive_colektion.append([word,1])
      coincidence=0  
def sorter():#Сортируем готовый архив
    archive_colektion.sort(key=lambda x: (x[1]), reverse=True)
def sorter_10():#Находим 10 первых
    chek = 0
    while chek<=10:
        archive_final.append(archive_colektion[chek])
        chek+=1
def txt_edgene(file_txt1,code1):#Получаем строка
 with codecs.open(file_txt1,'r',encoding=code1) as document:
    for line in document:
        collects_an_archive(line)   
def jason_edgene(file_txt1,code1):#Получаем строка
    with open(file_txt1, 'r', encoding=code1) as document: #открыли файл с данными
       text = json.load(document) #загнали все, что получилось в переменную
       #pprint(text) #вывели результат на экран
    for link in text['rss']['channel']['items']:
        #print(link['channel']['items']['description'])
        #print(link['description'])
        collects_an_archive(link['description'])
def xml_edgene(file_txt1,code1):#Получаем строка
    with open(file_txt1) as fp:
        soup = BeautifulSoup(fp, 'xml')

#Файлы TXT
file_txt1='Python_course-master\\PY1_Lesson_2.3\\newsafr.txt'
code1 = 'UTF-8'

file_txt2='Python_course-master\\PY1_Lesson_2.3\\newscy.txt'
code2 = 'KOI8-R'

file_txt3='Python_course-master\\PY1_Lesson_2.3\\newsfr.txt'
code3 = 'ISO8859-5'

file_txt4='Python_course-master\\PY1_Lesson_2.3\\newsit.txt'
code4 = 'CP1251'

file_jason1='Python_course-master\\PY1_Lesson_2.3\\newsafr.json'
code1_jason1 = 'UTF-8'

file_jason2='Python_course-master\\PY1_Lesson_2.3\\newscy.json'
code1_jason2 = 'KOI8-R'

file_jason3='Python_course-master\\PY1_Lesson_2.3\\newsfr.json'
code1_jason3 = 'ISO8859-5'

file_jason4='Python_course-master\\PY1_Lesson_2.3\\newsit.json'
code1_jason4 = 'CP1251'

file_xml1='Python_course-master\\PY1_Lesson_2.3\\newsafr.xml'
code1_xml1 = 'UTF-8'

archive_colektion=[]
archive_final=[]
#txt_edgene(file_txt1,code1)
#sorter()#Сортируем
#sorter_10()#Отбираем 10 первых
for sword in archive_final:
    print(sword[0],'-',sword[1])
print('')

archive_colektion=[]
archive_final=[]
#jason_edgene(file_jason4,code1_jason4)
#sorter()#Сортируем
#sorter_10()#Отбираем 10 первых
for sword in archive_final:
    print(sword[0],'-',sword[1])

archive_colektion=[]
archive_final=[]
xml_edgene(file_xml1,code1_jason1)
#sorter()#Сортируем
#sorter_10()#Отбираем 10 первых
for sword in archive_final:
    print(sword[0],'-',sword[1])