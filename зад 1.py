#Замените объединение строк на f-строку.

def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')

show_meteo(24, 'облачно')