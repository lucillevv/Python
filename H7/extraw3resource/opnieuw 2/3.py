from random import randint

num = randint(1, 9)

gok = int(input("gok een nummer tussen 1-9: "))

while gok != num:
    gok = int(input("gok een nummer tussen 1-9: "))
print("well guessed!")
