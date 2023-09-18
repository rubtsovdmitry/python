digit = int(input("%40s" % "Введите число: "))

dividers_list = []
while digit >= 2:
    divider = 2
    while digit % divider != 0:
        divider += 1
    dividers_list.append(divider)
    digit //= divider
print("%39s" % "Простые делители:", dividers_list)
print("%39s" % "Наибольший простой делитель:", max(dividers_list))