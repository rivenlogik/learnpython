# Import argv
from sys import argv
# Assign file parameter given to script
script, input_file = argv
# A function that reads the entire file
def print_all(f):
    print f.read()

# A function that goes to the beginning of the file
def rewind(f):
    f.seek(0)

# A function that will take the line count and file and print specific line
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open the file given to the script
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
# Print lines out, adding 1 to each line for lines 1,2,3.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
