# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

termplate = '''Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''

# port_info = ospf_route.split()
#['O', '10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']

_, prefix, metric, _, nexthop, update, interface = ospf_route.split()

# print(termplate.format(port_info[1], port_info[2][1:-1], port_info[4][:-1], port_info[5][:-1], port_info[6]))
print(termplate.format(prefix, metric[1:-1], nexthop[:-1], update[:-1], interface))