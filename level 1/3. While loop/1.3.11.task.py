list_of_digits = list()
while True:
    try:
        digit = int(input("Введите целое положительное число: "))
        if digit > 0:
            break
    except:
        print("Вы ввели не цифры. Попробуйте ещё раз.")
list_of_digits.append(digit)

while True:
    print(list_of_digits)
    if list_of_digits[-1] == 1:        
        break
    if list_of_digits[-1] % 2 == 0:
        list_of_digits.append(int(list_of_digits[-1] / 2))
    else:
        list_of_digits.append(list_of_digits[-1] * 3 + 1)