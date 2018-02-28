#!/usr/bin/env python

import sys
import os
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	license_type = entry[2].strip().strip(string.punctuation).strip()
	amount_due = entry[12].strip().strip(string.punctuation).strip()
	if license_type == 'NULL' or license_type == 'JZ' or license_type =='L744':
		continue

	if license_type=='1630':
		license_type = entry[2]

	print('{0:s}\t{1:s}'.format(license_type, amount_due))

	
        
