num = int(input(" geef een getal in "))

i = 1

while i < 11:
    x = i * num
    print("{:2} * {:2} = {:2}".format(i, num, x))
    i += 1
