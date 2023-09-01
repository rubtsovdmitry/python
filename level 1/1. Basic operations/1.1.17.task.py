from math import pi                         # подключение дополнительной константы из модуля math
print()

r = float(input("Введите радиус: "))        # ввод радиуса без единиц измерения                                                                                                

area = pi * r ** 2                          # формула для площади круга
volume = 4 / 3 * pi * r ** 3                # формула для объёма шара

print(area)
print(volume)