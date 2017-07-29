#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys


in_file_1 = open(sys.argv[1])
in_file_2 = open(sys.argv[2])
in_file_3 = open(sys.argv[3])
out_file = open(sys.argv[4], 'w')

names_comp = dict()

for line in in_file_1:
	if line[0] != '#':
		names_comp[line.split()[1].split('.')[0]] = line.split()[0]

names_mnem = dict()

for line in in_file_2:
	if line[0] != '#':
		names_mnem[line.split()[0]] = line.split()[1].split('.')[0]

num_names = { x : 0 for x in names_mnem.keys()}

for line in in_file_3:
	if line[0] == '>':
		tax_name = names_comp[line.split('|')[1]]
		if num_names[tax_name] != 0:
			line = '>%s_%s\n' % (names_mnem[tax_name], num_names[tax_name])
		else:
			line = '>%s\n' % (names_mnem[tax_name])
		num_names[tax_name] += 1
	out_file.write(line)

out_file.close()
