#!/usr/bin/env python

import sys
import os
import string
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	currfile = os.environ.get('mapreduce_map_input_file')
	line = line.strip()
	#line = re.sub(r'\".*?\"','1',line)
	matches = re.findall(r'\".*?\"', line)
	lst = list(map(lambda s:s.replace(',','*'), matches))
	for i, match in enumerate(matches):
		line = line.replace(match, lst[i])
	entry = line.split(',')

	if 'open' in currfile:
		summon_number = entry[0]
		print('{0:s}\t{1:s}'.format(summon_number, '0'))
	else:
		summon_number = entry[0]
		plate_id = entry[-8]
		violation_precinct = entry[-16]
		violation_code = entry[2]
		issue_date = entry[1]
		print('{0:s}\t{1:s},{2:s},{3:s},{4:s},{5:s}'.format(summon_number, '1', plate_id, violation_precinct, violation_code, issue_date)) 

	
        
