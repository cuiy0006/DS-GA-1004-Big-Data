#!/usr/bin/env python

import sys
import os

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	violation_code = entry[2]

	print('{0:s}\t{1:s}'.format(violation_code, '1')) 

	
        
