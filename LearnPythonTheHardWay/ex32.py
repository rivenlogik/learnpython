the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# STUDY DRILL #2
#elements = range(0, 6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# STUDY DRILL #3
"""
List methods
append() = Add an element
extend() = Add all elements to another list
insert() = insert an item at the defined index
remove() = remove an item from the list
pop() = remove and return an element from the list
clear() = remove all items from the list
index() = return the index of a matched item in the list
count() = return the count of number of items passed as an argument
sort() = sort items in a list in ascending order
reverse() = reverse the order of items
copy() = returns a shallow copy of the list
"""
