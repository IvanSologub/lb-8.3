#Задача №5

#Допишите функцию calc_stat(): выведите на экран суммарную статистику.

def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    total_minutes = sum(listened) // 60  # Подсчитываем общее количество минут
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {total_minutes} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))