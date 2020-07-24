rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('numbers_task4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in lines:
        i = i.split()
        new_line = rus[i[0]] + i[1] + i[2]
        new_file.append(f'{new_line} \n')
    print(new_file)

with open('new_numbers_task4.txt', 'w', encoding='utf-8') as f2:
    f2.writelines(new_file)