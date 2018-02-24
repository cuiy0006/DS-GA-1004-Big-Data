#!/usr/bin/env python

import sys
from decimal import Decimal

cnt = 0
currenttotal = Decimal(0)
currentkey = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)
	try:
		amount_due = Decimal(value)
	except ValueError:
		continue

	if key == currentkey:
		currenttotal += amount_due
		cnt += 1
	else:
		if currentkey:
			if currentkey == 'NULL':
				currentkey = ''
			print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentkey, currenttotal, currenttotal/cnt))
		currentkey = key
		cnt = 1
		currenttotal = amount_due

if currentkey != None:
	print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentkey, currenttotal, currenttotal/cnt))
