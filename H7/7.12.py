for z in range(1, 101):
    for i in range(1, z):
        for j in range(i, z):
            if z == i * i + j * j:
                print("{}= {}**2 + {}**2".format(z, i, j))
