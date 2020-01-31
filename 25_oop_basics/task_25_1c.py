# -*- coding: utf-8 -*-

'''
Задание 25.1c

Изменить класс Topology из задания 25.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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

	def delete_node(self, delete_device):
		dev_found = False
		for local_dev_port, remote_dev_port in [x for x in t.topology.items()]:
			if local_dev_port[0] == delete_device or remote_dev_port[0] == delete_device:
				del t.topology[local_dev_port]
				dev_found = True
		if not dev_found: print('Такого устройства нет\n')


print('Создание топологии:\nt = Topology(topology_example)')
t = Topology(topology_example)

print('\nt.topology: ')
pprint(t.topology)

print('\nУдаление устройства:\nt.delete_node(\'SW1\')')
t.delete_node('SW1')
pprint(t.topology)

print('\nЕсли такого устройства нет, выводится сообщение:\nt.delete_node(\'SW1\')')
t.delete_node('SW1')