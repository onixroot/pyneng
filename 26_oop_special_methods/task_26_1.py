# -*- coding: utf-8 -*-

'''
Задание 26.1

Изменить класс Topology из задания 25.1x.

Добавить метод, который позволит выполнять сложение двух объектов (экземпляров) Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

Создание двух топологий:

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
							 ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Суммирование топологий:

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка, что исходные топологии не изменились:

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
'''

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
					('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
					('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
					('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
					('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
					('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
					('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
					('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
					('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
					 ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

from pprint import pprint

class Topology:
	def __init__(self, topology_example):
		self.topology = topology_example

	def __add__(self, add_topology):
		for local_dev_port, remote_dev_port in add_topology.topology.items(): 
			self.topology[local_dev_port] = remote_dev_port
			return Topology(self.topology)

print('t1 = Topology(topology_example)')
t1 = Topology(topology_example)

print('\nt1.topology: ')
pprint(t1.topology)

print('\nt2 = Topology(topology_example2)')
t2 = Topology(topology_example2)

print('\nt2.topology: ')
pprint(t2.topology)

print('\nt3 = t1+t2:')
t3 = t1+t2

print('\nt3.topology: ')
pprint(t3.topology)

print('\nПроверка, что исходные топологии не изменились:')

print('\nt1.topology: ')
pprint(t1.topology)

print('\nt2.topology: ')
pprint(t2.topology)