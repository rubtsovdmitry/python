def my_def(a, b):
    if b == 0:                                              
        return a
    else:
        return my_def(b, a % b)


a = int(input("%100s" % "Введите целое число (a): "))
b = int(input("%100s" % "Введите целое число (b): "))

result = my_def(a, b)

print("%99s" % result)