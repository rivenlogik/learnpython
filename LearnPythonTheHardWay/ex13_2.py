from sys import argv

script, one, two = argv

answer = raw_input("What's 1+1? ")
finalanswer = int(answer) * int(one) * int(two)

print "Your answer of %d * the arguments provided to the script is %d" \
    % (int(answer), finalanswer)
