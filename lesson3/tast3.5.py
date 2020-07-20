def sum_str():
    total_sum = 0
    while True:
        my_str = input('Введите строку, разделенную пробелами ').split()
        res = 0
        try:
            for i in my_str:
                res += int(i)
            total_sum += res
            print(total_sum)
        except ValueError:
            res = total_sum
            print(total_sum)
            break


sum_str()
