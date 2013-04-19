from sys import argv

script, number, number2 = argv

def function(arg1, arg2):
    print "Is %d greater than %d?" % (arg1, arg2)
    print arg1 > arg2
    print "So that's the answer.\n"

print function(2, 3)

print function(5, 4)

print function(6, 7)

print function(int(raw_input('What\'s the first number you want to compare?')), int(raw_input('What\'s the second number you want to compare?')))

print function(int(number), int(number2))
