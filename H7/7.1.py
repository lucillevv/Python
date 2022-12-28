num = int(input("geef een getal: "))
i = 0

while i < 10:
    totaal = num * (i + 1)
    i += 1
    print("{} * {} = {}".format(i, num, totaal))
