from pcinput import getInteger

priem = getInteger("geef een getal ")

deler = 2
for i in range(1, priem):
    if priem % deler == 0:
        print(priem, "is not prime")
        break
    deler += 1
else:
    print(priem, "is prime")
