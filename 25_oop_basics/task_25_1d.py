# -*- coding: utf-8 -*-

'''
Задание 25.1d

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


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

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


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

	def add_link(self, new_local_dev_port, new_remote_dev_port):
		for local_dev_port, remote_dev_port in self.topology.items():
			if local_dev_port == new_local_dev_port and remote_dev_port == new_remote_dev_port: return print('Такое соединение существует')
			elif local_dev_port == new_local_dev_port or remote_dev_port == new_remote_dev_port: return print('Cоединение с одним из портов существует')
		self.topology[new_local_dev_port] = new_remote_dev_port
		return self.topology

t = Topology(topology_example)
pprint(t.topology)
print('Добавляем новый линк: ((\'R1\', \'Eth0/4\'), (\'R7\', \'Eth0/0\'))')
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
print('Добавляем новый линк: ((\'R1\', \'Eth0/4\'), (\'R7\', \'Eth0/0\'))')
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
print('Добавляем новый линк: ((\'R1\', \'Eth0/4\'), (\'R7\', \'Eth0/5\'))')
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
