from random import randint

print("houd een getal in gedachten. ik probeer dit te raden")

pogingen = 0
hoogste = 1001
laagste = 0


while True:
    guess = randint(laagste, hoogste)
    print("ik denk dat het getal", guess, "is")
    pogingen += 1
    hulp = input("is dit juist? help mij: ")
    if hulp == "C":
        break
    elif hulp == "L":
        hoogste = guess
    elif hulp == "H":
        laagste = guess

print("ik heb hiervoor {} keer geraden".format(pogingen))

# niet zon slim programma want raadt soms dezelfde getallen
