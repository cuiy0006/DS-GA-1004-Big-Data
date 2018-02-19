#!/usr/bin/env python
# map function for matrix multiply
# Input file assumed to have lines of the form "A,i,j,x", where i is the row index, j is the column index, and x is the value in row i, column j of A. Entries of A are followed by lines of the form "B,i,j,x" for the matrix B.
# It is assumed that the matrix dimensions are such that the product A*B exists.

# Input arguments:
# m should be set to the number of rows in A, p should be set to the number of columns in B.

import sys
import os
# import numpy

# #number of rows in A
# m = int(sys.argv[1])

# #number of columns in B
# p = int(sys.argv[2])


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	currfile = os.environ.get('mapreduce_map_input_file')
	line = line.strip()
	entry = line.split(",")

	if 'open' in currfile:
		summon_number = entry[0]
		print('{0:s}\t{1:s}'.format(summon_number, '0'))
	else:
		summon_number = entry[0]
		plate_id = entry[14]
		violation_precinct = entry[6]
		violation_code = entry[2]
		issue_date = entry[1]
		print('{0:s}\t{1:s} {2:s} {3:s} {4:s} {5:s}'.format(summon_number, '1', plate_id, violation_precinct, violation_code, issue_date)) 

	
        
