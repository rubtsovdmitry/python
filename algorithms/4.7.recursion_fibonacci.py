def fibo(i):                                                        # функция вычисляет число Фибоначчи по порядковому номеру числа
    if i == 1:                                                      # базовый случай
        return 1
    elif i == 2:                                                    # базовый случай
        return 1
    return fibo(i - 1) + fibo(i - 2)


digit = int(input("Введите сколько цифр Фибоначчи вывести (целое число): "))

diapazon = range(1, digit + 1)
result = [fibo(i) for i in diapazon]

print(result)