#!/usr/bin/env python

import sys

openkey = None
parkingkey = None
parkingvalue = []
currentkey = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)
	entry = value.split(',')
	if '"' in entry[1]:
		entry[1] = entry[1][1:-1].replace('*', ',')
	if key == currentkey:
		if entry[0] == '0':  # from open
			openkey = key
		else:
			parkingkey = key
			parkingvalue = entry
	else:
		if parkingkey != None and parkingkey != openkey:
			print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(parkingkey, parkingvalue[1], parkingvalue[2], parkingvalue[3], parkingvalue[4]))
		currentkey = key
		openkey = None
		parkingkey = None
		parkingvalue = []
		if entry[0] == '0': #from open
			openkey = key
		else: #from parking
			parkingkey = key
			parkingvalue = entry

if parkingkey != None and parkingkey != openkey:
	print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(parkingkey, parkingvalue[1], parkingvalue[2], parkingvalue[3], parkingvalue[4]))
