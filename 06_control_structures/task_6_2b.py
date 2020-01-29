# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def check_ip():
	ip = input('Введите ip адрес в формате X.X.X.X: ')
	octets = ip.split('.')
	if len(octets)==4 and all(x.isdigit() for x in octets) and all(0<=int(y)<=255 for y in octets):
		oct1 = int(octets[0])
		if ip == '0.0.0.0': print('unassigned')
		elif ip == '255.255.255.255': print('local broadcast')
		elif 1 <= oct1 <= 223 : print('unicast')
		elif 224 <= oct1 <= 239 : print('multicast')
		else: print('unused')
	else:
		print('Неверный IP-адрес')
		check_ip()

check_ip()