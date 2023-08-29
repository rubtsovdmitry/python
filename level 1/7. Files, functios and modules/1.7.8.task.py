def my_calculate(digit1, sign, digit2):                                                                 # сама логика калькулятора
    if sign == "+":                                                                                         
        return digit1 + digit2                                                                          # функция выполняется до первого return
    elif sign == "-":
        return digit1 - digit2
    elif sign == "/" and digit2 != 0:
        return digit1 / digit2
    elif sign == "/" and digit2 == 0:
        return " Деление на ноль невозможно."
    else:
        return digit1 * digit2


# ввод и проверка данных
digit1_test = ""                                                                                        # создадим переменную для запуска цикла
digit2_test = ""                                                                                        # создадим переменную для запуска цикла
sign = ""                                                                                               # создадим переменную для запуска цикла
SIGN = ("+", "-", "*", "x", "х", "/")                                                                   # создадим константу с набором возможных операций (x - англ., х - русская)
while digit1_test.isdigit() == False and digit2_test.isdigit() == False:                                # будет работать цикл, пока введённые переменные не будут соответствовать условию
    try:                                                                                                # проверка ввода для цифр
        digit1 = float(input("Введите первую цифру (если цифра дробная, то использовать точку): "))        
        digit2 = float(input("Введите вторую цифру (если цифра дробная, то использовать точку): "))
    except:
        print("Одна из цифр, которую Вы ввели не является цифрой.")
    else:
        digit1_test = str(int(digit1))          
        digit2_test = str(int(digit2))          
while sign not in SIGN:                                                                                 # проверка знака действия 
    sign = input("Введите знак операции: ")          

result = my_calculate(digit1, sign, digit2)
print(f'{digit1} {sign} {digit2} = {result}')