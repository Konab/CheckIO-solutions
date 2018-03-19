# В этой миссии вы должны написать функцию, которая представит человека по переданным параметрам.
def say_hi(name, age):
	return "Hi. My name is {} and I'm {} years old".format(name, age)

# На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
def correct_sentence(text):
	if text[-1]!='.':
		return text[0].upper()+text[1:]+'.'
	else:
		return text[0].upper()+text[1:]

# Дана строка и нужно найти ее первое слово.
def first_word(text):
	for i in text.split():
		if '.' not in i and ' ' not in i:
			return i.split(',')[0]
	return text.split('.')[0]

# Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
def second_index(text, symbol):
	i = text[text.find(symbol)+1:].find(symbol)+(1+text.find(symbol))
	if i>0 and i!=text.find(symbol):
		return i

# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
# Начальный и конечный маркеры всегда разные
# Если нет начального маркера, то началом считать начало строки
# Если нет конечного маркера, то концом считать конец строки
# Если нет ни конечно ни начального маркеров, то просто вернуть всю строку
# Если конечный маркер стоит перед начального, то вернуть пустую строку
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]

# Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.
import operator
def best_stock(data):
	return sorted(data.items(), key=operator.itemgetter(1), reverse=True)[0][0]

# Ваша задача в этой миссии определить популярность определенных слов в тексте.
from collections import Counter
import string
def popular_words(text, words):
	sort_dict = Counter([word.strip(string.punctuation) for word in text.split()])
	f_dict = {}
	for i in words:
		f_dict[i] = sort_dict[i]
		I = i[0].upper() + i[1:]
		if I in sort_dict:
			f_dict[i] += sort_dict[I]
	return f_dict

# Дана таблица всех доступных продуктов на складе. Данные представленны в виде списка диктов (a list of dicts)
# Your mission here is to find TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one
def bigger_price(limit, data):
	list_data = []
	for i,doc in enumerate(data): list_data.append((doc['price'], i))
	list_data = sorted(list_data, reverse = True)
	new_data = []
	for i in range(limit): new_data.append(data[list_data[i][1]])
	return new_data

# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5; 
# Число, как строку для остальных случаев.
def checkio(number): 
	if number%3==0 and number%5==0:
		return 'Fizz Buzz'
	elif number%3==0:
		return 'Fizz'
	elif number%5==0:
		return 'Buzz'
	else:
		return str(number)

# Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).
def checkio(*args):
	if args: return max(args) - min(args)
	return 0
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
def checkio(arrey):
	if not arrey:
		return 0
	sum = 0
	for i in range(len(arrey)):
		if i%2==0:
			sum+=arrey[i]
	return sum*arrey[-1]

# ан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
import string
def find_message(text):
	if not text: return None
	new_text = ''
	f_text = ''
	for i in [word.strip(string.punctuation) for word in text.split()]: new_text+=i
	for i in new_text: 
		if i==i.upper() and i not in '-1234567890&*': f_text+=i
	return f_text

# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
def checkio(word):
	j=0
	for i in word.split():
		if i[0] not in '1234567890':
			j+=1
			if j==3:
				return True
		else: j=0
	return False

# Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. Если N за границами массива, тогда вернуть -1.
def index_power(array, n):
	if n<len(array): return array[n]**n
	return -1

# Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.
def left_join(phrases):
	return ','.join(phrases).replace('left','right')

# Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
def checkio(number):
	power = 1
	for i in str(number):
		if i!='0': power*=int(i)
	return power

# Дано положительное число как строка и основание системы счисления для него. Ваша функция должна конвертировать это число в десятичную систему счисления. Основание системы счисления меньше 37 и больше 1. В задаче используются цифры и буквы A-Z внутри строчного представления числа.
def checkio(str_number, radix):
	try:
		return(int(str_number,radix))
	except:
		return -1

# Массив (tuple) содержит различные числа. Вам необходимо отсортировать их, но отсортировать на основе абсолютных значений в возрастающем порядке. Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20). Ваша функция должна возвращать список (list) или кортеж (tuple).
def checkio(numbers_array):
	return sorted(numbers_array, key = lambda x:abs(x))

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequenc
from collections import Counter
def most_frequent(data):
	return sorted(list(Counter(data).items()), key=lambda tup: tup[1], reverse = True)[0][0]

# Your mission here is to create a function that gets an tuple and returns a tuple with 3 elements - first, third and second to the last for the given array
def easy_unpack(elements):
	return (elements[0],elements[2],elements[-2])

# Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
# Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
def date_time(time):
	data, clock = time.split()[0],time.split()[1]
	data = data.split('.')
	clock = clock.split(':')
	day = dict(zip(['00','01','02','03','04','05','06','07','08','09'],['0','1','2','3','4','5','6','7','8','9']))
	month = dict(zip(['01','02','03','04','05','06','07','08','09','10','11','12'],['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))
	if data[0] in day.keys(): data[0] = day[data[0]]
	if clock[0] in day.keys(): clock[0] = day[clock[0]]
	if clock[1] in day.keys(): clock[1] = day[clock[1]]
	h = ' hour ' if clock[0]=='1' else ' hours '
	m = ' minute' if clock[1]=='1' else ' minutes'
	return data[0]+' '+month[data[1]]+' '+data[2]+' year '+clock[0]+h+clock[1]+m
