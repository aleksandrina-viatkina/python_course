with open('file_task1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст. Для окончания работы нажмите Enter ')
        f.write(f'{line} \n')
        if line == "":
            break