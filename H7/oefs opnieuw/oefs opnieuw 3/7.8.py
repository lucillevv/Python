from random import randint

rand = randint(1, 1000)
poging = 0

while True:
    gok = int(input("raad het getal "))
    poging += 1
    if gok < rand:
        print("Hoger!")
        continue
    if gok > rand:
        print("Lager!")
        continue
    else:
        print("hoera je hebt het geraden in {} pogingen".format(poging))
