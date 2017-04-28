people = 10
cars = 20
trucks = 15

# Check if cars > people and print a statement, else check if cars < people
# and print a statement, if they are equal say we can't decide
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

# If trucks > cars that's too many, if cars > trucks then take the trucks
# If equal, can't decide
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

# If people > trucks then take the trucks, otherwise stay home
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

#STUDY DRILL 3
if people > trucks and cars > trucks:
    print "We have lots of cars."

if people < trucks and cars > trucks:
    print "We need more cars."
