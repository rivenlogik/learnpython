from sys import argv

script, filename = argv
# Print instructions
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")
# Open the file in write, auto truncates the file
print "Opening the file..."
target = open(filename, 'w')

# This isn't actually needed since we used 'w' with open()
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# Grab input lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# Concatenate lines and write to destination file
allLines = "%s, %s, and %s" % (line1, line2, line3)
target.write(allLines)
target.write("\n")
# Close the file
print "And finally, we close it."
target.close()
