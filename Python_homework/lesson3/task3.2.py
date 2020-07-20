def list_data(**kwargs):
    """Вывод списком данных о пользователе"""
    return list(kwargs.values())

def users_data():
    print(list_data(
        имя=input('Введите имя '),
        фамилия=input('Введите фамилию '),
        год_рождения=int(input('Введите год рождения ')),
        город_проживания=input('Введите город проживания'),
        email=input('Введите электронный адрес '),
        телефон=input('Введите номер телефона '))
    )

users_data()