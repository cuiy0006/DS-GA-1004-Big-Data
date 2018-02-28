#!/usr/bin/env python

import sys
import os
import string
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	matches = re.findall(r'\".*?\"', line)
	lst = list(map(lambda s:s.replace(',','*'), matches))
	for i, match in enumerate(matches):
		line = line.replace(match, lst[i])
	entry = line.split(',')

	plate_id = entry[14]
	if '"' in plate_id:
		plate_id = plate_id[1:-1].replace('*', ',')
	registration_state = entry[16]
	# if plate_id == 'T':
	# 	continue

	print('{0:s}, {1:s}\t{2:s}'.format(plate_id, registration_state, '1')) 

	
        
