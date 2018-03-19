# Стефан и София забывают о безопасности и используют простые пароли для всего. Помогите Николе разработать модуль для проверки паролей на безопасность. Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.
def checkio(data):
	if len(data)<10:
		return False
	num = sum(i.isdigit() for i in data)
	up_str = sum(i.isupper() for i in data)
	low_str = sum(i.islower() for i in data)
	return True if num>0 and up_str>0 and low_str>0 else False

# Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
import collections
import re
def checkio(text):
    return collections.Counter(sorted(''.join(re.findall('[A-z]+',text)).lower())).most_common(1)[0][0]

# Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). Для решения этой задачи не меняйте оригинальный порядок элементов. Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
def checkio(data):
	d = []
	for i in range(len(data)):
		if data[i] in data[:i] or data[i] in data[i+1:]:
			d.append(data[i])
	return d 

# Задача о бесконечных обезьянах
def count_words(text, words):
	text = text.lower()
	n=0
	for i in words:
		if text.find(i)!=-1:
			n+=1
	return n

# Крестики нолики
def checkio(game_result):
	for i in range(3):
		game_result[i] = list(game_result[i])
		for j in range(3):
			if game_result[i][j]=='X': game_result[i][j]=1
			if game_result[i][j]=='O': game_result[i][j]=-1
			if game_result[i][j]=='.': game_result[i][j]=0
	if sum(game_result[0])==3 or sum(game_result[1])==3 or sum(game_result[2])==3 or sum([game_result[0][0],game_result[1][0],game_result[2][0]])==3 or sum([game_result[0][1],game_result[1][1],game_result[2][1]])==3 or sum([game_result[0][2],game_result[1][2],game_result[2][2]])==3 or sum([game_result[0][0],game_result[1][1],game_result[2][2]])==3 or sum([game_result[0][2],game_result[1][1],game_result[2][0]])==3:
		return 'X'
	elif sum(game_result[0])==-3 or sum(game_result[1])==-3 or sum(game_result[2])==-3 or sum([game_result[0][0],game_result[1][0],game_result[2][0]])==-3 or sum([game_result[0][1],game_result[1][1],game_result[2][1]])==-3 or sum([game_result[0][2],game_result[1][2],game_result[2][2]])==-3 or sum([game_result[0][0],game_result[1][1],game_result[2][2]])==-3 or sum([game_result[0][2],game_result[1][1],game_result[2][0]])==-3:
		return 'O'
	else:
		return 'D'

# Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.
def safe_pawns(pawns):
	n = 0
	for i in pawns:
		if chr(ord(i[0])-1)+str(int(i[1])-1) in pawns or chr(ord(i[0])+1)+str(int(i[1])-1) in pawns:
			n+=1
	return n

# Написать функции min и max
def min(*args, **kwargs):
	if len(args)==1:
		if kwargs:
			return sorted(args[0], key = kwargs['key'])[0]
		return sorted(args[0])[0]
	if kwargs:
		return sorted(args, key = kwargs['key'])[0]
	return sorted(args)[0]

def max(*args, **kwargs):
	if len(args)==1:
		if kwargs:
			return sorted(args[0], key = kwargs['key'], reverse = True)[0]
		return sorted(args[0], reverse = True)[0]
	if kwargs:
		return sorted(args, key = kwargs['key'], reverse = True)[0]
	return sorted(args, reverse = True)[0]

# Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". Последняя подстрока является самой длинной, что и делает ее ответом.
def long_repeat(line):
	if len(line)==0: return 0
	n=[]
	j = 1 
	l = line[0]
	for i in range(1,len(line)):
		if l == line[i]:
			j+=1
			n.append(j)
			l = line[i]
		else:
			j=1
			l = line[i]
			n.append(j)
	return max(n)

# В этой миссии Вам надо определить, все ли элементы массива равны.
from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
	if len(elements)==1: return True 
	for i in range(len(elements)):
		if (elements[i] not in elements[:i]) and (elements[i] not in elements[i+1:]):
			return False
	return True