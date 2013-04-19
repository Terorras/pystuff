from sys import argv

script, filename = argv

optxt = open(filename, 'w+r')
print optxt.read()

raw_input('Edit it? ')

change = raw_input('What do you want this file to say? ')

optxtw = open(filename, 'w')
optxtw.write(change)
print "Done"
