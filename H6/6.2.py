klinker = str.lower(input("geef een string in: "))

aantal = 0

if "a" in klinker:
    aantal += 1
if "o" in klinker:
    aantal += 1
if "i" in klinker:
    aantal += 1
if "e" in klinker:
    aantal += 1
if "u" in klinker:
    aantal += 1

if aantal == 0:
    print("er zitten geen klinkers in", klinker)
if aantal == 1:
    print(" er zit 1 verschillende klinker in", klinker)
else:
    print("er zitten {} verschillende klinkers in ".format(aantal), klinker)
