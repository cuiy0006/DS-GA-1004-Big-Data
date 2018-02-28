#!/usr/bin/env python

import sys
from heapq import heappush, heappop

cnt = 0
currentkey = None
maxheap = []

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t', 1)

	if key == currentkey:
		cnt += 1
	else:
		if currentkey != None:
			if len(maxheap) < 20:
				heappush(maxheap, (cnt, currentkey))
			else:
				if cnt > maxheap[0][0]:
					heappop(maxheap)
					heappush(maxheap, (cnt, currentkey))

		currentkey = key
		cnt = 1

if currentkey != None:
	if len(maxheap) < 20:
		heappush(maxheap, (cnt, currentkey))
	else:
		if cnt > maxheap[0][0]:
			heappop(maxheap)
			heappush(maxheap, (cnt, currentkey))

maxheap.sort()
for key, cnt in maxheap:
	print('{0:s}\t{1:d}'.format(key, cnt)) 