# import the argv feature from the sys module for accepting arguments
from sys import argv
# unpack the arguments to variables
script, filename = argv
# open the filename and assign file object to txt
txt = open(filename)
# print the contents of the file object 'txt'
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# Ask the user to input the filename again
print "Type the filename again:"
file_again = raw_input("> ")
# print the file object 'file_again'
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
