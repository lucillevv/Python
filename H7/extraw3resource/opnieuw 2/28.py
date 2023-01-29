str = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 and column == 5) and row != 6:
            str += "*"
        else:
            str += " "
    str += "\n"
print(str)
