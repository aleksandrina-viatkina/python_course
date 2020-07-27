with open('file_task7.txt', 'r', encoding='utf-8') as f:
    my_lines = f.readlines()
    firm_list = []
    firm_impact = {}
    i = 0
    total_profit = 0
    for line in my_lines:
        line = line.split()
        profit = float(line[2]) - float(line[3])
        if profit > 0:
            total_profit += profit
            print(f'Прибыль {line[0]} составит {profit:.2f} y.e.')
            i += 1
        else:
            print(f'У компании {line[0]} убиток в размере {profit:.2f} y.e.')
        firm_impact = ({line[0]: profit})
        firm_list.append(firm_impact)
    av_profit = total_profit / i
    print(f'Средняя прибыль по компаниям: {av_profit:.2f} y.e.')
    firm_list.append({'average_profit': av_profit})
    print(firm_list)

import json

with open('json_task7.json', 'w', encoding='utf-8') as f_json:
    json.dump(firm_list, f_json)
