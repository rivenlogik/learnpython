
# ORIGINAL
'''
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
'''

# STUDY DRILL 1
'''
def numbers(num):
    """Print out numbers in a list"""
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for n in numbers:
        print n

numbers(10)
numbers(12)
'''

# STUDY DRILL 3
'''
def numbers(num,adder):
    """Print out numbers in a list"""
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + adder
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for n in numbers:
        print n

numbers(10,2)
numbers(100,20/2)
'''

# STUDY DRILL 5
def numbers(num,adder):
    """Print out numbers in a list"""
    #i = 0
    numbers = []
    for i in range(0,num,adder):
    #    print "At the top i is %d" % i
        numbers.append(i)

    #    i = i + 1
        print "Numbers now: ", numbers
    #    print "At the bottom i is %d" % i

    print "The numbers: "

    for n in numbers:
        print n

numbers(10,2)
