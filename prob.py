stuff = []

for i in range(1, 1001):
    if i % 5 == 0 or i % 3 == 0:
        stuff.append(i)
    else:
        pass

print sum(stuff)
