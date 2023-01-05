for z in range(1, 101):
    for x in range(1, 9):
        for y in range(1, x):
            if z == (x * x) + (y * y):
                print("{} = {} ** 2 + {} ** 2".format(z, x, y))
