#!/usr/bin/env python

import sys
import os
import string
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = re.sub(r'\".*?\"','1',line)
	entry = line.split(",")

	registration_state = entry[16]
	if registration_state != 'NY':
		registration_state = 'Other'
		
	print('{0:s}\t{1:s}'.format(registration_state, '1')) 

	
        
