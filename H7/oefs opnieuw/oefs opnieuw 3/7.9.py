from random import randint

print("Ik raad het getal in jouw hoofd (1-1000) ")

hoogste = 1000
laagste = 1
pogingen = 0

while True:
    gok = randint(laagste, hoogste)
    print("mijn gok is", gok)
    pogingen += 1
    hulp = input("geef me een tip aub ")
    if hulp == "L":
        hoogste = gok
    if hulp == "H":
        laagste = gok
    if hulp == "C":
        break
print(
    "hoera juist geraden het getal was {}, geraden in {} pogingen".format(gok, pogingen)
)
# weer niet zo slim soms zelfde getallen raden
