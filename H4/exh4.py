# oefening 4.2
pi = 3.14159
straal = 3
gem_cirkel = str(straal**2 * pi)
print("de oppervlakte van een cirkel met straal 3 is " + gem_cirkel)

# oef 4.3

BEDRAG = 797
bedrag = 797

DOLLARS_BEDRAG = 100
KWARTJES_BEDRAG = 25
DUBBELTJES_BEDRAG = 10
STUIVERS_BEDRAG = 5
CENTEN_BEDRAG = 1

dollars = int(bedrag / DOLLARS_BEDRAG)
print(dollars)
bedrag -= dollars * DOLLARS_BEDRAG
kwartjes = int(bedrag / KWARTJES_BEDRAG)
print(kwartjes)
bedrag -= kwartjes * KWARTJES_BEDRAG
dubbeltjes = int(bedrag / DUBBELTJES_BEDRAG)
print(dubbeltjes)
bedrag -= dubbeltjes * DUBBELTJES_BEDRAG
stuivers = int(bedrag / STUIVERS_BEDRAG)
print(stuivers)
bedrag -= stuivers * STUIVERS_BEDRAG
centen = int(bedrag / CENTEN_BEDRAG)
print(centen)

print(BEDRAG, "bestaat uit de het volgende")
print("dollars:", dollars)
print("kwartjes:", kwartjes)
print("dubbeltjes:", dubbeltjes)
print("stuivers:", stuivers)
print("centen:", centen)

# oef 4.4

a = 17
b = 23
print("a =", a, "en b =", b)
a += b
# Voeg hier twee regels toe om a en b om te wisselen
print("a =", a, "en b =", b)
b = a - b
a -= b
print("a =", a, "en b =", b)
