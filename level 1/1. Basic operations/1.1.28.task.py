def tww(temperature_air, speed_wind):
    TEMPERATURE = 10
    WIND = 4.8
    if temperature_air > TEMPERATURE or speed_wind <= WIND:
        temperature_air = round(temperature_air, 2)
    elif temperature_air <= TEMPERATURE and speed_wind > WIND:
        temperature_air = round((13.12 + (0.6215 * temperature_air) - 11.37 * (speed_wind ** 0.16) + 0.3965 * temperature_air * (speed_wind ** 0.16)), 2)
    return temperature_air


try:
    temperature_air = float(input("Введите температуру в градусах цельсия: "))
    speed_wind = float(input("Введите скорость ветра в км/час: "))
    temperature_with_wind = tww(temperature_air, speed_wind)
    print("Температура с учетом ветра:", temperature_with_wind)
except ValueError:
    print("Ошибка в вводе.")