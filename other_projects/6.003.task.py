import pyinputplus, random

def my_def():    
    sign = random.randint(1, 2)                                                     # генерация знака
    sign = "+" if sign == 1 else "-"
    a = random.randint(1, 99)                                                       # генерация числа
    b = random.randint(1, 99)
    if sign == "-":
        result = (f"{max(a, b)} {sign} {min(a, b)} = ", (max(a, b) - min(a, b)))
    else:
        result = (f"{a} {sign} {b} = ", (a + b))
    return result                                                                   # вернёт кортеж из задания и его решения ('77 - 38 = ', 39)

print() 
diapazon = range(20)                                                                # количество вопросов
mistakes = 0                                                                        # сюда копим ошибки
for i in diapazon:
    temp = my_def()
    try:
        result = pyinputplus.inputInt(prompt=temp[0], timeout=30)                   # 30 секунд на ответ, ответ не цифра не является ошибкой
        if result != temp[-1]:                                                      # ответ не верен - ошибка
            print("Ошибка.")    
            mistakes += 1
    except:
        print("Время вышло.")                                                       # ответ не верен - ошибка
        mistakes += 1

print()
print(f"Количество ошибок: {mistakes}")
print()