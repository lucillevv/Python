temp = int(input("hoeveel wilt u omzetten"))
maat = input("C of F? ")

if maat == "F":
    C = (5 / 9) * (temp - 32)
    print("{}F = {:.0f}C".format(temp, C))
elif maat == "C":
    F = (9 * temp) / 5 + 32
    print("{}C = {:.0f}F".format(temp, F))
