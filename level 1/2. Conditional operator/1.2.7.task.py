quantity = int(input("%50s" % "Введите количество сторон: "))

result = "Введены неверные данные" if quantity < 3 or quantity > 10 else ("Это треугольник" if quantity == 3 else ("Это " + str(quantity) + "-х(ти)-угольник"))
print("%49s" % result)