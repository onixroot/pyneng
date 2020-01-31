# -*- coding: utf-8 -*-

'''
Задание 25.1a

Скопировать класс Topology из задания 25.1 и изменить его.

Если в задании 25.1 удаление дублей выполнялось в методе __init__,
надо перенести функциональность удаления дублей в метод _normalize.

При этом метод __init__ должен выглядеть таким образом:

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
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
        #pprint(topology_no_overlap)


top = Topology(topology_example)
pprint(top.topology)