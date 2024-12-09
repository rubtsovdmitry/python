# ввод данных
my_list = []
while True:
    digit = input("%100s" % "Введите число, которое будет элементом списка (для отмены просто нажать \"Enter\"): ")
    if digit == "":
        break
    else:        
        try:
            digit = float(digit)
            my_list.append(digit)                    
        except:
            print("%99s" % "Вы ввели не цифры.")
while True:
    small = input("%100s" % "Введите число, нижнюю границу диапазона: ")    
    try:
        small = float(small)             
        break
    except:
        print("%99s" % "Вы ввели не цифры.")
while True:
    big = input("%100s" % "Введите число, верхнюю границу диапазона: ")    
    try:
        big = float(big)             
        break
    except:
        print("%99s" % "Вы ввели не цифры.")
#######################################################################################################################################################
result_list = [i for i in my_list if small <= i <= big]
print("%99s" % "Числа в диапазоне:")
for i in result_list:
    print("%99s" % i)