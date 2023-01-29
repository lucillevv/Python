print("multiplication table")

num = int(input("geef een nummer: "))
totaal = 0

for x in range(1, 11):
    totaal = num * x
    print("{:^2} * {:^2} = {:^2}".format(num, x, totaal))
