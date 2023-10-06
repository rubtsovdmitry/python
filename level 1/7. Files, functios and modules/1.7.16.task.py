def my_function(quntity):
    FIRST = 10.95
    SECOND = 2.95
    if quntity == 1:
        return str(FIRST)
    else:
        return (str(round(FIRST + SECOND * (quntity -1), 2)) + " $")


# ввод количества товаров в заказе
while True:
    quntity = input("%75s" % "Введите количество товаров в заказе (например, 100): ")
    try:
        quntity = int(quntity)
        if quntity < 1:
            continue
        else:
            break
    except:
        print("%74s" % "Вы ввели не цифры.")

print("%74s" % "Стоимость доставки составит:", my_function(quntity))