# 2017-07-10 Challege #323 - 3SUM

from itertools import combinations

# Input list
old_input = "9 -6 -5 9 8 3 -4 8 1 7 -4 9 -9 1 9 -9 9 4 -6 -8"

input_test = '''4 5 -1 -2 -7 2 -5 -3 -7 -3 1
-1 -6 -3 -7 5 -8 2 -8 1
-5 -1 -4 2 9 -9 -6 -1 -7'''

input_list = input_test.split('\n')

# create a list of combinations of 3 for all input lines
comb = []
for input in input_list:
	comb.append(combinations(input.split(),3))


# Iterate each combination line in the input
for i in comb:
	zerosum_numbers = []
	# Iterate each tuple of combinations of 3
	for tup in i:
		result = 0
		# Add the 3 numbers in the tuple, convert to int to sum them
		for num in tup:
			result += int(num)
		if result == 0:
			# Append the ones that sum to zero to a temp list to print out
			zerosum_numbers.append(tup)
	# Print the list before moving to the next input line
	for li in zerosum_numbers:
		print li
	print "Number of answers:", len(zerosum_numbers)
	print