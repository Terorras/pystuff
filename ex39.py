from sys import exit

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'

}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['PA'] = 'Philidelphia'

states['Pennsylvania'] = 'PA'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
print "Pennsylvania's abbrevation is: ", states['Pennsylvania']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s." % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s." % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

city = cities.get('Tx', 'Does Not Exist')
print "The city for the state 'Tx' is: %s" % city

while True:
    choice = raw_input('Add to the list? ')

    if 'yes' in choice:
        choice = raw_input("A state abbreviation or a city? ")
        
        if 'state' in choice:
            new_state1 = raw_input('State: ')
            new_abbrev1 = raw_input('Abbreviation: ')
            states[new_state1] = new_abbrev1
            print "New State:", new_state1, states[new_state1]
            print "New List of States:"
            print states
        elif 'city' in choice:
            new_city1 = raw_input('City: ')
            new_citycon1 = raw_input('Abbreviation of City\'s State: ')
            cities[new_citycon1] = new_city1
            print "New City:", new_citycon1, new_city1
            print "New List of Cities:"
            print cities
    else:
        print 'k'
        exit(0)
