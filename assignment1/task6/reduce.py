#!/usr/bin/env python

import sys
from heapq import heappush, heappop

cnt = 0
currentkey = None
minheap = []
maxheap = []

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)

	if key == currentkey:
		cnt += 1
	else:
		if max_cnt < cnt:
			max_key = currentkey
			max_cnt = cnt
		currentkey = key
		cnt = 1

if max_key != None:
	print('{0:s}\t{1:d}'.format(max_key, max_cnt))
