for x in range(1, 101):
    for y in range(1, x):
        for z in range(y, x):
            if x == y * y + z * z:
                print("{} = {}**2 + {}**2,".format(x, y, z))
