for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                num1 = 1000 * a + 100 * b + 10 * c + d
                num2 = 1000 * d + 100 * c + 10 * b + a
                if num2 == 4 * num1:
                    print("a= {}, b= {}, c= {} en d = {}".format(a, b, c, d))
