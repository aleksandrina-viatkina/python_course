time_user_sec=int(input('Введите время в секундах '))
time_hours = time_user_sec // 3600
time_min = (time_user_sec % 3600)//60
time_sec = (time_user_sec % 3600)%60
print(f'{time_hours:02}:{time_min:02}:{time_sec:02}')