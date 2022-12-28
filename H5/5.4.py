from math import exp

a = -1
b = 0
c = 1
d = 2
e = 3

print("e tot de {:2} is {:.5f}".format(a, exp(a)))
print("e tot de {:2} is {:.5f}".format(b, exp(b)))
print("e tot de {:2} is {:.5f}".format(c, exp(c)))
print("e tot de {:2} is {:.5f}".format(d, exp(d)))
print("e tot de {:2} is {:.5f}".format(e, exp(e)))


s = "e to the power of {:2d} is {:>9.5f}"
print(s.format(-1, exp(-1)))
print(s.format(0, exp(0)))
print(s.format(1, exp(1)))
print(s.format(2, exp(2)))
print(s.format(3, exp(3)))
