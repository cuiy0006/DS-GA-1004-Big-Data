#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)

dic = {}
total = 0
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	continue
# 	#Remove leading and trailing whitespace
# 	line = line.strip()

# 	#Get key/value 
# 	key, value = line.split('\t',1)

# 	#Parse key/value input (your code goes here)

# 	entry = value.split(' ')
# 	MatrixName = entry[0]
# 	j = entry[1]
# 	subKey = (MatrixName, j)
# 	try:
# 		subValue = float(entry[2])
# 	except ValueError:
# 		continue

# 	#If we are still on the same key...
# 	if key==currentkey:

# 		#Process key/value pair (your code goes here)
# 		searchMatrix = 'A'
# 		if MatrixName == 'A':
# 			searchMatrix = 'B'

# 		searchKey = (searchMatrix, j)
# 		if searchKey in dic:
# 			total += subValue * dic[searchKey]
# 		else:
# 		#Otherwise, if this is a new key...
# 			dic[subKey] = subValue


# 	else:
# 		#If this is a new key and not the first key we've seen
# 		if currentkey:

# 			#compute/output result to STDOUT (your code goes here)
# 			print('{0:s}\t{1:f}'.format(currentkey, total))

# 		currentkey = key

# 		#Process input for new key (your code goes here)
# 		total = 0
# 		dic = {subKey: subValue}



# #Compute/output result for the last key (your code goes here)
# if currentkey == key:
# 	print('{0:s}\t{1:f}'.format(currentkey, total))



