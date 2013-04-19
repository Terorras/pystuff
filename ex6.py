#These set four variables, some of them contain format characters.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#These two lines print two of the variables, which contain the other two variables.
print x
print y
#These two lines print strings that contain format characters, which
# refer to two of the variables set at the beginning of the script.
print "I said: %r." % x
print "I also said: '%s'." % y

#These two lines set two variables, one of which is a string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#This line prints the two variables together, placing the first variable 
# into the string that is the second
print joke_evaluation % hilarious
#These two lines  define two new variables
w = "This is the left side of..."
e = "a string with a right side."
#This line combines the two variables as a single string, and prints them.
print w + e