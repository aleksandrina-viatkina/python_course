l = input('Введите последовательность ')
l = list(l)
i = 1
for el in range(1, len(l), 2):
    l[i - 1], l[i] = l[i], l[i - 1]
    i += 2
print((', ').join(l))
