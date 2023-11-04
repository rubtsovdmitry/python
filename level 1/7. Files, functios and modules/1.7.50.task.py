from sys import argv
from random import choice

try:
    script, first = argv         
    buf = open(f"./{first}", "r")       
    text = buf.read()                                                                                           # прочитаем текст сразу весь
    text = text.replace("\n", "")                                                                               # уберём переносы строк
    text = text.lower()                                                                                         # сделаем все буквы в нижнем регистре
    stay = " "                                                                                                  # часть символов, кот. не будем убирать из текста
    result = ""                                                                                                 # сюда будем копить модифицированный текст
    for i in text:                                  
        if i in stay or ("а" <= i <= "я"):                                  
            result += i                                 
    result = result.split(" ")                                                                                  # так создадим список из текста, где разделитель " "
    result = [i for i in result if 3 <= len(i) <= 7]                                                            # модифицируем список, где все элементы от 3 символов до 7
    result = [i.capitalize() for i in result]                                                                   # модифицируем список, теперь все элементы списка начинаются с заглавной буквы
    element_1 = choice(result)                                                                                  # первый элемент    
    element_2 = choice([i for i in result if ((8 - len(element_1)) <= len(i) <= (10 - len(element_1)))])        # второй элемент
    password = element_1 + element_2
    print(password)
except:
    print("Имя файла не существует или слишком много аргументов.")