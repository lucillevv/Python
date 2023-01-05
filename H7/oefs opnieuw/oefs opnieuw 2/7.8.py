from random import randint

num = randint(0, 1000)
i = 0

while True:
    gok = int(input("raad het getal van de computer: "))
    i += 1
    if gok < num:
        print("Hoger")
    if gok > num:
        print("lager")
    if gok == num:
        print("Hoera je hebt het geraden, hiervoor heb je {} keer geraden".format(i))
