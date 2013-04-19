from sys import argv

script, filename = argv

txt = open(filename, 'w')

print "This script will open and write things to %s." % filename

change = raw_input("What do you want to write? ")

print "You want to write \"%s\" to %s. If this is correct, hit enter. If not, hit CTRL-C." % (change, filename)
raw_input("Well? ")

txt.write(change)
