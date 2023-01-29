for x in range(6):
    for y in range(x):
        print("*", end=" ")
    print()
    if x == 5:
        for x in range(4, 0, -1):
            for y in range(x):
                print("*", end=" ")
            print()
