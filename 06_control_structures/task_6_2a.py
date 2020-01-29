# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

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
	else: print('Неверный IP-адрес')

check_ip()