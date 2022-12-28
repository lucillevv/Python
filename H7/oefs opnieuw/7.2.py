num = int(input("geef een getal in "))

for x in range(1, 11):
    tot = x * num
    print("{} * {} = {}".format(x, num, tot))
