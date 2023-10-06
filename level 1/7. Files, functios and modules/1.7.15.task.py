def my_function(base, price_1km, way):
    return (base + price_1km * way)


# ввод стоимости базового тарифа
while True:
    base = input("%75s" % "Введите стоимость базового тарифа (например, 100): ")
    try:
        base = float(base)
        break
    except:
        print("%74s" % "Вы ввели не цифры.")

# ввод стоимости проезда 1 км пути
while True:
    price_1km = input("%75s" % "Введите стоимость проезда 1 км пути (например, 20): ")
    try:
        price_1km = float(price_1km)
        break
    except:
        print("%74s" % "Вы ввели не цифры.")

# ввод длины поездки в км.
while True:
    way = input("%75s" % "Введите длину поездки в км (например, 10): ")
    try:
        way = float(way)
        break
    except:
        print("%74s" % "Вы ввели не цифры.")

print("%74s" % "Стоимость поездки составила:", my_function(base, price_1km, way))