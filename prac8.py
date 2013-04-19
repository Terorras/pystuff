from sys import argv

script, filename = argv

print "This script will write changes to %s." % filename

print "Opening file..."
txt = open(filename, 'w')

change = raw_input('What do you want to write to %s? ' % filename)
raw_input("Are you sure that you want to write %s to %s? (Hit CTRL-C to cancel, or enter to continue) " % (change, filename))

print "Writing to file..."
txt.write(change)
print "The changes have been written."
