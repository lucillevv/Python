str = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 0 or column == 4) and (row != 0 or row != 6):

            str += "*"
        else:
            str += " "
    str += "\n"
print(str)
# idk man
