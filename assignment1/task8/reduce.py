#!/usr/bin/env python

import sys

color_dic = {}
make_dic = {}

for line in sys.stdin:
	line = line.strip()
	key, _ = line.split('\t', 1)

	curr_column_name, curr_term = key.split(',')
	if curr_column_name == 'vehicle_make':
		if curr_term in make_dic:
			make_dic[curr_term] += 1
		else:
			make_dic[curr_term] = 1
	else:
		if curr_term in color_dic:
			color_dic[curr_term] += 1
		else:
			color_dic[curr_term] = 1


makes = sorted(list(make_dic.keys()))
colors = sorted(list(color_dic.keys()))
for make in makes:
	print('{0:s}\t{1:s} {2:d}'.format('vehicle_make', make, make_dic[make]))
for color in colors:
	print('{0:s}\t{1:s} {2:d}'.format('vehicle_color', color, color_dic[color]))