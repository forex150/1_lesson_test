import json
import csv
def user_list(user_list):#Список пользователей
	check = 0
	users_chek =[]

	print('Выбирите пользователя')
	for element in user_list:
		
		print(check,'-',user_list[element]['name'])
		users_chek.append(element)
		check+=1
	print(check,'- Добавить пользователя')
	
	input_user = int(input())
	if 0<=input_user<len(users_chek):
		print('Пользователь',user_list[users_chek[input_user]]['name'])
		return(user_list[users_chek[input_user]])
	elif input_user==len(users_chek):
		print('Добавим пользователя')
def checking_for_correctness(date_list):#проверка на коректность
	print(date_list[1])
	schet = 0
	for arr, dep in  date_list :
		arrival = date_list[schet][0]
		departure = date_list[schet][1]
		schet+=1
		print('дата прибытия',arrival,'дата отезда',departure)
		if not type(arrival) == int or not type(departure) == int:
			return('Ошибка значение не является числом')
		if arrival>departure:
			return('Ошибка в датах')
		if not schet==len(date_list):
			if departure>date_list[schet][0]:
				return('Ошибка вы приехали раньше чем уехали в прошлый раз')
	return date_list
def the_list_is_counted(date_list):#просто сумма всех переменных
	date_list_summ = []
	for element in date_list:
		date_list_summ.append(element[1]-element[0]+1)
	return date_list_summ
def summ_day(date_list):#Сумма одной поездки
	date_list = date_list[1]-date_list[0]+1
	return date_list
def schengen_counter(date_list):#Движок подсчета
	for element in date_list:
		shengen_sum = 0
		shengen_sum +=summ_day(element)
		for element_old in date_list:
			if element_old[1]<element[0] and element_old[1]>element[1]-LIMITED_180:
				shengen_sum+=summ_day(element_old)
		#print(shengen_sum)
		shengen_sum_list.append(shengen_sum)
def checking_for_limits(summ_list,days_of_stay_def): #проверка на лимиты
	check = 0
	for element, element2 in zip(summ_list,days_of_stay_def):
		if element>LIMITED_90:
			print('Превышение лимита. Время прибытия ',element,'Поездка',element2)
		check+=1
def first_entry(days_of_stay_in_schengen_def):#Первая поездка
	e=0
	while e==0:
	   print('У вас было совершено всего',len(days_of_stay_in_schengen_def),'Поездок')
	   print('e - подробней')
	   print('v - выбрать пользователя')
	   print('s - выход')
	   input_user = input()
	   if input_user=='s':
	      #e=1
	      save_select()
	      exit(0)
	   elif input_user=='e':
	      schengen_counter(days_of_stay_in_schengen_def)#Движок подсчета
	      print(shengen_sum_list)
	      checking_for_limits(shengen_sum_list,days_of_stay_in_schengen_def)
	   elif input_user=='v':
	   	 engine()


	      #Экраны
def engine():#Основной движок
	select = user_list(days_of_stay_in_schengen_plus_user)#Выбираем пользователя
	#print(select)
	arivves(select['visits'])
	first_entry(select['visits'])
def arivves(date_list):#Просто все поездки
	print(date_list)
def save_json():#Сохраняем в фаил
	with open('becup1.json','w') as write_file:
		json.dump(days_of_stay_in_schengen_plus_user,write_file)
def loading_json():#Загружаем json
	with open('becup1.json','r') as write_file:
		days_of_stay_in_schengen_plus_user= json.load(write_file)
	return days_of_stay_in_schengen_plus_user
def save_csv():
	with open('becup.csv','w') as write_file:
		fieldname = ['first_name','rus_name','date_list']
		writer = csv.DictWriter(write_file,fieldnames=fieldname,quoting=csv.QUOTE_NONNUMERIC)

		writer.writeheader()
		for element in days_of_stay_in_schengen_plus_user:
			writer.writerow({'first_name': element, 'rus_name': days_of_stay_in_schengen_plus_user[element]['name'],'date_list':days_of_stay_in_schengen_plus_user[element]['visits']})
def loading_csv():
	list_data = {}
	with open('becup.csv') as csvfile:
		country_reader = csv.DictReader(csvfile,delimiter=',')
		for row in country_reader:
			list_data_smal = {
			'name':row['rus_name'],
			'visits':row['date_list']
			}

			list_data[row['first_name']]=list_data_smal
			#list_data[row['first_name']]['visits']=row['date_list']
			print (list_data)
	return list_data

def save_select():#Выбираем метод сохранения
	print('Выбирите метод сохранения')
	print('1 - json')
	print('2 - csv')
	user_input = input()
	if user_input=='1':
		save_json()
	elif user_input=='2':
		save_csv()
def load_select():#Выбираем метод загрузки
	print('Выбирите метод загрузки')
	print('1 - json')
	print('2 - csv')
	user_input = input()
	if user_input=='1':
		return loading_json()
	elif user_input=='2':
		return loading_csv()


print('Добро пожаловать')
print('В Шенгенский калькулятор')

LIMITED_90 = 90
LIMITED_180 = 180
shengen_sum_list = []
days_of_stay_in_schengen_plus_user=load_select()
#days_of_stay_in_schengen = [[9,10],[15,24],[83,94],[108,135],[136,198],[250,260]]
#user_list1 = ['Гребенюк','Петухова','Машников']
#days_of_stay_in_schengen_plus_user={
#	'Grebenuk':{
#	'name':'Гребенюк',
#	'visits': [[9,10],[15,24],[83,94],[108,135],[136,198],[250,260]],
#	},
#	'visits': [[9,10],[15,24],[83,94],[108,135],[136,198]],
#	},
#	'Mashnicov':{
#	'name':'Машников',
#	'visits': [[9,10],[15,24],[83,94],[108,135],[136,198],[250,260]],
#	},
#}
#print(days_of_stay_in_schengen_plus_user['Petuhova']['name'])
#print(days_of_stay_in_schengen_plus_user)

engine()



#print(checking_for_correctness(days_of_stay_in_schengen))#проверка на коректность
#print(the_list_is_counted(days_of_stay_in_schengen))#просто сумма всех переменных
#print(summ_day([10,15]))
#schengen_counter(days_of_stay_in_schengen)#Движок подсчета
#checking_for_limits(shengen_sum_list)