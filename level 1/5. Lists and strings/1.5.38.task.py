# ввод данных
my_list = []
while True:
    digit = input("%100s" % "Введите целое число, которое будет элементом списка (для отмены просто нажать \"Enter\"): ")
    if digit == "":
        break
    else:        
        try:
            digit = int(digit)
            my_list.append(digit)                    
        except:
            print("%99s" % "Вы ввели не цифры.")

# 
if len(my_list) == 0:
    print("%99s" % "У вас пустой список.")
elif len(my_list) == 1:
    print("%99s" % "ваш список содержит всего один элемент.")
elif len(my_list) > 1:
    flag_up = 1
    flag_down = 1
    flag_middle = 1
    temp = my_list[0]
    for i in my_list:
        if i > temp:
            flag_down = 0
            flag_middle = 0            
            temp = i
        if i == temp:
            pass        
        if i < temp:
            flag_up = 0
            flag_middle = 0
            temp = i    
    if my_list[0] == my_list[-1] and flag_middle == 1:
        print("%99s" % "Все элементы списка равны.")
    elif flag_up == 1:
        print("%99s" % "Все элементы в списке отсортированы по возрастанию.")
    elif flag_down == 1:
        print("%99s" % "Все элементы в списке отсортированы по убыванию.")
    else:
        print("%99s" % "Список не отсортирован.")