from math import sqrt

a = float(input("geef een waarde voor a"))
b = float(input("geef een waarde voor b"))
c = float(input("geef een waarde voor c"))

if a == 0:
    if b == 0:
        print("er zijn geen oplossingen")
    else:
        print(" er is 1 oplossing namelijk", -b / c)
else:
    opl = b**2 - 4 * a * c
    if opl < 0:
        print("er zijn geen oplossingen")
    if opl == 0:
        print("er is 1 oplossing")
    else:
        print(
            "er zijn 2 oplossingen nl",
            (-b + sqrt(opl)) / (2 * a),
            "and",
            (-b - sqrt(opl)) / (2 * a),
        )
# math domain error idk what to do, de oplossingen zijn hetzelfde dus idk man
