import os
#import pprint
import sys
import subprocess
import shutil

import time
#import math
#from multiprocessing import Pool

def list_file_def(file): #Выдает список файлов
	list_file_temp = []
	path =file
	list_file = os.listdir(path)

	for element in list_file:
		if os.path.isfile(os.path.join(path,element)):
			list_file_temp.append(os.path.join(path,element))
	print(list_file_temp)		
	return list_file_temp
def sufics_input():#Спрашивает за суфикс
	print('Введите суфикс к итоговым файлам')
	return input()
def create_a_folder(path,folder):#Создать папку для результата
	print(os.path.isdir(path))
	print(os.path.join('Result'))
	if not os.path.isdir(path):
		os.makedirs(path)
	else:
		dell_file_temp(path)
		os.makedirs(path)
def pool_process(element,x_size,y_size,folder_path,sufics):#Мульти процессинг
	name=os.path.basename(os.path.join(element))
	name_temp = str(sufics)+'_'+str(name)
	folder_path2=os.path.join(folder_path,name_temp)
	print('folder_path2 ',folder_path2)
	print('path ',element)
	name_path_file='convert.exe "'+str(element)+'" -resize '+str(x_size)+'x'+str(y_size)+' "'+folder_path2+'"' 
	print('name_path_file - '+name_path_file)
	subprocess.run(name_path_file)
def engeni_img(list_file,x_size,y_size,folder_path,sufics):#Обрабатываем каждый файл
	for element in list_file:
		pool_process(element,x_size,y_size,folder_path,sufics)	
def dell_file_temp(path):#Удалить файлы
	path = os.path.join(os.getcwd(),path)
	shutil.rmtree(path)
def copy_and_final(folder_path,folder_result_final,folder_result):#Окончание
	list_file2=list_file_def(folder_path)#Получаем список файлов
	create_a_folder(folder_result_final,'Folder')
	#Копируем файлы
	for element in list_file2:
		element_in_copy = os.path.join(folder_result_final,os.path.basename(element))
		shutil.copyfile(element, element_in_copy)
	dell_file_temp(folder_result)

print('Это список файлов для обработки')
os.chdir('F:\\Рабочая папка\\python\\1_lesson\\Python_course-master\\PY1_Lesson_2.5\\homework')
#dell_file_temp('Result')

start_time = time.perf_counter()

list_file=[]
sufics=sufics_input()
folder_result="Result2"
Folder_orignal='H:\\Новая папка\\Black Big'
x_size = 100
y_size = 600
folder_path ="Result2"
folder_result_final = "F:\\Рабочая папка\\python\\1_lesson\\Python_course-master\\PY1_Lesson_2.5\\homework\\Result"

#folder_path=os.path.join(os.getcwd(),folder_result)#Путь к папке с результатам
#folder_path=folder_result
create_a_folder(folder_path,folder_result)#Создать папку для результатов

list_file=list_file_def(Folder_orignal)#Получить список файлов в папке с исходниками
#pprint(list_file)
engeni_img(list_file,x_size,y_size,folder_path,sufics)#Отправляем файлы на обработку и складываем их
finish_time = time.perf_counter()
print("Program finished in {} seconds - using multiprocessing".format(finish_time-start_time))
print("---")



copy_and_final(folder_path,folder_result_final,folder_result)#Окончание



#print(list_file)


