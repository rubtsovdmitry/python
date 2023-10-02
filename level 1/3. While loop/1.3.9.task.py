import math

def my_function(last_point_x, last_point_y, x, y):
    dist = math.sqrt((last_point_x - x) ** 2 + (last_point_y - y) ** 2)
    return dist


print("%125s" % "Программа считает периметр многоугольника по введённым точкам в системе координат на плоскости.")
print("%125s" % "Пусть значения координат будут целыми цислами.")
print("%125s" % "Чтобы получился многоугольник, а не прямая координаты не должны лежать на одной линии.")
point = 1
perimetr = 0
while True:
    x = input("%126s" % f"Введите координаты {point}-й точки по оси абсцисс: ")
    y = input("%126s" % f"Введите координаты {point}-й точки по оси ординат: ")
    if x == "" or y == "":                                                                  # здесь цикл прерывается по условию задачи (совместно со следующим условием прерывания цикла является избыточным)
        break
    try:
        x = int(x)
        y = int(y)
    except:                                                                                 # здесь цикл прерывается по если введены некорректные данные
        print("%125s" % "Введены не числа.")
        break
    if point == 1:                                                                          # запомним координаты первой точки
        first_x = int(x)
        first_y = int(y)
    if point > 1:
        perimetr += my_function(last_point_x, last_point_y, x, y)
    last_point_x = x
    last_point_y = y
    point += 1                                                                              # следующая точка

if point <= 3:
    print("%125s" % "Вы ввели всего две точки. Не получилась фигура многоугольника.")
else:
    perimetr += my_function(last_point_x, last_point_y, first_x, first_y)

print("%125s" % "Периметр многоугольника", int(perimetr))