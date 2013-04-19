from sys import argv

script, arg1, arg2 = argv

def writefile(doc, change):
    raw_input('Continue? ')
    txt = open(doc, 'w')
    txt.write(change)
    txt.close()

writefile(arg1, arg2)

print "New File:"
rtxt = open(arg1)
readtxt = rtxt.read()
print readtxt
