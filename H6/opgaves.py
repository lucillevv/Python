# p 53

print(1 / 2 > 0.5)
print(1 / 2 < 0.5)
print(1 / 2 == 0.5)

print(1 / 3 > 0.33)
print(1 / 3 < 0.33)
print(1 / 3 == 0.33)

# is een integer even of oneven
from pcinput import getInteger

a = getInteger("voer hier een integer in: ")

if a % 2 == 0:
    print(a, "is even")
else:
    print(a, "is oneven")

# p61

gewicht = float(input("wat is het gewicht van uw koffer? "))

if gewicht > 20:
    print("er moet een toeslag betaald worden van 25 voor te zwaar gewicht")
elif gewicht == 20:
    print("poeh dat gewicht is net goed")
else:
    print("goede reis")
