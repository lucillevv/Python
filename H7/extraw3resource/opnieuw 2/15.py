import re

p = input("geef een passwoord in ")

x = True

while x:
    if len(p) < 6 or len(p) > 16:
        break
    elif not re.search("[a - z]", p):
        break
    elif not re.search("[A - Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif not re.search("[0 - 9]", p):
        break
    else:
        print("valid")
        x = False
        break

if x:
    print("Not a Valid Password")


# zou hier niet zelf opkomen
