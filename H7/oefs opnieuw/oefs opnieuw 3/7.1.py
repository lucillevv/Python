num = int(input("geef een getal "))


for i in range(1, 11):
    x = i * num
    print("{:2} * {:2} = {:2}".format(i, num, x))
