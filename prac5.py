from sys import argv

script, first, second, third, fourth, fifth, sixth = argv

print "So, you want your %s in %s, your %s in %s, and your %s in %s?" % (first, second, third, fourth, fifth, sixth)

age = int(raw_input("What is your age? "))
age_months = age * 12
print "Your age in months is %s." % age_months

weight = int(raw_input("What is your weight in pounds? "))
kilo = weight * .453592
print "Your weight in kilograms is %s." % kilo

height = int(raw_input("What is your height in feet? "))
height_meters = height * .3048
print "Your height in meters is %s." % height_meters

