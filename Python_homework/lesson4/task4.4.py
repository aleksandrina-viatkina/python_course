my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_my_list = [el for el in my_list if my_list.count(el) < 2]
print(new_my_list)
