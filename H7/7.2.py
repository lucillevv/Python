num = int(input("geef een getal: "))
totaal = 0

for x in range(1, 11):
    totaal = num * x
    print("{} * {} = {}".format(x, num, totaal))
