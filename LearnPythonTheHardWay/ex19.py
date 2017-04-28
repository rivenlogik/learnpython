# Define the function that prints the cheese and cracker amounts
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes_of_crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Call the function using normal numbers for arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# Call the function using variables for arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# Call the function using math on regular numbers for arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Call the function using variables and math for arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
