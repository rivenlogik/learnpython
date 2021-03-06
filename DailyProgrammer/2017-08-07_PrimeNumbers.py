## Find the nearest prime numbers before and after a given integer

import math

input_integer = input("Enter an integer: ")

boolean_list = [True for i in range(2,input_integer+1)]
for i in range(2,int(math.sqrt(input_integer)+1)):
    if boolean_list[i] is True:
        j = 0
        for num in range(0,input_integer+1):
            if input_integer+1 > i**2+num*i:
                j = i**2+num*i
                #print j
                boolean_list[j-2] = False

#print boolean_list
primes = [i+2 for i in range(0,len(boolean_list)) if boolean_list[i] == True]
# The highest prime below a given integer
if primes[-1] == input_integer:
	print "%d is a prime number." % input_integer
else:
	print primes[-1]
