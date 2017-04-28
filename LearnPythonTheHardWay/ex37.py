#### KEYWORDS ####
## Point out what each one does and use it in code ##

# "AND" - Logical
# 0 and 1 = 0
print "+++ AND Usage +++"
logand = True and False
print logand
print

#####
# "AS" - Part of with-as statement
# "With <this_file/function> as <variable>"
# The above will execute the file/function __enter__ method, the return
# from that method will be assigned to the <variable>
# Then - no matter what happens with the code executed in the following code
# block the with-as statement will still call the file/function __exit__ method
# The __exit__ method can look at the return / exception of the code block
# and act or suppress it as necessary

#With-as statement, print the first line of the file, then close it
# File object has __enter__ and __exit__ methods for handling files
print "+++ WITH-AS Usage +++"
with open('ex36_game.py') as file:
    print file.readline()
print

####
# "Assert" - Ensure that something is True
# Used well in debugging - used to prove something resolves to True
assert True
# assert False # Assertion error! (Python Error)

####
# "Break" - used to stop a loop - only 1 execution below instead of infinite
print "+++ Break Usage +++"
while True:
    print "Hi! Let's break this loop!"
    break
print

####
# Class - define a class
# __init__ function defines all variables used within the class definition
# Generally, don't introduce attributes outside the __init__ function of a class
# "Self" refers to the object instance
# ie.  jeff = Person() means self = "jeff" instance
print "+++ Class Person +++"
class Person(object):
    sex = 'male'
    def __init__(self, name, hair):
        self.name = name
        self.hair = hair

jeff = Person('Jeff', 'Brown')
print "The Person Class"
print "Name:", jeff.name
print "Hair Color:", jeff.hair
print "Sex:", jeff.sex
print

####
# Continue - don't process more of the loop, run it again
print "+++ Continue Usage +++"
for i in range(2,0,-1):
    print "Hi! Let's continue %d more time(s)!!" % i
    continue
    print "Hi2! I won't be seen!"
print

####
### def - Define a function! ###
print "+++ Def - define a function +++"
def func(text):
    print text
    print
func("I'm a function!")

####
## del - delete from a dictionary
print "+++ Del - Remove items from Dictionary +++"
dict = {'a':'dictionary', 'b': 'exists'}
print dict
del dict['a']
print "And a is removed! See:", dict
print

####
# if / elif / else statement
print "+++ If statements +++"
for i in range(0,11):
    if i <= 3:
        print "0-3!"
    elif i >= 4 and i <= 7:
        print "4-7!"
    else:
        print "8-10!"
print

####
# except statement - try an assert
print "+++ Except statement +++"
try:
    assert False
except AssertionError:
    print "Error!!!"
print

####
# exec - run a string as Python
# Good for when you have python code stored in a string variable?
print "+++ Exec statement +++"
exec 'print "some"'
print

####
# finally - Exceptions or not, do this no matter what in try/except
print "+++ Finally usage +++"
myfile = open("test.txt", "w")
try:
    myfile.write("The answer is: ")
    myfile.write(42)
except TypeError:
    pass
finally:
    print "FINALLY! Still printing!!!"
    print

####
# For loops
print "+++ For loop +++"
for i in range(0,3):
    print "For loop %d" % i
print

####
# Global - Declare a global variable
# Must be used in functions to modify global variables
# Not needed to read global variables
print "+++ Global usage +++"
globx = 0
def change_globx():
    global globx
    globx = 1
change_globx()
print globx
print

####
# in - used in for loops for lists etc
print "+++ in usage +++"
l = ['1', '2', '1', '3']
for i in l:
    print i
print

####
# lambda - creating a short anonymous function.
# commonly used with map(), reduce(), and filter() functions
# the above functions take in a function as an argument
print "+++ Lambda usage +++"
lambdalist = filter(lambda x: x % 2 == 1, range(0,20))
print lambdalist
print

####
# pass - pass this block of code
print "+++ pass usage +++"
if 1 == 1:
    pass
print

####
# raise - raise an exception when things go wrong
print "+++ Raise usage +++"
#raise TypeError("Stuff!!!!")
print

# String Escapes
print "\\ backslash"
print "\' single quote"
print "\" double quote"
print "\a bell!"
print "\b backspace!"
print "\f formfeed!"
print "\n newline!"
print "\r carriage return!"
print "\t tab!!"
print "\v vertical tab!"
