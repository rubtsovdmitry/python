a = float(input("%50s" % "Введите длину стороны a: "))
b = float(input("%50s" % "Введите длину стороны b: "))
c = float(input("%50s" % "Введите длину стороны c: "))

our_set = set()                                                     # значительно проще определить количество равных сторон с помощью множества, чем городить условия
our_set.update([a, b, c])                                           # запись с добавлением сразу списка элементов в множество

if len(our_set) == 1:
    print("%49s" % "Равносторонний треугольник")
elif len(our_set) == 2:
    print("%49s" % "Равнобедренный треугольник")
else:
    print("%49s" % "Разносторонний треугольник.")