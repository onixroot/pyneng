# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan_number = input('Введите номер vlan\'a: ')

file_name = 'CAM_table.txt'
vlans = {}

with open(file_name, 'r') as file:
	output = file.readlines()

for line in range(6,len(output)):
	vlans[output[line].replace('DYNAMIC   ','')] = int(output[line].split()[0])

for x,y in vlans.items():
	if y==int(vlan_number): print(x, end='')
