num_user = int(input('Введите количество небходимых товаров '))
catalog_list = []
goods = {}
analitics_dict = {
    '"название":': [],
    '"цена":': [],
    '"количество":': [],
    '"ед":': []
}
num_goods = 1
while num_user >= num_goods:
    position = input('Наименование товара ')
    price = float(input('Стоимость товара '))
    quantity = int(input('Количество товара '))
    unity = input('Единица измерения товара ')
    goods = (num_goods, {'"название":': position, '"цена":': price, '"количество":': quantity, '"ед":': unity})
    catalog_list.append(goods)
    num_goods = num_goods + 1
    analitics_dict['"название":'].append(position)
    analitics_dict['"цена":'].append(price)
    analitics_dict['"количество":'].append(quantity)
    analitics_dict['"ед":'].append(unity)
print('[')
for i in catalog_list:
    print(i)
print(']')
for key in analitics_dict:
    print(key, analitics_dict[key])
