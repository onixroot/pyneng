# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file_name = argv[1]
with open(file_name, 'r') as file:
	for line in file:
		if line[0] != '!' and not any(w in line for w in ignore):
			print(line, end='')

