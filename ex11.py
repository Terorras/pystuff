print "How old are you?",
age = int(raw_input())
age_in_months = age * 12
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = int(raw_input())
weight_in_kg = weight * .453592
print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)
print "Your age in months is %r." % age_in_months
print "Your weight in kilograms is %r." % weight_in_kg