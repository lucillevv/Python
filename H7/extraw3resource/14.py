data = input("geef een string met letters en cijfers : ")
letter = 0
digit = 0

for x in data:
    if x.isalpha():
        letter += 1
    if x.isdigit():
        digit += 1

print("aantal letters is {}, aantal cijfers is {}".format(letter, digit))

# het tellen van letters digits en spaces met isdigit, isspace, isalpha
