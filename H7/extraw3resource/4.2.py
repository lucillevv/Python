
for x in range(6):
    for i in range(x):
        print("*", end=" ")
    print()
    if x == 5:
        for y in range(4, 0, -1):
            for j in range(y):
                print("*", end=" ")
            print()
