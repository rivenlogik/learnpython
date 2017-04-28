# print the sentence
print "I will now count my chickens:"

# Print out the number of hens and roosters, order of operations taken into account
# 25 + 30/6 == 25 + 5 == 30
print "Hens", 25.0 + 30.0 / 6.0
# 25 * 3 == 75 % 4 = remainder of 3 so 100-3 = 97
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

# print the sentence
print "Now I will count the eggs:"

# order of operations - adding fp numbers
# 3 + 2 + 1 - 5 + (4%2) - (1/4) + 6
# 7 + (4%2) - (1/4)
# 7 + 0 - .25 = 6.75
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

# print the question
print "Is it true that 3.0 + 2.5 < 5.5 - 7.0?"

# 3.0 + 2.5 < 5.5 - 7.0 == 5 < -2 = False
print 3.0 + 2.5 < 5.5 - 7.0

# Print the questions and answers
print "What is 3 + 2?", 3.0 + 2.0
print "what is 5 - 7?", 5.0 - 7.0

# Print the sentence
print "Oh, that's why it's False."

#Again
print "How about some more."

# True, True, False
print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0
