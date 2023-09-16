from math import sqrt

# ввод данных
a = float(input("%50s" % """Введите "a" (a не равно 0): """))
b = float(input("%50s" % """Введите "b": """))
c = float(input("%50s" % """Введите "c": """))

# вычисление дискриминанта
d = (b ** 2 - 4 * a * c) 
if d == 0:    
    x = (-b) / (2 * a)
    print("%49s" % "Значение функции:", x)
elif d > 0:    
    x = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("%49s" % "У функции два значения:", round(x, 4), "и", round(x2, 4))
else:
    print("%49s" % "Уравнение не имееет корней.")