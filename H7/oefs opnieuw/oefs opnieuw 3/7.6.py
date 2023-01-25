w1 = input("geef het eerste woord ")
w2 = input("geef het tweede woord ")

beide = ""

for x in w1:
    if (x in w2) and (x not in beide):
        beide += x
if beide == 0:
    print("de woorde hebben niks gemeen")
else:
    print(beide)
