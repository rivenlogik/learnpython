# Number of cars
cars = 100
# Maximum people in a car
space_in_a_car = 4
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Cars not driven is the number of cars minus drivers available
cars_not_driven = cars - drivers
# Number of cars driven = drivers available
cars_driven = drivers
# Carpool capacity is the number of cars driven * the space available in each car
carpool_capacity = cars_driven * space_in_a_car
# The average passengers is the total number of passengers required divided by the number of cars available to be driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
