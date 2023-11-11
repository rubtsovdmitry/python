def my_def():
    digit = input("%100s" % "Введите число (просто -enter- для выхода): ")
    if digit == "":
        return 0
    else:        
        return (my_def() + float(digit))


print("%99s" % f"Сумма всех введённых чисел равна: {my_def()}")