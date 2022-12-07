import os
def limited_file(text,limitation):
    #print(len(text))
    chek = True
    str_text_limited = []
    start_posishion = 0
    if len(text)<limitation:
        str_text_limited.append(text)
    else:
        while chek:
           if len(text)<start_posishion+limitation:
                str_text_limited.append(text[start_posishion:-1])
                break
           #print(start_posishion,limitation,start_posishion+limitation)
           #print(text)
           test_text=''
           for element in text[start_posishion:-1]:
               #print(element)
               start_posishion=start_posishion+1
               if element=='.':
                   test_text=test_text+element

                   break
               else:
                   test_text=test_text+element


           print(test_text)


           #start_posishion=start_posishion+9000


                #start_posishion=start_posishion+1
                #print(start_posishion)
                #print(text[start_posishion+limitation])







    #print(str_text_limited)
    return str_text_limited
def loсal_engine(str_open):
    return 'en'
def Get_a_list_of_all_files_in_a_folder(the_way,filter):#Получить список всех файлов в папке (путь)(список с путями и именами файлов)
    filter_the_way = []
    files = os.listdir(the_way)
    for element in files:
        if filter in element:
            filter_the_way.append(element)
    #print(filter_the_way)

    return filter_the_way
def Determine_the_language_of_the_file(Main_List):#Определить язык файла (список с путями и именами)(тотже список но добавили языки)
    Main_List_reg= []
    for element in Main_List:
        #print(os.path.join(the_way,element))
        with open(os.path.join(the_way,element),'r') as r:
            str_open= r.read(17)
            file_languageg = loсal_engine(str_open)
            #print(file_languageg)
            Main_List_reg.append([element,file_languageg])
            #print(element,file_languageg)
    #print(Main_List_reg)
    return Main_List_reg

def Work_on_translation(Main_List,limitation,the_way):#Работа над переводом (Список все тотже но расшириный)
    for element in Main_List:
      with open(os.path.join(the_way,element[0]),'r',encoding='UTF-8') as f:
          limited_arr = limited_file(f.read(),limitation)
          engine_translete(limited_arr, element[1])
    return limited_arr

def engine_translete(text,local):
    #print('engine_translete',text,local)

    return 12

print('Привет я первая строка')
the_way = 'F:\\Рабочая папка\\python\\1_lesson\\Python_course-master\\PY3_Lesson_3.2' #Путь к файлу
Main_List = [] #Список главный с путями именами и языками
filter = 'txt' #Фильтр для поиска файлов
limitation = 50

Main_List = Get_a_list_of_all_files_in_a_folder(the_way,filter)#Получить список всех файлов в папке (путь)(список с путями и именами файлов)
#print(Main_List)
Main_List = Determine_the_language_of_the_file(Main_List)#Определить язык файла (список с путями и именами)(тотже список но добавили языки)
#print(Main_List)
Work_on_translation(Main_List,limitation,the_way)#Работа над переводом (Список все тотже но расшириный)

