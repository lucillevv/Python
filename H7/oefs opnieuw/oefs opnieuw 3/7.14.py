for a in range(1, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(1, 9):
                num1 = 1000 * a + 100 * b + 10 * c + d
                num2 = 1000 * d + 100 * c + 10 * b + a
                if num2 == 4 * num1:
                    print("A={}, B={}, C={} & D={}".format(a, b, c, d))
