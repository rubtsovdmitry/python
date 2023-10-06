def my_function(digit):                                                                           
    our_dict = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    return our_dict[digit]

# ввод цифры
while True:
    digit = input("%75s" % "Введите число от 1 до 12: ")    
    try:
        digit = int(digit)
        if digit < 1 or digit > 12:
             print("%74s" % "Вы ввели цифру вне диапазона.")
             continue
        else:
            break
    except:
        print("%74s" % "Вы ввели текст.")

print("%74s" % "Числительное:", my_function(digit))