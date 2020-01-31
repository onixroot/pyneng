# -*- coding: utf-8 -*-

'''
Задание 25.1b

Изменить класс Topology из задания 25.1a или 25.1.

Добавить метод delete_link, который удаляет указанное соединение.
Метод должен удалять и зеркальное соединение, если оно есть.

Если такого соединения нет, выводится сообщение "Такого соединения нет".

Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление линка:
In [9]: t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление зеркального линка
In [11]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))

In [12]: t.topology
Out[12]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}

Если такого соединения нет, выводится сообщение:
In [13]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
Такого соединения нет

'''

from pprint import pprint

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

class Topology:
	def __init__(self, topology_dict):
		self.topology = self._normalize(topology_dict)

	def _normalize(self, topology_example):
		topology_no_overlap = {}
		for dev_port in topology_example:
			if topology_example[dev_port] not in topology_example: 
				topology_no_overlap[dev_port] = topology_example[dev_port]
			else: 
				if topology_example[dev_port] not in topology_no_overlap:
					topology_no_overlap[dev_port] = topology_example[dev_port]
		return topology_no_overlap

	def delete_link(self, local_dev_port, remote_dev_port):
		if t.topology.get(local_dev_port): del t.topology[local_dev_port]
		elif t.topology.get(remote_dev_port): del t.topology[remote_dev_port]
		else: print('Такого соединения нет')

print('Создание топологии: \nt = Topology(topology_example)')
t = Topology(topology_example)

print('\nt.topology: ')
pprint(t.topology)

print('\nУдаление линка:\nt.delete_link((\'R3\', \'Eth0/1\'), (\'R4\', \'Eth0/0\'))')
t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
pprint(t.topology)

print('\nУдаление зеркального линка:\nt.delete_link((\'R5\', \'Eth0/0\'), (\'R3\', \'Eth0/2\'))')
t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
pprint(t.topology)

print('\nt.delete_link((\'R5\', \'Eth0/0\'), (\'R3\', \'Eth0/2\'))')
t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))