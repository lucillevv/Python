for x in range(1, 6):
    num = x * "*"
    print(num)
    if x == 5:
        for x in range(4, 0, -1):
            num = x * "*"
            print(num)
