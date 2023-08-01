# первый вариант (его минус в том, что он выдаёт только одно значение, даже если будет два имени одной и той же длины)

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
print(max(names, key=len))
print()


# второй вариант (который будет выводить уже все имена с максимальной длиной)

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names_long = list()                                             # создадим список, в кот. будем хранить имена с максимальной длиной
long = int()                                                    # введём переменную, кот. хранит максимальную длину имени
for i in names:                                                 # обойдём все значения имён в names цикле в поиске максимальной длины имени
    if len(i) >= long:                                          # ищем максимальную длину имён
        long = len(i)                                           # обновляем значение переменной, в кот. хранится максимальная длина
for i in names:                                                 # обойдём ещё раз все значения имён в names цикле в поиске имени максимальной длины
    if len(i) == long:                                          # ищем самые длинные имена
        names_long.append(i)                                    # добавляем имена с максимальной длиной в новый список
print(names_long)