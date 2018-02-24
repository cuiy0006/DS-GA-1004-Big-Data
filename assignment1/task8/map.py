#!/usr/bin/env python

import sys
import os
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")

	vehicle_make = entry[-2].strip(string.punctuation).strip()
	vehicle_color = entry[-3].strip(string.punctuation).strip()

	print('{0:s},{1:s}\t{2:s}'.format('vehicle_make', vehicle_make, '1'))
	print('{0:s},{1:s}\t{2:s}'.format('vehicle_color', vehicle_color, '1'))
        
