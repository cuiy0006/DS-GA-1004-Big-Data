#!/usr/bin/env python

import sys

currentkey = None
cnt = 0
color_dic = {}
make_dic = {}

for line in sys.stdin:
	line = line.strip()
	key, _ = line.split('\t', 1)

	if key == currentkey:
		cnt += 1
	else:
		if currentkey != None:
			curr_column_name, curr_term = currentkey.split(',')
			if curr_column_name == 'vehicle_make':
				make_dic[curr_term] = cnt
			else:
				color_dic[curr_term] = cnt
		currentkey = key
		cnt = 1

if currentkey != None:
	curr_column_name, curr_term = currentkey.split(',')
	if curr_column_name == 'vehicle_make':
		make_dic[curr_term] = cnt
	else:
		color_dic[curr_term] = cnt

makes = sorted(list(make_dic.keys()))
colors = sorted(list(color_dic.keys()))
for make in makes:
	print('{0:s}\t{1:s}, {2:d}'.format('vehicle_make', make, make_dic[make]))
for color in colors:
	print('{0:s}\t{1:s}, {2:d}'.format('vehicle_color', color, color_dic[color]))