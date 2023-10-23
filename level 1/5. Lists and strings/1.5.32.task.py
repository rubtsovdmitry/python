my_list = []
while True:
    digit = input("%100s" % "Введите целое число (для отмены нажать \"Enter\"): ")
    if digit == "" and len(my_list) >= 1:
        break   
    elif digit == "" and len(my_list) < 1:        
        print("%99s" % "Вы не ввели ни одного числа.")    
        continue    
    try:
        digit = float(digit)
        if digit % 1 != 0:
            print("%99s" % "Вы ввели дробное число.")
            continue
        digit = int(digit)        
        my_list.append(digit)
    except:
        print("%99s" % "Вы ввели не цифру.")

print()
middle = int(sum(my_list) / len(my_list))
print("%99s" % f"Среднее значение введённого ряда чисел: {middle}")

print()
low = [i for i in my_list if i < middle]
count = 1
for i in low:
    print("%99s" % f"Значение {count}-е меньше среднего: {i}")
    count += 1

print()
middle_result = [i for i in my_list if i == middle]
count = 1
for i in middle_result:
    print("%99s" % f"Значение {count}-е равное среднему: {i}")
    count += 1

print()
high = [i for i in my_list if i > middle]
count = 1
for i in high:
    print("%99s" % f"Значение {count}-е больше среднего: {i}")
    count += 1