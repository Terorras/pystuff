#for i in range(1, 101):
#   print i*'*', i*'#'

#for i in range(1, 501):
#    if i % 3 == 0 and i % 5 == 0:
#        print 'fizzbuzz'
#    elif i % 3 == 0:
#        print 'fizz'
#    elif i % 5 == 0:
#        print 'buzz'
#    else:
#        print i

for i in range(1, 101):
    if i * 21 < 100:
        print '   ', i * 21
    elif i * 21 < 1000:
        print '  ', i * 21
    elif i * 21 < 10000:
        print ' ', i * 21
    elif i * 21 < 100000:
        print '', i * 21
