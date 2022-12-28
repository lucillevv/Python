from random import randint

pogingen = 0

print("raad het getal in de computer zsm!")

x = randint(1, 1000)
print(x)

while True:
    num = int(input("raad het getal: "))
    pogingen += 1
    if num > x:
        print("Lager")
        continue
    if num < x:
        print("Hoger")
        continue
    if num == x:
        print("proficiat je hebt het getal geraden in {} pogingen".format(pogingen))
