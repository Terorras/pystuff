from sys import argv

script, filename = argv

print "This script will erase %s." % filename
print """
Do you want this?
CTRL-C = No
Enter = Yes
"""
raw_input("> ")

print "Opening file..."
thing = open(filename, 'w')
print "Erasing the file..."
thing.truncate()

print "The file was deleted."
