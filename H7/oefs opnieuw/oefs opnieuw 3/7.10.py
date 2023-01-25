num = int(input("geef een getal in "))

for i in range(2, num):
    if (num % i) == 0:
        print(num, "is geen priemgetal")
        print(i, "keer", num // i, "is", num)
        break
else:
    print(num, "is een priemgetal")
