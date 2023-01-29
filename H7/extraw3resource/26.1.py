str = ""

for row in range(0, 15):
    for column in range(0, 18):
        if (
            ((row <= 2 or (row > 5 and row < 9) or row >= 12) and column < 18)
            or ((row > 2 and row < 6 and column < 4))
            or (row > 8 and row < 12 and column > 13)
        ):
            str += "O"
        else:
            str += " "
    str += "\n"
print(str)
