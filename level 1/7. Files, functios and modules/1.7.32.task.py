import random

def my_4(password):                                                                     # проверка на наличие букв в верхнем регистре
    result = "ненадёжный"
    for i in password:
        if "A" <= i <= "Z":
            result = "надёжный"
    return result


def my_3(password):                                                                     # проверка на наличие букв в нижнем регистре
    result = "ненадёжный"
    for i in password:
        if "a" <= i <= "z":
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_4(password)


def my_2(password):                                                                     # проверка на наличие букв в пароле
    result = "ненадёжный"
    for i in password:
        if i.isdigit() == False:
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_3(password)
    

def my(password):                                                                       # проверка на наличие цифр в пароле
    result = "ненадёжный"
    for i in password:
        if i.isdigit() == True:
            result = "надёжный"
    if result == "ненадёжный":
        return result
    elif result == "надёжный":        
        return my_2(password)


def small():                                                                            # генерирует маленькие буквы
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = random.randint(1, len(alphabet))
    return alphabet[x - 1]


def big():                                                                              # генерирует большие буквы
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = random.randint(1, len(alphabet))
    return alphabet.upper()[x - 1]


def digit():                                                                            # генерирует цифры
    x = random.randint(0, 9)
    return str(x)


def my_password():                                                                      # генеринует длину пароля, определяет какая функция будет генерировать символ (a/A/1)
    len_password = range(0, random.randint(8, 25))                                      # произвольная длина пароля от 8 до 25 символов
    password = ""
    for i in len_password:
        choice = random.randint(1, 3)
        if choice == 1:
            password += small()
        elif choice == 2:
            password += big()
        elif choice == 3:
            password += digit()
    return password


while True:
    password = my_password()
    if my(password) == "ненадёжный":
        continue
    else:
        print("%49s" % "Генератор пароля:", password)
        break