from random import randint

poging = 0

getal = int(input("geef een getal in"))

if getal < 1 and getal > 1000:
    print("getal moet binnen 1-1000 liggen")

print("de computer raadt jouw getal")

while True:
    pc = randint(1, 1000)
    print(pc)
    poging += 1
    antwoord = input("help mij")
    H = pc < getal
    L = pc > getal
    C = pc == getal
    if antwoord == H:
        randint(1, 1000) > pc
    if antwoord == L:
        randint(1, 1000) < pc
    if antwoord == C:
        pc == getal
        break

print("de pc heeft {} pogingen ondernomen".format(poging))

# klopt niet ik weet niet hoe dit moet met randint
