def my_function_2(list_of_sides):
    result = True
    for i in list_of_sides:        
        if i >= (sum(list_of_sides) / 2):
            result = False                
    return result


def my_function_1(*sides):
    list_of_sides = [i for i in sides if i > 0]                                             # составим список из трёх элементов, если все из них больше 0
    if len(list_of_sides) == 3:                                                             # проверка списка, есть ли в нём три элемента, если есть то треугольник получается
        result = my_function_2(list_of_sides)                                               # по количеству сторон проверили треугольник, теперь нужно проверить, чтобы одна из сторон не была больше или равна половине суммы всех сторон (след. функция)
    else:
        result = False
    return result


while True:
    try:
        first_side = int(input("%100s" % "Введите первую сторону треугольника: "))
        second_side = int(input("%100s" % "Введите вторую сторону треугольника: "))
        third_side = int(input("%100s" % "Введите третью сторону треугольника: "))
        break        
    except:
        print("%99s" % "Вы ввели не цифры. Попробуйте ещё раз.")
result = my_function_1(first_side, second_side, third_side)
if result:
    print("%99s" % "Из введённых сторон треугольник получится.")
else:
    print("%99s" % "Из введённых сторон треугольник не получится.")