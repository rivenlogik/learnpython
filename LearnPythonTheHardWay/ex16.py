from sys import argv

script, filename = argv
# Instructions
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")
# Open the file in write mode
print "Opening the file..."
target = open(filename, 'w')

# Not needed, since we open the file with 'w' which auto truncates
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# Get input for writing to file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# Write the lines to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Close the file
print "And finally, we close it."
target.close()
