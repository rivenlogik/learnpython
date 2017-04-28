# Set x to the joke sentence
x = "There are %d types of people." % 10
# Binary and do_not variables
binary = "binary"
do_not = "don't"
# Set y to the punch line
y = "Those who know %s and those who %s." % (binary, do_not)

# Print both lines of the joke
print x
print y

# Repeat the joke using a different formatting operator
# %r is best for debugging variables attempting to print
print "I said: %r." % x
print "I also said: '%s'." % y

# Set joke funniness to 0
hilarious = False
# State joke funniness is 0
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the joke result
print joke_evaluation % hilarious

# Make two strings for concatenation
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate the strings
print w + e
