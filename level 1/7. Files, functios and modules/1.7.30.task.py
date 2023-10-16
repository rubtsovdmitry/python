import random 

def new():
    number = ""
    min_digit = 1
    max_digit = 9
    count = 4
    while count > 0:
        x = random.randint(min_digit, max_digit)
        number += str(x)
        count -= 1
    number += " "
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters = 33
    count = 3    
    while count > 0:
        x = random.randint(1, letters)
        number += alphabet[x - 1].upper()
        count -= 1
    return number


def old():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters = 33
    count = 3
    number = ""
    while count > 0:
        x = random.randint(1, letters)
        number += alphabet[x - 1].upper()
        count -= 1
    number += " "
    min_digit = 1
    max_digit = 9
    count = 3
    while count > 0:
        x = random.randint(min_digit, max_digit)
        number += str(x)
        count -= 1
    return number


def my_number():
    x = random.randint(1, 2)
    if x == 1:
        return old()
    else:
        return new()


print(my_number())