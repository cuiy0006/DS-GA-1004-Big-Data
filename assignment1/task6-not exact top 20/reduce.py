#!/usr/bin/env python

import sys
from heapq import heappush, heappop

cnt = 0
currentkey = None
maxheap = []

mincnt = None
minlst = []

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
				if cnt >= maxheap[0][0]:
					tmpcnt, tmpkey = heappop(maxheap)
					if mincnt == tmpcnt:
						minlst.append((tmpcnt, tmpkey))
					else:
						mincnt = tmpcnt
						minlst = [(tmpcnt, tmpkey)]
					heappush(maxheap, (cnt, currentkey))

		currentkey = key
		cnt = 1

if currentkey != None:
	if len(maxheap) < 20:
		heappush(maxheap, (cnt, currentkey))
	else:
		if cnt >= maxheap[0][0]:
			tmpcnt, tmpkey = heappop(maxheap)
			if mincnt == tmpcnt:
				minlst.append((tmpcnt, tmpkey))
			else:
				mincnt = tmpcnt
				minlst = [(tmpcnt, tmpkey)]
			heappush(maxheap, (cnt, currentkey))

if mincnt == maxheap[0][0]:
	maxheap += minlst

maxheap.sort(key=lambda x:(-x[0], x[1]))
for cnt, key in maxheap:
	print('{0:s}\t{1:d}'.format(key, cnt)) 