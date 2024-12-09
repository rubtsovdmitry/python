my_list = []
while True:
     digit = input("%100s" % "Введите число (для отмены введите \"Enter\"): ")
     try:
        if digit == "":
            break
        digit = float(digit)
        my_list.append(digit)
     except:
        print(("%99s" % "Вы ввели не число: "))
print()
result_list = []
for i in my_list:
    if i < 0:
        result_list.append(i)
for i in my_list:
    if i == 0:
        result_list.append(i)
for i in my_list:
    if i > 0:
        result_list.append(i)
for i in result_list:
    print("%99s" % i)