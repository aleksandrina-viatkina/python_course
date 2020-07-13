n = int(input("Введите целое положительное число "))
max_num = n % 10
n = n // 10

while n > 0:
    if n % 10 > max_num:
        max_num = n % 10
    n = n // 10
print(max_num)
