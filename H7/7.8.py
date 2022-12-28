from random import randint

pogingen = 0
rand = randint(1, 1000)
print(rand)

while True:
    num = int(input("Raad het random getal: "))
    pogingen += 1
    if num < rand:
        print("Hoger")

    if num > rand:
        print("Lager")

    if num == rand:
        print("Je hebt het geraden")
        break

print("je hebt {} keer geprobeerd".format(pogingen))
