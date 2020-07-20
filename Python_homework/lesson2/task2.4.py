user_str = input('Введите произвольную строку ')
user_str = user_str.split()
for ind, el in enumerate(user_str):
    print(ind, el[0:10])
