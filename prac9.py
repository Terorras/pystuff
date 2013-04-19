from sys import argv

script, filename, change = argv

print "This script will edit %s with the change requested, %s." % (filename, change)
print "Opening the file..."
openfile = open(filename)

print "Here are the current contents of the file:"
print openfile.read()
openfile.close()

print "The file will now be erased and replaced with %s. Are you sure you want to do this?" % change
raw_input('Hit CTRL-C to cancel, or enter to continue. ')

print "Opening the file to write..."
openfilew = open(filename, 'w')

print "Writing to the file..."
openfilew.write(change)

print "The requested change has been writen to the file."
