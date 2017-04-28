# print the sentence
print "I will now count my chickens:"

# Print out the number of hens and roosters, order of operations taken into account
# 25 + 30/6 == 25 + 5 == 30
print "Hens", 25 + 30 / 6
# 25 * 3 == 75 % 4 = remainder of 3 so 100-3 = 97
print "Roosters", 100 - 25 * 3 % 4

# print the sentence
print "Now I will count the eggs:"

# order of operations
# 3 + 2 + 1 - 5 + (4%2) - (1/4) + 6
# 7 + (4%2) - (1/4)
# 7 + 0 - 0 == 7 (no floaing point for 1/4 to be 0.25)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# print the question
print "Is it true that 3 + 2 < 5 - 7?"

# 3+2 < 5-7 == 5 < -2 = False
print 3 + 2 < 5 - 7

# Print the questions and answers
print "What is 3 + 2?", 3 + 2
print "what is 5 - 7?", 5 - 7

# Print the sentence
print "Oh, that's why it's False."

#Again
print "How about some more."

# True, True, False
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
