str = ""

for row in range(0, 7):
    for column in range(0, 7):
        if column == 3 or (row == 0 and (column > 0 and column < 6)):
            str += "*"

        else:
            str += " "
    str += "\n"
print(str)
