#!/usr/bin/env python

import sys
from decimal import Decimal

cnt = 0
currenttotal = Decimal(0)
currentkey = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)
	amount_due = Decimal(value)

	if key == currentkey:
		currenttotal += amount_due
		cnt += 1
	else:
		if currentkey:
			print('{0:s}\t{1:s} {2:s}'.format(currentkey, str(round(currenttotal, 2)), str(round(currenttotal/cnt, 2))))
		currentkey = key
		cnt = 1
		currenttotal = amount_due

if currentkey != None:
	print('{0:s}\t{1:s} {2:s}'.format(currentkey, str(round(currenttotal, 2)), str(round(currenttotal/cnt, 2))))
