#!/usr/bin/env python

import sys
import os
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	license_type = entry[2].strip(string.punctuation).strip()
	if license_type == '':
		continue
	amount_due = entry[12].strip(string.punctuation).strip()
	if amount_due == '':
		amount_due = '0'

	print('{0:s}\t{1:s}'.format(license_type, amount_due))

	
        
