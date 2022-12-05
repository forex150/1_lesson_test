import os

current_dectory = 'F:\\Рабочая папка\\python\\1_lesson\\Python_course-master\\PY1_Lesson_2.4\\homework\\Migrations'#os.getcwd()


def folder_engeni(current_dectory):
	a = os.listdir(current_dectory)
	file_path = []
	for element in a:
	   if os.path.isfile(os.path.join(current_dectory,element)) and ".sql" in element:
	      #print(element)
	      file_path.append(os.path.join(current_dectory,element))
	   elif not os.path.isfile(os.path.join(current_dectory,element)):
	      print('Папка',element)
	      folder_engeni(os.path.join(current_dectory,element))
	      print('Конец Папки',element)
	return file_path
def search_text(current_file,text):
	file_path_temp = []
	for element in current_file:
		chek = 0
		with open(element) as link:
			for linka in link:
				if text in linka and chek==0:
					file_path_temp.append(element)
					chek=1

	#print(file_path_temp)
	return file_path_temp
def input_text_def():
	input_text = input()
	return input_text
def print_def(text1):
	for element in text1:
		print(os.path.basename(element))
#current_dectory = os.getcwd()
#print(current_dectory)
#os.chdir('games')
#os.pathjoin
list_folder = folder_engeni(current_dectory)
a=0
while a==0:
	print('Введите строку поиска')
	print('е - выйти')
	input_text = input_text_def()
	if input_text=='e':
		exit()
	#print(list_folder)
	list_folder = search_text(list_folder,input_text)
	print_def(list_folder)
	#list_folder = file_path

print(list_folder)
