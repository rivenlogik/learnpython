name = 'Travis J. Munson'
age = 31 # not a lie
height = 72.0 # inches
weight = 240.0 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
metric_weight_kg = weight / 2.2
metric_height_cm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In metric centimeters that is %dcm tall." % metric_height_cm
print "He's %d pounds heavy." % weight
print "In metric kilograms that is %dkg." % metric_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
