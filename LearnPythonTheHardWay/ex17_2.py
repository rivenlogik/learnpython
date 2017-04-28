from sys import argv

# Grab variables, open the destination file
# Write the contents from opening and reading the from_file
script, from_file, to_file = argv
open(to_file,'w').write(open(from_file).read())
# Substitute variables with argv array
#open(argv[2],'w').write(open(argv[1]).read()) ; print "Done!"

# Just for kicks, print all done
print "Alright, all done."

# We want to do a file.close() to free up resources in the system
