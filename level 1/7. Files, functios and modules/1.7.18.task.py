def my_function(digit):                                                                           
    our_dict = {
        1: "Первый",
        2: "Второй",
        3: "Третий",
        4: "Четвёртый",
        5: "Пятый",
        6: "Шестой",
        7: "Седьмой",
        8: "Восьмой",
        9: "Девятый",
        10: "Десятый"
    }
    return our_dict[digit]

# ввод цифры
while True:
    digit = input("%75s" % "Введите число от 1 до 10: ")    
    try:
        digit = int(digit)
        if digit < 1 or digit > 10:
             print("%74s" % "Вы ввели цифру вне диапазона.")
             continue
        else:
            break
    except:
        print("%74s" % "Вы ввели текст.")

print("%74s" % "Числительное:", my_function(digit))