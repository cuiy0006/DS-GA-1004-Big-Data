#!/usr/bin/env python

import sys

weekdaycnt = 0
weekendcnt = 0
currentkey = None
weekends = set(['05', '06', '12', '13', '19', '20', '26', '27'])
NOofWeekend = 8
NOofWeekday = 23

for line in sys.stdin:
	line = line.strip()
	violation_code, issue_date = line.split('\t', 1)
	_, _, issue_day = issue_date.split('-')

	if violation_code == currentkey:
		if issue_day in weekends:
			weekendcnt += 1
		else:
			weekdaycnt += 1
	else:
		if currentkey != None:
			print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentkey, weekendcnt/NOofWeekend, weekdaycnt/NOofWeekday))
		currentkey = violation_code
		weekdaycnt = 0
		weekendcnt = 0
		if issue_day in weekends:
			weekendcnt += 1
		else:
			weekdaycnt += 1

if currentkey != None:
	print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentkey, weekendcnt/NOofWeekend, weekdaycnt/NOofWeekday))
