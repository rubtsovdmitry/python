import math

def my_function(cathet_1, cathet_2):
    return (math.sqrt(cathet_1 ** 2 + cathet_2 ** 2))


cathet_1 = float(input("%75s" % "Введите длину 1-го катета: "))
cathet_2 = float(input("%75s" % "Введите длину 2-го катета: "))
print()
hypotenuse = my_function(cathet_1, cathet_2)
print("%74s" % "Длина гипотенузы:", hypotenuse)