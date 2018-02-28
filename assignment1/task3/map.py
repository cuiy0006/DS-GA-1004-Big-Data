#!/usr/bin/env python

import sys
import os
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	license_type = entry[2]
	amount_due = entry[-6]
	if license_type == 'NULL' or license_type == 'JZ' or license_type =='L744':
		continue

	print('{0:s}\t{1:s}'.format(license_type, amount_due))

	
        
