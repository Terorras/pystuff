from sys import argv

script, filename = argv

something = open(filename)
readsomething = something.read()

print len(readsomething)
print readsomething
