for i in range(int(raw_input('Enter a number: ')), int(raw_input('Enter another: '))):
    if i % 3 == 0 and i % 5 == 0:
        print "fizzbuzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i
