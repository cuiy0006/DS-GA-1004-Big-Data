#!/usr/bin/env python

import sys
from decimal import Decimal

other_cnt = 0
NY_cnt = 0

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)

	if key == 'NY':
		NY_cnt += 1
	else:
		other_cnt += 1

if NY_cnt != 0:
	print('{0:s}\t{1:d}'.format('NY', NY_cnt))
if other_cnt != 0:
	print('{0:s}\t{1:d}'.format('Other', other_cnt))