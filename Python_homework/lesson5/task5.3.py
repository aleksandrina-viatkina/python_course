with open('file_task3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    salaries = []
    for line in lines:
        last_name, salary = line.split()
        salary = float(salary)
        if salary <= 20000: #вычисляем сотрудников с зарплатой менее 20 т.р.
            print(last_name)
        salaries.append(salary)
        av_salary =sum(salaries)/len(lines)
    print(f'Средняя величина доходов сотрудников {av_salary:.2f}')
