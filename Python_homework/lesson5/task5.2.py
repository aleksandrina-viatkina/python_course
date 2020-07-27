with open('file_task2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    number_str = len(lines) #расчет количества строк
    print(f'Количество строк в файле: {number_str}')
    i=1
    for line in lines:
        line_list = line.split()
        print(f'Количество слов в {i} строке: {len(line_list)}')
        i+=1


