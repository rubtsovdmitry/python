def my_5(password):                                                                     # проверка на наличие букв в верхнем регистре
    result = "ненадёжный"
    for i in password:
        if "A" <= i <= "Z":
            result = "надёжный"
    return result


def my_4(password):                                                                     # проверка на наличие букв в нижнем регистре
    result = "ненадёжный"
    for i in password:
        if "a" <= i <= "z":
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_5(password)


def my_3(password):                                                                     # проверка на наличие букв в пароле
    result = "ненадёжный"
    for i in password:
        if i.isdigit() == False:
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_4(password)
    

def my_2(password):                                                                     # проверка на наличие цифр в пароле
    result = "ненадёжный"
    for i in password:
        if i.isdigit() == True:
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_3(password)
    

def my(password):                                                                       # проверка на длину пароля
    good_len = 8
    test = "надёжный" if len(password) >= good_len else "ненадёжный"   
    if test == "ненадёжный":
        return test
    elif test == "надёжный":        
        return my_2(password)


while True:
    password = input("%50s" % "Введите ваш пароль: ")
    rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    test = True
    for i in password:
        if i in rus_alphabet or i in rus_alphabet.upper():
            test = False        
    if test:
        break
    else:
        print("%49s" % "Вы ввели пароль на русском языке.")
        print()

print("%49s" % "Ваш пароль:", my(password))