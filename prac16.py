from sys import argv
from os.path import exists

script, filename = argv

print "Does the file exist? %s" % exists(filename)
raw_input('If the above was \'True\', than continuing will erase and replace it. Continue?')

txt = open(filename, 'w')
txt.write(raw_input('What do you want the file to be? '))
txt.close()

print "Here is the new file:"
rtxt = open(filename)
print rtxt.read()
