rating_list = [9, 8, 6, 6, 5, 3]
a = float(input('Введите произвольный элемент рейтинга '))
for i in range(len(rating_list)):
    if a > rating_list[i]:
        rating_list.insert(i, a)
        break
    elif a <= rating_list[-1]:
        rating_list.append(a)
        break
print(rating_list)