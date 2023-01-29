sample = "Python 3.2"
letters = 0
digits = 0

for x in sample:
    if x.isdigit():
        digits += 1
    if x.isalpha():
        letters += 1

print(letters, digits)
