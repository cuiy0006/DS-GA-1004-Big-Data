#!/usr/bin/env python

import sys
import os
import string
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	matches = re.findall(r'\".*?\"', line)
	lst = list(map(lambda s:s[1:-1].replace(',', '*'), matches))
	for i, match in enumerate(matches):
		line = line.replace(match, lst[i])
	entry = line.split(',')

	vehicle_make = entry[-2]
	vehicle_color = entry[-3]

	if vehicle_make == '':
		vehicle_make = 'NONE'

	print('{0:s},{1:s}\t{2:s}'.format('vehicle_make', vehicle_make, '1'))
	if vehicle_color == '':
		vehicle_color = 'NONE'

	print('{0:s},{1:s}\t{2:s}'.format('vehicle_color', vehicle_color, '1'))
        
