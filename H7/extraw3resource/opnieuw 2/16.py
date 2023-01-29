list = []

for x in range(100, 401):
    i = str(x)
    if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0):
        list.append(i)

print(", ".join(list))
