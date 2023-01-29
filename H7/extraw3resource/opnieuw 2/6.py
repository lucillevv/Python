even = 0
oneven = 0

for x in range(1, 10):
    if x % 2 == 0:
        even += 1
    else:
        oneven += 1

print("aantal even nummers is {} en aantal oneven is {}".format(even, oneven))
