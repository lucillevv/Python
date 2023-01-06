numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
oneven = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        oneven += 1
print("even = {} en oneven = {}".format(even, oneven))
