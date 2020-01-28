# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

def calc_network(host_mask):
	host, mask_prefix = host_mask.split('/')
	host = list(map(int, host.split('.')))
	mask_prefix = int(mask_prefix)

	ext2 = [128,64,32,16,8,4,2,1]
	bin_to_dec = lambda a: sum(ext2[:a]) if a>0 else 0
	mask = [bin_to_dec(mask_prefix-b*8) for b in range(4)]

	network = list(map(lambda x,y: x&y, host, mask))

	network_template = 'Network:\n{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:0>8b}  {1:0>8b}  {2:0>8b}  {3:0>8b}\n'
	print(network_template.format(network[0], network[1], network[2],  network[3]))

	mask_template = 'Mask:\n/{4}\n{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:0>8b}  {1:0>8b}  {2:0>8b}  {3:0>8b}'
	print(mask_template.format(mask[0], mask[1], mask[2], mask[3], str(mask_prefix)))

host_mask = argv[1]
calc_network(host_mask)