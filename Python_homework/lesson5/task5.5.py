with open('file_task5.txt', 'w+', encoding='utf-8') as f:
    try:
        my_line = input('Введите числа, разделенные пробелами ')
        f.write(f'{my_line} \n')
        my_lines = f.read()
        my_lines = my_line.split()
        total = 0
        for line in my_lines:
            total += int(line)
        print(total)
    except ValueError:
        print('Неверный формат введенных данных')
