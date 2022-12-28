import math

a = int(input("wat is de lengte van de eerste zijde?: "))
b = int(input("wat is de lengte van de tweede zijde?: "))


c = math.sqrt(pow(a, 2) + pow(b, 2))


print("de lengte van c is {:.3f}".format(c))
