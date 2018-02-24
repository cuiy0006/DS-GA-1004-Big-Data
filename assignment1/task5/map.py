#!/usr/bin/env python

import sys
import os
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	plate_id = entry[14].strip(string.punctuation).strip()
	registration_state = entry[16].strip(string.punctuation).strip()

	print('{0:s}, {1:s}\t{2:s}'.format(plate_id, registration_state, '1')) 

	
        
