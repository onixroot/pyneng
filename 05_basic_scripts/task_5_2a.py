# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

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

# host_mask = '10.0.1.1/24'
host_mask = '10.0.5.1/30'
calc_network(host_mask)