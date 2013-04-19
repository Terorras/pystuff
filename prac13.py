from sys import argv

script, in_file = argv

txt = open(in_file)

readtxt = txt.read()

print readtxt
