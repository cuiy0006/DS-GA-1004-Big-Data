#!/usr/bin/env python

import sys
import os
import string
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	line = re.sub(r'\".*?\"','1',line)
	license_type = entry[2]
	amount_due = entry[12]

	print('{0:s}\t{1:s}'.format(license_type, amount_due))

	
        
