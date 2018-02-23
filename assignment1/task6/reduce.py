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
		if currentkey != None:
			if len(maxheap) < 10:
				heappush(maxheap, (cnt, currentkey))
			else:
				if cnt > maxheap[0][0]:
					heappop(maxheap)
					heappush(maxheap, (cnt, currentkey))

			if len(minheap) < 10:
				heappush(minheap, (-cnt, currentkey))
			else:
				if -cnt > minheap[0][0]:
					heappop(minheap)
					heappush(maxheap, (-cnt, currentkey))

		currentkey = key
		cnt = 1

if currentkey != None:
	if len(maxheap) < 10:
		heappush(maxheap, (cnt, currentkey))
	else:
		if cnt > maxheap[0][0]:
			heappop(maxheap)
			heappush(maxheap, (cnt, currentkey))

	if len(minheap) < 10:
		heappush(minheap, (-cnt, currentkey))
	else:
		if -cnt > minheap[0][0]:
			heappop(minheap)
			heappush(maxheap, (-cnt, currentkey))

res = []
while len(maxheap) != 0:
	cnt, key = heappop(maxheap)
	res.append((key, cnt))
res.reverse()
while len(minheap) != 0:
	cnt, key = heappop(minheap)
	res.append((key, -cnt))
for key, cnt in res:
	print('{0:s}\t{1:d}'.format(key, cnt)) 

