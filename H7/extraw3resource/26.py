str = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (
            (
                ((column == 1) and row > 0 and row < 3)
                or (row == 6 and column > 0 and column < 5)
                or ((row == 0) and column > 1 and column < 6)
            )
            or ((row == 3) and column > 1 and column < 5)
            or ((column == 5) and row > 3 and row < 6)
        ):
            str += "*"
        else:
            str += " "
    str += "\n"
print(str)


row = 15
col = 18
result_str = ""
for i in range(1, row + 1):
    if (i <= 3) or (i >= 7 and i <= 9) or (i >= 13 and i <= 15):
        for j in range(1, col):
            result_str = result_str + "o"
        result_str = result_str + "\n"

    else:

        result_str = result_str + "\n"
print(result_str)
