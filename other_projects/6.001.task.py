import random

def my_def(digit):
    if digit == 2:
        sign = random.randint(1, 2)                                                     # генерация знака
        sign = "+" if sign == 1 else "-"
        a = random.randint(1, 99)                                                       # генерация числа
        b = random.randint(1, 99)
        if sign == "-":
            result = f"{max(a, b)} {sign} {min(a, b)} = "
        else:
            result = f"{a} {sign} {b} = "
    elif digit == 3:
        sign = random.randint(1, 2)                                                     # генерация знака
        sign = "+" if sign == 1 else "-"
        a = random.randint(1, 999)                                                      # генерация числа
        b = random.randint(1, 999)
        if sign == "-":
            result = f"{max(a, b)} {sign} {min(a, b)} = "
        else:
            result = f"{a} {sign} {b} = "
    return result


# ввод данных
while True:
    try:
        digit = input("%100s" % "Введите порядок числа (2 или 3): ")
        print()
        digit = int(digit)
    except:
        print("%99s" % "Вы ввели не цифры.")
        print()
    else:
        if 2 <= digit <= 3:
            break
        else:
            print("%99s" % "Вы ввели не тот порядок.")
            print()
            continue

buf = open("./6.001.task.txt", "w")
for a in range(55):                                                                     # количество строк на листе
    for b in range(6):                                                                  # количество столбцов
        s = "%15s" % my_def(digit)
        buf.write(s)                                                                    # дописываем строку с каждой новой итерацией в цикле
    s = "\n"                                                                            # с окончанием вложенного цикла, заканчивается и строка примеров, переходим на новую строку
    buf.write(s)                                                                        # здесь происходит запись по-строчно
buf.close()